import requests
from pyrogram import Client as Bot
from pyrogram import idle
from config import API_ID, API_HASH, BOT_TOKE


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

bot.start()
run() 
idle() 
