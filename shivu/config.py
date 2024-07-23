class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1148001896"
    sudo_users = "6661148556", "6765826972"
    GROUP_ID = -1002210922945
    TOKEN = "6837013687:AAFvbZJG7lmfWtX3TF2wg4dzurr54Ou5e3I"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "suppendhsb"
    UPDATE_CHAT = "vycvnkubb"
    BOT_USERNAME = "Waifugraberobot"
    CHARA_CHANNEL_ID = "-1002219117680"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
