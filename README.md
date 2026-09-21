# 🎭 FuntoBot | ربات فانتو

> 🎉 An interactive entertainment bot for Rubika groups, featuring **1000+ Challenges, 1000+ Dares, 1000+ Truth Questions**, and a customizable learning system.

> 🤖 یک ربات سرگرمی و تعاملی برای گروه‌های روبیکا با **بیش از ۱۰۰۰ چالش، ۱۰۰۰ جرئت، ۱۰۰۰ سؤال حقیقت** و سیستم یادگیری پاسخ‌های اختصاصی.

---

## ✨ Features | قابلیت‌ها

* 🎯 Random Challenge Generator
* 😈 Random Dare Generator
* ❓ Random Truth Question Generator
* 🔥 1000+ Different Challenges
* 😈 1000+ Different Dares
* 🧠 1000+ Truth Questions
* 👋 Responses to common messages such as greetings and goodbyes
* 🧠 Interactive learning system
* 💬 Custom question & answer creation
* 💾 Persistent storage of learned responses
* 📚 `/یاد بگیر` command for teaching new responses
* 🎲 Random and varied content selection
* 👥 Designed for groups and gatherings
* ⚡ Fast command responses
* 🔄 Diverse and non-repetitive entertainment content

---

## 🧠 Learning System | سیستم یادگیری

One of FuntoBot's main features is its ability to learn custom responses.

Users can teach the bot a new question and answer using:

```text
/یاد بگیر "شغلت چیه" / "من شغلم جواب دادن به شماست 😂"
```

After learning, the bot stores the custom response and can use it when the corresponding question is received.

### Example

**User:**

```text
شغلت چیه؟
```

**FuntoBot:**

```text
من شغلم جواب دادن به شماست 😂
```

---

## 🎮 Entertainment Commands | دستورات سرگرمی

### Challenge

```text
چالش
```

Sends a random challenge.

### Dare

```text
جرئت
```

Sends a random dare.

### Truth

```text
حقیقت
```

Sends a random truth question.

### Learning

```text
/یاد بگیر
```

Teaches the bot a new custom question and answer.

---

## 📊 Content Database | بانک محتوا

FuntoBot includes a large collection of entertainment content:

| Content           | Amount |
| ----------------- | -----: |
| 🎯 Challenges     |  1000+ |
| 😈 Dares          |  1000+ |
| ❓ Truth Questions |  1000+ |

The bot randomly selects content to provide a more varied experience in groups.

---

## 💬 Interactive Responses | پاسخ‌گویی تعاملی

FuntoBot isn't limited to predefined commands.

It can also respond to common public messages such as:

```text
سلام
خداحافظ
```

Combined with its learning system, the bot can be customized with additional question-and-answer responses.

---

## 👥 Designed for Groups | مناسب گروه‌ها

FuntoBot is designed primarily for:

* 🎉 Friendly groups
* 👥 Group gatherings
* 🎮 Entertainment groups
* 😂 Friend communities
* 🔥 Truth-or-Dare games

Its random content system helps keep group interactions dynamic and entertaining.

---

## ⚡ Fast & Simple

FuntoBot is designed to provide quick responses to commands while keeping the interaction simple for users.

The main goal is to make starting a game or conversation in a Rubika group as easy as sending a command.

---

## 🛠️ Project Structure

A typical project structure can be organized like this:

```text
FuntoBot/
│
├── bot.py
├── commands/
│   ├── challenge.py
│   ├── dare.py
│   ├── truth.py
│   ├── help.py
│   └── learn.py
│
├── data/
│   ├── challenges.json
│   ├── dares.json
│   ├── truths.json
│   └── learned.json
│
└── README.md
```

---

## 🎯 Project Goal

The goal of FuntoBot is to provide a lightweight and interactive entertainment experience for Rubika groups.

With a large content database and a customizable learning system, administrators and users can make the bot more suitable for their own community.

---

## 🔐 Privacy & Data

Learned question-and-answer pairs may be stored by the bot so they can be used in future interactions.

Avoid teaching the bot sensitive, private, or personal information.

---

## 👨‍💻 Developer

**mr-api**

---

## 📜 License

This project can be distributed according to the license included in the repository.

---

# 🇮🇷 نسخه فارسی

## 🎭 فانتو | FuntoBot

**فانتو** یک ربات سرگرمی و تعاملی برای روبیکاست که برای استفاده در گروه‌ها و دورهمی‌ها طراحی شده است.

