#https://github.com/PredatorHackerzZ/RENAMER-BOT

import os
import time
import random
import logging
import pyrogram

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
from pyrogram import Client as Clinton
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from functions.nekmo_ffmpeg import take_screen_shot
from functions.display_progress import progress_for_pyrogram
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Clinton.on_message(filters.command(["convert"]))
async def convert(bot, update):

    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(Scripted.ACCESS_DENIED)
               return
        except UserNotParticipant:
            await update.reply_text(text=Scripted.JOIN_NOW_TEXT,
                  reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="📢 ᴊᴏɪɴ ɴᴏᴡ ", url=f"https://t.me/{Config.UPDATE_CHANNEL}") ]
                ] 
              )
            )
            return
        except Exception:
            await update.reply_text(Scripted.CONTACT_MY_DEVELOPER)
            return

    if update.reply_to_message is not None:
        description = Scripted.CUSTOM_CAPTION
        download_location = Config.DOWNLOAD_LOCATION + "/"
        c = await bot.send_message(
            chat_id=update.chat.id,
            text=Scripted.TRYING_TO_DOWNLOAD,
            reply_to_message_id=update.message_id
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Scripted.DOWNLOAD_START,
                c,
                c_time
            )
        )
        if the_real_download_location is not None:
            await bot.edit_message_text(
                text=Scripted.TRYING_TO_UPLOAD,
                chat_id=update.chat.id,
                message_id=c.message_id
            )
            logger.info(the_real_download_location)
            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(the_real_download_location))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = await take_screen_shot(
                    the_real_download_location,
                    os.path.dirname(the_real_download_location),
                    random.randint(
                        0,
                        duration - 1
                    )
                )
            logger.info(thumb_image_path)
            metadata = extractMetadata(createParser(thumb_image_path))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
            Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
            img = Image.open(thumb_image_path)
            img.resize((90, height))
            img.save(thumb_image_path, "JPEG")
            c_time = time.time()
            await bot.send_video(
                chat_id=update.chat.id,
                video=the_real_download_location,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=True,
                thumb=thumb_image_path,
                reply_to_message_id=update.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    Scripted.UPLOAD_START,
                    c,
                    c_time
                )
            )
            try:
                os.remove(the_real_download_location)
                #os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                  text=Scripted.UPLOAD_SUCCESS,
                  chat_id=update.chat.id,
                  message_id=c.message_id
            )
            
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Scripted.REPLY_TO_MEDIA,
            reply_to_message_id=update.message_id)
