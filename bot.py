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

from data.questions import (
    get_answer,
    add_question,
    parse_learn_command
)


# =========================
# TOKEN
# =========================

TOKEN = "YOUR_BOT_TOKEN"

bot = Robot(token=TOKEN)


# =========================
# GROUP MESSAGE HANDLER
# =========================

@bot.on_message_group()
async def handle_message(bot: Robot, message: Message):

    text = (message.text or "").strip()

    # =========================
    # فعال‌سازی گروه
    # =========================

    if text == "/فعال":
        await handle_activate(bot, message)
        return

    # =========================
    # غیرفعال‌سازی گروه
    # =========================

    if text == "/غیرفعال":
        await handle_deactivate(bot, message)
        return

    # =========================
    # اگر گروه فعال نیست
    # =========================

    if not is_group_active(message.chat_id):
        return

    # =========================
    # فانتو
    # =========================

    if text == "/فانتو":
        await bot.send_message(
            chat_id=message.chat_id,
            text=get_phanto_response()
        )
        return

    # =========================
    # چالش
    # =========================

    if text == "/چالش":
        await handle_challenge(bot, message)
        return

    # =========================
    # جرئت
    # =========================

    if text == "/جرئت":
        await handle_dare(bot, message)
        return

    # =========================
    # حقیقت
    # =========================

    if text == "/حقیقت":
        await handle_truth(bot, message)
        return

    # =========================
    # راهنما
    # =========================

    if text == "/راهنما":
        await handle_help(bot, message)
        return

    # =========================
    # امتیاز
    # =========================

    if text == "/امتیاز":
        await handle_score(bot, message)
        return

    # =========================
    # امتیاز من
    # =========================

    if text == "/امتیاز من":
        await handle_my_score(bot, message)
        return

    # =========================
    # رتبه‌بندی
    # =========================

    if text == "/رتبه":
        await handle_rank(bot, message)
        return

    # =========================
    # یاد گرفتن سؤال جدید
    # =========================

    if text.startswith("/یاد"):
        question, answer = parse_learn_command(text)

        if not question or not answer:
            await bot.send_message(
                chat_id=message.chat_id,
                text=(
                    "❌ فرمت اشتباه است.\n\n"
                    "فرمت درست:\n"
                    '/یاد بگیر "سوال" / "جواب"'
                )
            )
            return

        success, result = add_question(question, answer)

        if success:
            await bot.send_message(
                chat_id=message.chat_id,
                text=(
                    "✅ یاد گرفتم!\n\n"
                    f"❓ سوال: {question}\n"
                    f"💬 جواب: {answer}"
                )
            )
        else:
            await bot.send_message(
                chat_id=message.chat_id,
                text=f"❌ {result}"
            )

        return

    # =========================
    # پاسخ به سؤال‌های ذخیره‌شده
    # =========================

    if text.startswith("/"):
        question_text = text[1:].strip()

        answer = get_answer(question_text)

        if answer:
            await bot.send_message(
                chat_id=message.chat_id,
                text=answer
            )
            return


# =========================
# START BOT
# =========================

bot.run()
