
import random

from data.truths import TRUTHS
from database.database import add_score


async def handle_truth(bot, message):
    truth = random.choice(TRUTHS)

    user_id = message.sender_id
    name = getattr(message, "sender_name", None) or "کاربر"

    add_score(user_id, name, 3)

    await bot.send_message(
        chat_id=message.chat_id,
        text=f"🧠 حقیقت:\n\n{truth}\n\n🏆 +3 امتیاز"
    )
