from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help

def progress(current, total):
    print(f"{current * 100 / total:.1f}%")
    
@UserBot.on_message((filters.video | filters.animation) & ~filters.edited & filters.me )
async def anime(_, message: Message):
    if message.chat.id == -586987941:
        await message.reply("Iniciando descarga...")
        try:
            await UserBot.download_media(message, progress = progress)
            await message.reply("Video descargado...")
            await message.delete()
        except:
            message.reply("Ha habido algun error al descargar este video. Avisa a @soukron.")
