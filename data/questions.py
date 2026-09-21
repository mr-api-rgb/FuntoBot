import json
import os
import re
import random

QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions.json")


DEFAULT_QUESTIONS = {
    "سلام": [
        "سلام 👋",
        "سلام رفیق 😎",
        "درود 👻",
    ],

    "خوبی": [
        "آره، خوبم 😎",
        "خوبم، تو چطوری؟ 👀",
        "فانتو همیشه خوبه 👻",
    ],

    "چه خبر": [
        "خبر خاصی نیست، تو بگو 😎",
        "همه‌چی آرومه 👀",
        "منتظرم یکی یه چیز جالب بگه 😂",
    ],

    "کص کش": [
        "خودتی 😂",
        "ادب داشته باش رفیق 😐😂",
        "چه شروع گرمی داشتیم 😂",
    ],

    "خراب": [
        "خودت خراب‌تری 😂",
        "خراب ولی سرپا 😎",
        "خرابی از اینجا شروع شد 😂",
    ],

    "پدر محله ای": [
        "نه بابا، من پدر کل گروهم 😎",
        "پدر محله خودتی 😂",
    ],

    "مرگ موش بگیره عمت": [
        "آروم‌تر رفیق 😂",
        "این دیگه از کجا اومد؟ 😂",
    ],

    "خاله خراب": [
        "خودت خراب نکن بحثو 😂",
        "😂 باشه رفیق",
    ],

    "کونی زاده": [
        "😂 چه ادبیات گرمی",
        "آروم باش پهلوان 😐😂",
    ],

    "ننه قاشقی": [
        "قاشق رو از کجا آوردی؟ 😂",
        "این یکی دیگه خیلی خاص بود 😂",
    ],

    "قاشق زاده": [
        "قاشق‌زاده در خدمت شماست 😂",
        "ظرف هم با خودت آوردی؟ 😂",
    ],

    "کص ننه": [
        "😂 بیا یه کم آروم‌تر",
        "فانتو شاهد این مکالمه‌ست 👻",
    ],

    "توله سگ": [
        "خودت توله‌ای 😂",
        "هاپ هاپ 🐶😂",
    ],

    "بیشرف": [
        "بی‌شرف خودتی 😂",
        "من که کاری نکردم 😐😂",
    ],

    "کص صورتی": [
        "😂 این دیگه چه ترکیبی بود؟",
        "فانتو هنگ کرد 👻😂",
    ],

    "جنده": [
        "😂 چه ادبیاتی",
        "آروم رفیق 😐",
    ],

    "هرزه": [
        "خودت شروع کردی 😂",
        "😂 باشه پهلوان",
    ],

    "قهوه": [
        "قهوه؟ الان یکی لازم دارم ☕😂",
        "تلخ یا شیرین؟ 👀",
        "قهوه همیشه جواب میده ☕😎",
    ],

    "ننه مشکی": [
        "😂 داستان این یکی چیه؟",
        "فانتو در جریان نیست 👻",
    ],

    "خداحافظ": [
        "خداحافظ رفیق 👋",
        "فعلاً 😎",
        "برو ولی برگرد 😂",
    ],

    "صبح بخیر": [
        "صبح بخیر رفیق ☀️",
        "صبح تو هم بخیر 😎",
    ],

    "شب بخیر": [
        "شب بخیر 🌙",
        "خواب‌های خوب ببینی 😴",
    ],

    "چطوری": [
        "خوبم، تو چطوری؟ 😎",
        "فعلاً که زنده‌ام 😂",
    ],

    "کجایی": [
        "همین‌جا توی گروه 👻",
        "یه جای نامعلوم بین صفر و یک 😂",
    ],

    "کی هستی": [
        "من فانتومم 👻",
        "همون رباتی که ولت نمی‌کنه 😂",
    ],

    "اسمت چیه": [
        "فانتو 😎",
        "اسمم فانتوعه 👻",
    ],

    "عاشقی": [
        "من فقط عاشق اینترنت پرسرعتم 😂",
        "فعلاً نه 😎",
    ],

    "تنهایی": [
        "نه، شماها هستید دیگه 👻",
        "تنهایی برای فانتو معنی نداره 😂",
    ],

    "حوصله ندارم": [
        "یه /جرئت بزن شاید حالت عوض شد 😎",
        "پس وقتشه یه /چالش بزنی 😂",
    ],

    "حوصلم سر رفته": [
        "یه /چالش بزن 😈",
        "یه /جرئت بگیر 😂",
    ],

    "بخند": [
        "😂😂😂",
        "هاهاهاها 😂",
        "فانتو خندید 👻😂",
    ],

    "فانتو": [
        "جانم؟ 👻",
        "بله رفیق؟ 😎",
        "فانتو اینجاست 😂",
    ],

    "فانتو خوبی": [
        "وقتی شماها هستید آره 😂",
        "عالی‌ام 👻",
    ],

    "فانتو کجایی": [
        "همین‌جا بالای سرت 👻",
        "توی همین گروه 😎",
    ],

    "ربات": [
        "بله؟ 🤖",
        "رباتم ولی حواسم بهت هست 😂",
    ],

    "خفه": [
        "باشه 😐😂",
        "چشم، ساکت شدم 🤐",
    ],

    "ساکت": [
        "🤐",
        "چشم رئیس 😂",
    ],

    "دمت گرم": [
        "قربونت 😎🔥",
        "دمت گرم خودت 😂",
    ],

    "مرسی": [
        "خواهش می‌کنم 👻",
        "قابلی نداشت 😎",
    ],

    "ممنون": [
        "خواهش می‌کنم ❤️",
        "قربونت 😎",
    ],
}


def normalize(text):
    text = (text or "").strip()

    text = text.replace("ي", "ی")
    text = text.replace("ى", "ی")
    text = text.replace("ك", "ک")
    text = text.replace("\u200c", " ")

    text = re.sub(r"\s+", " ", text)

    text = re.sub(r"[؟?!]+$", "", text)

    return text.strip().lower()


def save_questions(data):
    with open(QUESTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_questions():
    if not os.path.exists(QUESTIONS_FILE):
        data = {}

        for question, answers in DEFAULT_QUESTIONS.items():
            data[normalize(question)] = answers

        save_questions(data)
        return data

    try:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            return {}

        return data

    except Exception:
        return {}


def get_answer(question):
    question = normalize(question)

    data = load_questions()

    answers = data.get(question)

    if not answers:
        return None

    if isinstance(answers, list):
        return random.choice(answers)

    return str(answers)


def add_question(question, answer):
    question = normalize(question)
    answer = answer.strip()

    if not question or not answer:
        return False, "سؤال یا جواب خالی است."

    data = load_questions()

    is_update = question in data

    if question not in data:
        data[question] = []

    if isinstance(data[question], str):
        data[question] = [data[question]]

    if answer not in data[question]:
        data[question].append(answer)

    save_questions(data)

    if is_update:
        return True, "به سؤال موجود یک جواب جدید اضافه شد."

    return True, "سؤال جدید ذخیره شد."


def parse_learn_command(text):
    pattern = r'^/یاد\s*بگیر\s*"(.+?)"\s*/\s*"(.+?)"\s*$'

    match = re.match(pattern, text.strip())

    if not match:
        return None, None

    question = match.group(1).strip()
    answer = match.group(2).strip()

    return question, answer
