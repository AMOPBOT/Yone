
from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.enums import ChatAction
from pyrogram.types import InputMediaPhoto
from Yone import pbot as  yone
import requests
import time
from pyrogram.enums import ChatAction, ParseMode

BOT_USERNAME = "Yone_Robot"

@yone.on_message(filters.command("imagine"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    results= requests.get(f"https://mukesh-api.vercel.app/imagine/{text}").json()["results"]

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ Gᴇɴᴇʀᴀᴛᴇᴅ 💘
✨ **Gᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** @{BOT_USERNAME}
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
    await m.delete()
    photos=[]
    for i in range(5):
        photos.append(InputMediaPhoto(results[i]))
    photos.append(InputMediaPhoto(results[5], caption=caption))
    await b.send_media_group(message.chat.id, media=photos)



@yone.on_message(filters.command("mahadev"))
async def Mahadev(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO) 
        response = requests.get(f'https://mukesh-api.vercel.app/mahadev') 
        x=response.json()["results"]
            
        await message.reply_photo(photo=x,caption=f" \n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
        
@yone.on_message(filters.command("uselessfact"))
async def uselessa_fact(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING) 
        response = requests.get(f'https://mukesh-api.vercel.app/uselessfact') 
        x=response.json()["results"]
            
        await message.reply_text(x, parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

__mod_name__ = "Iᴍᴀɢɪɴᴇ"
__help__ = """
 ➻ /imagine : ɪᴍᴀɢᴇ ɢᴇɴᴇʀᴀᴛᴏʀ ᴀɪ
 ➻ /mahadev : ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
➻ /uselessfact :
 """
