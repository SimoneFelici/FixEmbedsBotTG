import re
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "BOT_TOKEN"

def convert_links(text):

    # Instagram
    text = re.sub(r'https?://(www\.)?instagram\.com', r'https://ddinstagram.com', text)

    # Twitter
    text = re.sub(r'https?://(www\.)?x\.com', r'https://fixupx.com', text)
    text = re.sub(r'https?://(www\.)?twitter\.com', r'https://fxtwitter.com', text)

    # TikTok
    text = re.sub(r'https?://(www\.)?tiktok\.com', r'https://d.tnktok.com', text)

    return text

async def link_converter(update, context):
    original_text = update.message.text
    converted_text = convert_links(original_text)
    if original_text != converted_text:
        await update.message.reply_text(converted_text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (filters.Entity('url') | filters.Entity('text_link')), link_converter))
app.run_polling()
