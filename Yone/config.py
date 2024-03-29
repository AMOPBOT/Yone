
import json
import os


def get_user_list(config, key):
    with open("{}/Yone/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True

    API_ID = "12227067"
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "1683925087:AAEKWjNEbZ8x68HotlPXCdTlakvShJPsCug"
    OWNER_ID = "2105971379"
    DEEP_API = "c8e3d7fc-1f7e-455b-8019-5c1b7f21047a"
    OPENAI_KEY = ""
    OWNER_USERNAME = "sultan11100"
    SUPPORT_CHAT = "Yone_Support"
    JOIN_LOGGER = "-1001841879487"
    EVENT_LOGS = "-1001908711819"
    BOT_USERNAME = "Yone_Robot"
    BOT_NAME = "Yone"
    MONGO_DB_URI = "mongodb+srv://YoneNewDB:tEMKfnQA8xHkmxtX@yonenewdb.jwnwd6g.mongodb.net/?retryWrites=true&w=majority"
    GBANS = list(map("5360305806 2105971379").split())
    # DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    DATABASE_URL = "postgres://yone:Kushal55@yone.cirqmtrbghab.us-east-1.rds.amazonaws.com:5432/yone"  # sql
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    REDIS_URL = "redis://default:725m47dhlmisA0QecURSMkcHNGXkM1uP@redis-15808.c275.us-east-1-4.ec2.cloud.redislabs.com:15808"

    INSPECTOR = get_user_list("elevated_users.json", "ins")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "req")

    CERT_PATH = None
    STRICT_GBAN = True
    PORT = "8080"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 20
    ALLOW_EXCL = True
    ALLOW_CHATS = True
    PHOTO = "https://graph.org/file/324a12454d23b5d78dd48.jpg" # Miss Poppy Music Pic
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
