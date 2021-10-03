# (@) TeleRoidGroup| https://github.com/PredatorHackerzZ/RENAMER-BOT

# (©) @PredatorHackerzZ | @Clinton-Abraham / [ 28-12-2020] 5:10 PM

import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("WEBHOOK", False)):

    from sample_config import Config
else:
    from config import Config

from pyrogram import Client as Clinton


if __name__ == "__main__" :

    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = Clinton("Teleroid_Renamer_Bot", 
          bot_token=Config.TG_BOT_TOKEN, 
          api_id=Config.APP_ID,
          api_hash=Config.API_HASH,
          plugins=plugins
    )
    Config.AUTH_USERS.add(1287407305)
    app.run()
