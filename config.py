import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "20445873"))
API_HASH = os.environ.get("API_HASH", "057fd0be9d7c38526b143c582bceb24b")


OWNER_ID = int(os.environ.get("OWNER_ID", "5543390445"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://mitsuha:mitsuha@cluster0.7zztr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002521004548"))     #DB of Hellsing [Aqua] [Killua DB]

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002416627674"))  #Anime_Harvest

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", "-1002183861154"))   #PVT channel of Anime Harvest


REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "-1002359112533"))   #Backup Channel of Anime Harvest [Manga Campus Backup channel]



START_PIC = os.environ.get("START_PIC", "https://imgfoto.host/i/CZre5l")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://imgfoto.host/i/CZrUjk")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8040")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[5543390445]
    for x in (os.environ.get("ADMINS", "5543390445 6975428639 7827086839 5891177226 5164955785").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")



CUSTOM_CAPTION = os.environ.get("", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<blockquote>𝗗𝗼𝗻'𝘁 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗱𝗶𝗿𝗲𝗰𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝗱𝗺, 𝗱𝗼 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝗮 𝗱𝗲𝗮𝘁𝗵 𝘄𝗶𝘀𝗵?</blockquote>"

START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>Moshi Moshi Senpai {mention}</b></blockquote>\n\n<b>I'm Killua Zoldyck a Filestore bot of @Anime_Harvest,</b>\n\n<blockquote><i>Not killing people is really hard. Clean living is tough.</i></blockquote>\n\n<u><i>I can bring all animes for you</i></u>\n\n<b><a href=https://t.me/Manga_Campus>━━━━━━━━━━ 「 𝗠𝗮𝗻𝗴𝗮 𝗖𝗮𝗺𝗽𝘂𝘀 」 ━━━━━━━━━</a></b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ Sᴇɴᴘᴀɪ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Fɪʟᴇs</b>")




ADMINS.append(OWNER_ID)
ADMINS.append(5543390445)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href='https://t.me/KILLUA_REBOT'>Killua Zoldyck 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Manga_Campus'>Manga_Campus</a>

    
<b>😈 Bot Made By :</b> @Aaru_2074"""
