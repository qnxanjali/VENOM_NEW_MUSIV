from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("🥂 ᴄʜᴀᴛɢᴘᴛ 🥂", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("❄️ ᴛᴧɢ-ᴧʟʟ ❄️", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("✨ ɪɴғᴏ ✨", callback_data="mplus HELP_Info"),InlineKeyboardButton("Exᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("🕯️️ ɪᴍᴧɢᴇ 🕯️", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("🎏 ᴧᴄᴛɪᴏɴ 🎏", callback_data="mplus HELP_Action"),InlineKeyboardButton("Sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("🫧 ғᴏɴᴛ 🫧", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("🔖 ɢᴀᴍᴇs 🔖", callback_data="mplus HELP_Game"),InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("🎐 ɪᴍᴘᴏsᴛᴇʀ 🎐", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("🍹 ᴛʀᴜᴛʜ-ᴅᴀʀᴇ 🍹", callback_data="mplus HELP_TD"),InlineKeyboardButton("ʜᴀsᴛᴀɢ", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("🍡 ᴛᴛs 🍡", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("🍥 ғᴜɴ 🍥", callback_data="mplus HELP_Fun"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<🔘", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("🔘>", callback_data=f"managebot123 settings_back_helper"),
    ]]
