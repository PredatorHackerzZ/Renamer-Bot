class Scripted(object):    


    PROGRESS_DIS = """\n
<b>📁 : {1} | {2}</b>\n
<b>🚀 : {0}%</b>\n
<b>⚡ : {3}/s</b>\n
<b>⏱️ : {4}</b>\n"""


    HELP_TEXT = """
<i>𝐖𝐚𝐭𝐜𝐡 𝐕𝐢𝐝𝐞𝐨 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐌𝐞 <a href='https://youtu.be/HnXdu74o34E'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></i>\n
<i>𝐒𝐞𝐧𝐝 𝐚 𝐩𝐡𝐨𝐭𝐨 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐚𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 (optional)</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 (or) 𝐌𝐞𝐝𝐢𝐚 𝐟𝐫𝐨𝐦 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦</i>\n
<i>𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧𝐭𝐨 𝐯𝐢𝐝𝐞𝐨 𝐮𝐬𝐞 /convert 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞.ext</i>\n
<i>𝐕𝐢𝐞𝐰 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /sthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>\n
<i>𝐃𝐞𝐥𝐞𝐭𝐞 𝐲𝐨𝐮𝐫 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐝𝐨 /dthumbnail 𝐜𝐨𝐦𝐦𝐚𝐧𝐝</i>"""


    ABOUT_TEXT = """
<b>🤖 𝐌𝐲 𝐍𝐚𝐦𝐞 : <a href='https://t.me/Renamer_teleroid_bot'>Rename X2 Bot</a></b>\n
<b>📢 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href='https://t.me/TeleRoidGroup'>TÉLÉRØÎD</a></b>\n
<b>👥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 𝐕𝟐 : <a href='https://t.me/TeleRoid_Renamer_bot'>0.9.2 beta</a></b>\n
<b>📥 𝐒𝐨𝐮𝐫𝐜𝐞 : <a href='https://github.com/P-Phreak/Renamer-bot'>Click Here</a></b>\n
<b>🌐 𝐒𝐞𝐫𝐯𝐞𝐫 : <a href='https://heroku.com'>Heroku</a></b>\n
<b>📕 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
<b>㊙ 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞  : <a href='https://www.python.org'>Python 3.9.4</a></b>\n
<b>👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='https://t.me/PredatorHackerzZ_bot'>꧁ ƤℜɆĐ₳₮Øℜ 🇮🇳 ꧂</a></b>\n
<b>📌 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : <a href='https://t.me/Moviesflixers_DL'>Tᴀᴍɪʟᴡᴇʙ Tɢ Nᴇᴛᴡᴏʀᴋ</a></b>\n"""


    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>¥ou 𝐀𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 🚫</b>"
    BANNED_USER_TEXT = "<i>¥ou 𝐀𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 🚫</i>"
    TRYING_TO_UPLOAD = "<i>𝐓𝐫𝐲𝐢𝐧𝐠 𝐭𝐨 𝐮𝐩𝐥𝐨𝐚𝐝....</i>"
    CURRENT_THUMBNAIL = "<i>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🎭</i>"
    THUMBNAIL_SAVED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 ✅</i>"
    THUMBNAIL_DELETED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ✅</i>"
    NO_THUMBNAIL_FOUND = "<i>𝐍𝐨 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝 (𝐊𝐨𝐧𝐬𝐢 𝐆𝐚𝐚𝐥𝐢 𝐂𝐡𝐚𝐡𝐢𝐲𝐞)😔</i>"
    TRYING_TO_DOWNLOAD = "<i>𝐓𝐫𝐲𝐢𝐧𝐠 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝....</i>"
    UPLOAD_SUCCESS = "<u><i>𝕿𝖍𝖆𝖓𝖐𝖘 𝖋𝖔𝖗 𝖚𝖘𝖎𝖓𝖌 𝖒𝖊𝖍 𝖇𝖔𝖙 ❤ @TheTeleRoid</i></u>"
    REPLY_TO_MEDIA = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐌𝐞𝐝𝐢𝐚 𝐰𝐢𝐭𝐡 /convert</i>"
    UPLOAD_START = "<i>📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    DOWNLOAD_START = "<i>📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    JOIN_NOW_TEXT = "<code>𝕱𝖎𝖗𝖘𝖙 𝕵𝖔𝖎𝖓 𝕸𝖞 𝖀𝖕𝖉𝖆𝖙𝖊𝖘 𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝕿𝖔 𝖀𝖘𝖊 𝕸𝖊𝖍</code>"
    REPLY_TO_FILE = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞 .𝐞𝐱𝐭</i>"
    CONTACT_MY_DEVELOPER = "<i>𝕾𝖔𝖒𝖊𝖙𝖍𝖎𝖓𝖌 𝖂𝖗𝖔𝖓𝖌 𝕮𝖔𝖓𝖙𝖆𝖈𝖙 𝕸𝖞 𝕯𝖊𝖛𝖊𝖑𝖔𝖕𝖊𝖗 🤯</i>"
    START_TEXT = "<i>𝕿𝖍𝖎𝖘 𝖎𝖘 𝖆 𝕾𝖎𝖒𝖕𝖑𝖊 𝖋𝖎𝖑𝖊 𝖗𝖊𝖓𝖆𝖒𝖊𝖗 & 𝕱𝖎𝖑𝖊 𝕮𝖔𝖓𝖛𝖊𝖗𝖙𝖊𝖗 𝖇𝖔𝖙 𝖜𝖎𝖙𝖍 𝖕𝖊𝖗𝖒𝖆𝖓𝖊𝖓𝖙 𝖙𝖍𝖚𝖒𝖇𝖓𝖆𝖎𝖑 𝖘𝖚𝖕𝖕𝖔𝖗𝖙 💯</i>"
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/TeleRoid14'>[ 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 ]</a></b>"
