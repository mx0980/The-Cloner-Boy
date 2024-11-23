from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQGVSWgAO8oMgWIy-dKBS1Mi1BNBwFGO2ZIHnnrpLsFbUCZTtOuCOyFooPChm1F2r5Fvk_HtywDMAQRsuyLWZzfdZowe-rVN4c0o_OHCeT-b9vuLuTLfZ1uAdH6r6tIQzafy5blEFCOBeljb7Uyftexs8cmJ967PhUyD0JYLXtnbJI6ZFAs0f4qDKzNt7VlCtBDXvq3fdoMNtxrSouvEjGWAh1sENEkwk2gIuau3yM6COTJl9BkSrosyLMSuaK9L69bJS6bbOP9i9FLkO3N9mwujiN9qIoIvQoo4KVLUtRjkkEmxedXRgflj1qhOr6_-N8xfiJcD-wbceb2ojvPg15a5PKgAxgAAAAGM3ZfRAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
