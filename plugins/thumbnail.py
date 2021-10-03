#https://github.com/PredatorHackerzZ/RENAMER-BOT

import os
import logging
import pyrogram
import database.database as sql

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from PIL import Image
from pyrogram import filters
from scripts import Scripted
from database.database import *
from pyrogram import Client as Clinton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Clinton.on_message(filters.photo)
async def save_photo(bot, update):
  
    if update.media_group_id is not None:
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + "/" + str(update.media_group_id) + "/"
        if not os.path.isdir(download_location):
            os.makedirs(download_location)
        await sql.df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
              message=update,
              file_name=download_location
        )
    else:
        # received single photo
        download_location = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
        await sql.df_thumb(update.from_user.id, update.message_id)
        await bot.download_media(
            message=update,
            file_name=download_location
        )
        await bot.send_message(
            chat_id=update.chat.id,
            text=Scripted.THUMBNAIL_SAVED,
            reply_to_message_id=update.message_id
        )


@Clinton.on_message(filters.private & filters.command(["sthumbnail"]))
async def show_thumb(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await bot.delete_messages(
              chat_id=update.chat.id,
              message_ids=update.message_id,
              revoke=True
        )
        return

    thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    if not os.path.exists(thumb_image_path):
        mes = await sthumb(update.from_user.id)
        if mes != None:
            m = await bot.get_messages(update.chat.id, mes.msg_id)
            await m.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None    
    
    if thumb_image_path is not None:
         await bot.send_photo(
               chat_id=update.chat.id,
               photo=thumb_image_path,
               caption=Scripted.CURRENT_THUMBNAIL,
               reply_to_message_id=update.message_id)

        
    elif thumb_image_path is None:
         await bot.send_message(
               chat_id=update.chat.id,
               text=Scripted.NO_THUMBNAIL_FOUND,
               reply_to_message_id=update.message_id)


@Clinton.on_message(filters.private & filters.command(["dthumbnail"]))
async def delete_thumbnail(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await bot.delete_messages(
              chat_id=update.chat.id,
              message_ids=update.message_id,
              revoke=True
        )
        return

    thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
    
    try:
        await sql.dthumb(update.from_user.id)
        os.remove(thumb_image_path)
    except:
        pass
    await bot.send_message(
          chat_id=update.chat.id,
          text=Scripted.THUMBNAIL_DELETED,
          reply_to_message_id=update.message_id)
