from pyrogram import filters
from pyrogram.types import Message

from wbb import SUDOERS, USERBOT_PREFIX, app, app2

__MODULE__ = "النرد"
__HELP__ = """/dice - رمي نرد.
/dart - رمي سهم.
/basket - رمي كرة سلة.
/foot - رمي كرة قدم.
/bowl - رمي بولينغ.
/slot - تشغيل مكنة الحظ.
🔸 العربية: نرد، سهم، سلة، كرة، بولينغ، حظ"""


@app2.on_message(
    filters.command("dice", prefixes=USERBOT_PREFIX)
    & SUDOERS
    & ~filters.forwarded
    & ~filters.via_bot
)
@app.on_message(filters.command("dice"))
async def throw_dice(client, message: Message):
    six = (message.from_user.id in SUDOERS) if message.from_user else False

    c = message.chat.id
    if not six:
        return await client.send_dice(c, "🎲")

    m = await client.send_dice(c, "🎲")

    while m.dice.value != 6:
        await m.delete()
        m = await client.send_dice(c, "🎲")