این ربات علاوه بر مجموعه بزرگی از **چالش‌ها، جرئت‌ها و سؤالات حقیقت**، دارای سیستم یادگیری است که به کاربران اجازه می‌دهد پاسخ‌های اختصاصی خودشان را به ربات آموزش دهند.

---

## ✨ قابلیت‌ها

* 🎯 ارسال چالش تصادفی
* 😈 ارسال جرئت تصادفی
* ❓ ارسال سؤال حقیقت تصادفی
* 🔥 بیش از ۱۰۰۰ چالش مختلف
* 😈 بیش از ۱۰۰۰ جرئت متفاوت
* 🧠 بیش از ۱۰۰۰ سؤال حقیقت
* 👋 پاسخ به پیام‌های عمومی مانند سلام و خداحافظی
* 🧠 سیستم یادگیری و آموزش پاسخ‌های جدید
* 💬 تعریف سؤال و جواب اختصاصی
* 💾 ذخیره پاسخ‌های آموزش‌داده‌شده
* 📚 دستور `/یاد بگیر`
* 🎲 انتخاب تصادفی و متنوع محتوا
* 👥 مناسب گروه‌ها و دورهمی‌ها
* ⚡ پاسخ سریع به دستورات
* 🔄 محتوای سرگرمی متنوع و غیرتکراری

---

## 🧠 سیستم یادگیری

یکی از قابلیت‌های اصلی فانتو، امکان آموزش پاسخ‌های جدید به ربات است.

برای مثال:

```text
/یاد بگیر "شغلت چیه" / "من شغلم جواب دادن به شماست 😂"
```

ربات سؤال و پاسخ مشخص‌شده را ذخیره می‌کند و در زمان مناسب از پاسخ آموزش‌داده‌شده استفاده می‌کند.

### مثال

**کاربر:**

```text
شغلت چیه؟
```

**فانتو:**

```text
من شغلم جواب دادن به شماست 😂
```

---

## 🎮 دستورات اصلی

### 🎯 چالش

```text
چالش
```

ارسال یک چالش تصادفی.

### 😈 جرئت

```text
جرئت
```

ارسال یک جرئت تصادفی.

### ❓ حقیقت

```text
حقیقت
```

ارسال یک سؤال حقیقت تصادفی.

### 🧠 یادگیری

```text
/یاد بگیر
```

آموزش یک سؤال و جواب جدید به ربات.

---

## 📊 بانک محتوای فانتو

| نوع محتوا | تعداد |
| --------- | ----: |
| 🎯 چالش   | ۱۰۰۰+ |
| 😈 جرئت   | ۱۰۰۰+ |
| ❓ حقیقت   | ۱۰۰۰+ |

محتوا به‌صورت تصادفی انتخاب می‌شود تا پاسخ‌ها متنوع‌تر باشند.

---

## 💬 پاسخ‌گویی تعاملی

فانتو فقط به دستورات مشخص محدود نیست.

ربات می‌تواند به پیام‌های عمومی مانند:

```text
سلام
خداحافظ
```

پاسخ دهد.

همچنین با استفاده از سیستم یادگیری، می‌توان پاسخ‌های اختصاصی بیشتری برای ربات تعریف کرد.

---

## 👥 مناسب برای گروه‌ها

فانتو برای موارد زیر طراحی شده است:

* 🎉 گروه‌های دوستانه
* 👥 دورهمی‌ها
* 🎮 گروه‌های سرگرمی
* 😂 جمع‌های دوستان
* 🔥 بازی‌های حقیقت و جرئت

---

## 🎯 هدف پروژه

هدف FuntoBot ایجاد یک تجربه سرگرم‌کننده و تعاملی برای کاربران روبیکاست.

ترکیب بانک محتوای بزرگ، انتخاب تصادفی و سیستم یادگیری باعث می‌شود ربات بتواند با توجه به فضای هر گروه شخصی‌سازی شود.

---

## 🔐 حریم خصوصی

پاسخ‌هایی که به ربات آموزش داده می‌شوند ممکن است برای استفاده در تعاملات بعدی ذخیره شوند.

از آموزش اطلاعات شخصی، محرمانه یا حساس به ربات خودداری کنید.

---

## 👨‍💻 توسعه‌دهنده

**mr-api**

---

## 📜 لایسنس

این پروژه مطابق لایسنس موجود در مخزن قابل استفاده و توسعه است.
