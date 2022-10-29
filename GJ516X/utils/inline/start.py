from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from GJ516X import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="╚»ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ«╝ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✧ʜᴇʟᴩ✧",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✧sᴇᴛᴛɪɴɢs✧", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✧ᴍᴀɪɴᴛᴀɪɴᴇʀ✧", user_id=OWNER),
            InlineKeyboardButton(
                text="✧sᴜᴩᴩᴏʀᴛ✧", url=f"https://t.me/+p2A5gHTe9_YzNDk1"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=" ╚»ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴩ❤️«╝ ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✧ʜᴇʟᴩ✧", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="✧ᴏᴡɴᴇʀ⚛✧", url=f"https://t.me/toxic_aadi28"),
        ],
        [ 
            InlineKeyboardButton(text="⚡ᴅᴇᴠᴇʟᴏᴩᴇʀ⚡", url=f"https://t.me/heartlessaryan_op"),
            InlineKeyboardButton(text="✧sᴜᴩᴩᴏʀᴛ✧", url=f"https://t.me/+p2A5gHTe9_YzNDk1"),
        ],
       
     ]
    return buttons
