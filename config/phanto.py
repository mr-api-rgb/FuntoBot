import random


PHANTO_RESPONSES = [
    "👻 جانم؟",
    "👻 فانتو اینجاست!",
    "😎 بله؟ کاری داشتی؟",
    "👻 صدای من کردی؟",
    "😂 جان فانتو؟",
    "🔥 فانتو حاضر است!",
    "👀 بله، گوشم با توئه.",
    "😎بکن گاردی اینجاس",
    "😍جونم عشقم؟",
]


def get_phanto_response():
    return random.choice(PHANTO_RESPONSES)
