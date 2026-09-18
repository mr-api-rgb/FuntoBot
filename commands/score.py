from database.database import get_score


async def handle_score(bot, message):
    user_id = message.sender_id
    score = get_score(user_id)

    await bot.send_message(
        chat_id=message.chat_id,
        text=f"🏆 امتیاز شما: {score}"
    )


async def handle_my_score(bot, message):
    user_id = message.sender_id
    score = get_score(user_id)

    await bot.send_message(
        chat_id=message.chat_id,
        text=f"👤 امتیاز من\n\n🏆 امتیاز شما: {score}"
    )
