from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from GJ516X import app
from GJ516X.core.call import GJ516
from GJ516X.utils import bot_sys_stats
from GJ516X.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
       caption=" Pinging...⚡ ",

    )

    await aditi.edit_text(

        f"""<b> pong ping ! ⚡</b>\n  🏓 {resp} ms\n\n<b><u>{BOT_NAME} system stats:</u></b>\n\n✨ Uptime : {bot_uptime}\n🔮 Cpu : {cpu}%\n💫 Disk : {disk}%\n❤️ Ram : {mem}\n\nᴍᴀᴅᴇ 🖤 ʙʏ [🕊️★ Aryan ★🇮🇳⃝🕊️](https://t.me/heartlessaryan_op)""",

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        "📨 Support ", url=f"https://t.me/+p2A5gHTe9_YzNDk1"

                    ),

                    InlineKeyboardButton(

                        "📨 owner ", url=f"https://t.me/Toxic_aadi28"

                    ),

                ],

                [

                    InlineKeyboardButton(

                        "💡Developer ", url="https://t.me/Heartlessaryan_op"

                    )

                ]

            ]

        ),

    )


