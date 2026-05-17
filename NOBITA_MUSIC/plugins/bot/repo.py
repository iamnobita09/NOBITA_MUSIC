from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NOBITA_MUSIC import app
from config import BOT_USERNAME
from NOBITA_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @II_NOBITA_DEFAULTERS_II ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/+S0Q1-J_EQLA3YmU1"),
          InlineKeyboardButton("𝚴 𝐎 𝐁 𝚰 𝐓 𝚲", url="https://t.me/II_NOBITA_DEFAULTERS_II"),
          ],
               [
                InlineKeyboardButton("˹ɴᴏʙɪᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/NOBITA_SUPP0RT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/NobitaMusiccRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
