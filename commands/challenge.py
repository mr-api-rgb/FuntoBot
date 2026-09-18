
import random

from data.challenges import CHALLENGES
from database.database import add_score


async def handle_challenge(bot, message):
    challenge = random.choice(CHALLENGES)

    user_id = message.sender_id
    name = getattr(message, "sender_name", None) or "کاربر"

    add_score(user_id, name, 2)

    await bot.send_message(
        chat_id=message.chat_id,
        text=f"🎯 چالش:\n\n{challenge}\n\n🏆 +2 امتیاز"
    )
