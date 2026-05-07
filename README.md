<div dir="rtl" align="center">

# 🤖 Wibot — بوت إدارة مجموعات تيليجرام (نسخة عربية)

بوت متكامل لإدارة مجموعات تيليجرام بأكثر من **50 موديول** بميزات قوية، **بواجهة وأوامر عربية** بالكامل + توافق مع الأوامر الإنجليزية.

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-Kurigram%202.2-orange)](https://github.com/KurimuzonAkuma/pyrogram)

</div>

---

## ✨ المميزات

- 🛡️ **إدارة كاملة** — حظر، طرد، كتم، تحذير، رفع/تنزيل، تثبيت، حذف رسائل، تطهير
- 👋 **ترحيب وكابتشا** — حماية المجموعة من البوتات وحسابات السبام
- 📜 **قوانين، ملاحظات، فلاتر** — احفظ ردوداً تلقائية ونظّم مجموعتك
- 🔒 **أقفال** — لقفل أنواع معيّنة من الرسائل (روابط، صور، استيكرات...)
- 🌊 **مكافحة الإغراق (Anti-flood)** — كتم/طرد/حظر تلقائي عند تجاوز الحد
- 🤝 **اتحادات (Federation)** — حظر مستخدم في عدة مجموعات دفعة واحدة
- 🎵 **موسيقى وملصقات** — تنزيل، اقتباسات (Quotly)، سرقة ملصقات
- 🔍 **معلومات** — معلومات المستخدم، فحص IP، عملات رقمية، ترجمة، RSS، Carbon
- 💬 **محادثة ذكية** — مدمجة مع AI
- ⚡ **أوامر عربية بدون شرطة** — اكتب `حظر` أو `طرد` مباشرة بدون `/`

## 📋 الأوامر العربية الأساسية

| الفئة | الأوامر |
|------|---------|
| الإدارة | `حظر`, `طرد`, `كتم`, `تحذير`, `رفع`, `تنزيل`, `تثبيت`, `تطهير`, `حذف` |
| فك القيود | `الغاء_حظر`, `الغاء_كتم`, `الغاء_تثبيت`, `مسح_التحذيرات` |
| المعلومات | `معلومات`, `الايدي`, `حي`, `بنق` |
| القوانين | `القوانين`, `ضع_قوانين`, `ملاحظات`, `احفظ`, `استرجع` |
| الترحيب | `ترحيب`, `وداع`, `كابتشا` |
| الفلاتر | `فلاتر`, `فلتر`, `قائمة_سوداء`, `قفل`, `فتح`, `الاقفال` |
| البدء | `بدء`, `مساعدة`, `اوامر` |

> أرسل `/help` أو `مساعدة` في الخاص للاطلاع على القائمة الكاملة لكل الـ50+ موديول.

---

## 🚀 طرق النشر

### الطريقة 1️⃣ — VPS (Ubuntu / Debian)

```bash
# 1) تثبيت المتطلبات
sudo apt update && sudo apt install -y python3.11 python3.11-venv git ffmpeg
git clone https://github.com/YOUR_USERNAME/Wibot.git
cd Wibot

# 2) بيئة افتراضية وتنصيب الحزم
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3) إعداد المتغيرات
cp sample_config.env config.env
nano config.env   # عدّل القيم

# 4) تشغيل
python -m wbb
```

لتشغيل دائم في الخلفية باستخدام `systemd`:

```bash
sudo nano /etc/systemd/system/wibot.service
```

```ini
[Unit]
Description=Wibot Telegram Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Wibot
ExecStart=/root/Wibot/venv/bin/python -m wbb
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now wibot
sudo systemctl status wibot
```

---

### الطريقة 2️⃣ — Docker

```bash
git clone https://github.com/YOUR_USERNAME/Wibot.git
cd Wibot
cp sample_config.env config.env
nano config.env

docker build -t wibot .
docker run -d --name wibot --restart=always wibot
```

أو باستخدام `docker-compose`:

```bash
docker-compose up -d
```

---

### الطريقة 3️⃣ — Railway / Render / Koyeb

1. اعمل **Fork** للمستودع على GitHub.
2. سجّل في [Railway](https://railway.app) (أو [Render](https://render.com) / [Koyeb](https://www.koyeb.com)).
3. اختر **New Project → Deploy from GitHub Repo**.
4. ضع متغيرات البيئة في تبويب **Variables**:
   - `BOT_TOKEN`
   - `API_ID`
   - `API_HASH`
   - `MONGO_URL`
   - `SUDO_USERS_ID`
   - `LOG_GROUP_ID`
   - `MESSAGE_DUMP_CHAT`
   - `GBAN_LOG_GROUP_ID`
5. النشر تلقائي. الملف `Procfile` يخبر المنصة كيف تشغّل البوت.

---

### الطريقة 4️⃣ — Heroku

```bash
heroku create my-wibot
heroku stack:set heroku-22
heroku config:set BOT_TOKEN=... API_ID=... API_HASH=... MONGO_URL=... SUDO_USERS_ID=... LOG_GROUP_ID=... MESSAGE_DUMP_CHAT=... GBAN_LOG_GROUP_ID=...
git push heroku main
heroku ps:scale worker=1
heroku logs --tail
```

---

## 🔑 الحصول على المفاتيح

| المفتاح | من أين تحصل عليه |
|---------|-----------------|
| `BOT_TOKEN` | [@BotFather](https://t.me/BotFather) |
| `API_ID` و `API_HASH` | [my.telegram.org](https://my.telegram.org) → API development tools |
| `MONGO_URL` | [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (مجاناً) |
| `SUDO_USERS_ID` | معرفك في تيليجرام (من [@MissRose_bot](https://t.me/MissRose_bot) → `/id`) |
| `LOG_GROUP_ID` | معرف مجموعة لسجلات البوت (-100...) |

> ⚠️ **مهم:** اجعل البوت **مشرفاً** في `LOG_GROUP_ID` و `MESSAGE_DUMP_CHAT` و `GBAN_LOG_GROUP_ID`.

### اختياري: Userbot (حساب شخصي بجانب البوت)

لتفعيل ميزات Userbot (مثل `purge_me`, بعض ميزات الموسيقى والملصقات):

```bash
pip install kurigram TgCrypto
python str_gen.py
```

ثم ضع `SESSION_STRING` في `config.env`. **لا تستخدم حسابك الأساسي** — استخدم رقم هاتف اختياري.

---

## 📁 هيكل المشروع

```
Wibot/
├── wbb/
│   ├── __init__.py          # تهيئة العميل
│   ├── __main__.py          # نقطة الدخول والـ /start, /help
│   ├── core/                # decorators وkeyboard وfilters
│   ├── modules/             # 50+ موديول للميزات
│   │   ├── admin.py
│   │   ├── greetings.py
│   │   ├── notes.py
│   │   └── ...
│   └── utils/
│       ├── acmd.py          # 🆕 فلتر الأوامر العربية
│       ├── dbfunctions.py
│       └── ...
├── sample_config.env        # نموذج للمتغيرات
├── sample_config.py         # محمّل المتغيرات
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Procfile
├── runtime.txt
└── README.md
```

---

## 🛠 إصلاحات تمت في هذه النسخة

هذه النسخة معدّلة من المستودع الأصلي [WilliamButcherBot](https://github.com/thehamkercat/WilliamButcherBot) مع إصلاحات حرجة:

- ✅ **أُنشئ ملف `wbb/modules/admin.py`** الذي كان مفقوداً ويسبب `ImportError` في 8 ملفات
- ✅ **إصلاح حلقة asyncio** في `wbb/__init__.py` و `wbb/__main__.py`
- ✅ **إصلاح مشكلة aiohttp ClientSession** التي تتطلب event loop running
- ✅ **دعم تشغيل بدون SESSION_STRING** (aliasing `app2 = app`)
- ✅ **إصلاح Dockerfile** (كان يعتمد على ملفات مفقودة)
- ✅ **`requirements.txt` نظيف وكامل** مع كل التبعيات
- ✅ **defaults آمنة** للمتغيرات (لا ينهار إذا كان متغيّر مفقوداً)
- ✅ **تعريب كامل** للـ`__HELP__` ولأسماء الموديولات
- ✅ **أوامر عربية** بدون شرطة `/` لأكثر من 70 أمراً
- ✅ **ترجمة الردود الشائعة** في الـ admin/greetings/sudoers/notes

---

## 📜 الترخيص

MIT License — انظر [LICENSE](LICENSE).

البوت الأصلي من [@TheHamkerCat](https://github.com/thehamkercat). التعديلات والتعريب: 2026.

---

<div dir="rtl" align="center">

**صنع بـ ❤️ — اضغط ⭐ إذا أعجبك المشروع**

</div>
