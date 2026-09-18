from rubka import Robot, Message

from commands.challenge import handle_challenge
from commands.dare import handle_dare
from commands.truth import handle_truth
from commands.help import handle_help
from commands.score import handle_score, handle_my_score
from commands.rank import handle_rank
from commands.group import handle_activate, handle_deactivate

from config.phanto import get_phanto_response
from config.group_status import is_group_active


TOKEN = "TOKEN"

bot = Robot(token=TOKEN)


@bot.on_message_group()
async def handle_message(bot: Robot, message: Message):

    text = (message.text or "").strip()

    # فعال‌سازی گروه
    if text == "/فعال":
        await handle_activate(bot, message)
        return

    # غیرفعال‌سازی گروه
    if text == "/غیرفعال":
        await handle_deactivate(bot, message)
        return

    # اگر گروه فعال نیست، هیچ دستوری اجرا نشود
    if not is_group_active(message.chat_id):
        return

    # فانتو
    if text == "/فانتو":
        await bot.send_message(
            chat_id=message.chat_id,
            text=get_phanto_response()
        )

    # چالش
    elif text == "/چالش":
        await handle_challenge(bot, message)

    # جرئت
    elif text == "/جرئت":
        await handle_dare(bot, message)

    # حقیقت
    elif text == "/حقیقت":
        await handle_truth(bot, message)

    # راهنما
    elif text == "/راهنما":
        await handle_help(bot, message)

    # امتیاز
    elif text == "/امتیاز":
        await handle_score(bot, message)

    # امتیاز من
    elif text == "/امتیاز من":
        await handle_my_score(bot, message)

    # رتبه‌بندی
    elif text == "/رتبه":
        await handle_rank(bot, message)


bot.run()
