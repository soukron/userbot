from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot, ALLOWED_USERS, ANIME_DOWNLOADS_DIR
from userbot.plugins.help import add_command_help
import sys
import json

def progress(current, total):
    print(f"{current * 100 / total:.1f}%")
    
@UserBot.on_message((filters.video | filters.animation) & ~filters.edited & (filters.me | filters.user(ALLOWED_USERS)) )
async def anime(_, message: Message):
    print(ANIME_DOWNLOADS_DIR + message.video.file_name)
    if message.chat.id == -586987941:
        await message.reply("Iniciando descarga del fichero %s..." % message.video.file_name)
        try:
            await UserBot.download_media(message, progress = progress, file_name = ANIME_DOWNLOADS_DIR + "/" + message.video.file_name)
            await message.reply("Video %s descargado..." % message.video.file_name)
            await message.delete()
        except:
            await message.reply("Ha habido algun error al descargar este video. Avisa a @soukron.")
