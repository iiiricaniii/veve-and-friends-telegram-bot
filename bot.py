from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8784080562:AAHl_WzqPuPCznZUPYLQFF2Qypxul_7-YLg"
CHAT_ID = -1003732081764

async def delete_edited(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.edited_message

    if msg is None:
        return

    if msg.chat.id != CHAT_ID:
        return

    try:
        await context.bot.delete_message(
            chat_id=msg.chat.id,
            message_id=msg.message_id
        )
        print("Deleted edited message")

    except Exception as e:
        print("Error:", e)

def main():
    app = Application.builder().token(TOKEN).build()

    # IMPORTANT FIX: catch ALL updates, then filter manually
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, delete_edited))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
