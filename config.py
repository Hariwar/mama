import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "17822592")
API_HASH = os.environ.get("API_HASH", "a20b3dbbe07ed695563b4609a3e62012")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7694688386:AAEyyOnqVujrBBi12eE6THWmhS8C9GG_tRw")
ADMIN = int(os.environ.get("ADMIN", '7835575911'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "mtpmasala")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "mtpmasala")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://temaga6324:rolex143@cluster0.hinoe.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002397670865')
GROUP = int(group) if group and id_pattern.search(group) else None
SUNRISES_PIC= "https://telegra.ph/file/0151dc084b62cb01b209d.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '7835575911'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", "-1002326958626")
