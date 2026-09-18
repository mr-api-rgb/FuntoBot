
import random

from data.dares import DARES
from database.database import add_score


async def handle_dare(bot, message):
    dare = random.choice(DARES)

    user_id = message.sender_id
    name = getattr(message, "sender_name", None) or "کاربر"

    add_score(user_id, name, 3)

    await bot.send_message(
        chat_id=message.chat_id,
        text=f"🔥 جرئت:\n\n{dare}\n\n🏆 +3 امتیاز"
    )
