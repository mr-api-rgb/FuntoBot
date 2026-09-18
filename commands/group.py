from config.group_status import activate_group, deactivate_group


async def handle_activate(bot, message):
    activate_group(message.chat_id)

    await bot.send_message(
        chat_id=message.chat_id,
        text="✅ ربات در این گروه فعال شد."
    )


async def handle_deactivate(bot, message):
    deactivate_group(message.chat_id)

    await bot.send_message(
        chat_id=message.chat_id,
        text="❌ ربات در این گروه غیرفعال شد."
    )
