from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8784080562:AAHl_WzqPuPCznZUPYLQFF2Qypxul_7-YLg"
CHAT_ID = -1003732081764

async def handle_edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.edited_message

    if not msg:
        return

    if msg.chat.id != CHAT_ID:
        return

    try:
        await context.bot.delete_message(
            chat_id=msg.chat.id,
            message_id=msg.message_id
        )
    except:
        pass

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, handle_edit))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
