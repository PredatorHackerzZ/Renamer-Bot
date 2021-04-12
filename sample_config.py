import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))
    
    API_HASH = os.environ.get("API_HASH")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600
    
    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DB_URI = os.environ.get("DATABASE_URL", "")

    UPDATE_GROUP = os.environ.get("UPDATE_GROUP", "")
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
