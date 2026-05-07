"""
Arabic command filter helpers.

Usage:
    from wbb.utils.acmd import cmd

    @app.on_message(cmd(en="ban", ar=["حظر", "بان"]))
    async def ban(_, m):
        # m.command is populated like filters.command does
        ...

You can also keep using filters.command and OR with cmd() for Arabic only:
    @app.on_message(filters.command("ban") | cmd(ar=["حظر"]))
"""
from typing import Iterable, Optional, Union

from pyrogram import filters


def _as_list(x: Optional[Union[str, Iterable[str]]]) -> list:
    if x is None:
        return []
    if isinstance(x, str):
        return [x]
    return list(x)


def cmd(en: Optional[Union[str, Iterable[str]]] = None,
        ar: Optional[Union[str, Iterable[str]]] = None,
        prefixes: Iterable[str] = ("/", "!")):
    """
    Match either:
      * English-style commands with prefix (e.g. /ban, !ban)
      * Arabic words at the start of a message (no prefix, e.g. "حظر")

    Populates message.command = [trigger, *args] just like filters.command.
    """
    en_words = _as_list(en)
    ar_words = _as_list(ar)
    prefixes = tuple(prefixes)

    async def func(flt, _, message):
        text = message.text or message.caption
        if not text:
            return False
        text = text.strip()

        # English with prefix
        for word in en_words:
            for pref in prefixes:
                token = pref + word
                if text.startswith(token):
                    rest = text[len(token):]
                    # also accept @bot suffix: /ban@MyBot
                    if rest.startswith("@"):
                        sp = rest.find(" ")
                        rest = "" if sp == -1 else rest[sp:]
                    if rest == "" or rest[0] in (" ", "\n", "\t"):
                        args = rest.strip().split() if rest.strip() else []
                        message.command = [word] + args
                        return True

        # Arabic without prefix (whole word match)
        for word in ar_words:
            if text == word or text.startswith(word + " ") or text.startswith(word + "\n"):
                rest = text[len(word):]
                args = rest.strip().split() if rest.strip() else []
                message.command = [word] + args
                return True

        return False

    return filters.create(func)
