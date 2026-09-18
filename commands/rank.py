from database.database import get_top_users


async def handle_rank(bot, message):
    users = get_top_users(10)

    if not users:
        await bot.send_message(
            chat_id=message.chat_id,
            text="🏆 هنوز هیچ امتیازی ثبت نشده است."
        )
        return

    text = "🏆 رتبه‌بندی کاربران\n\n"

    medals = ["🥇", "🥈", "🥉"]

    for index, user in enumerate(users, start=1):
        user_id, name, score = user

        if index <= 3:
            medal = medals[index - 1]
        else:
            medal = f"{index}."

        text += f"{medal} {name} — {score} امتیاز\n"

    await bot.send_message(
        chat_id=message.chat_id,
        text=text
    )
