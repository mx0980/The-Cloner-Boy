from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQEMD9UAZKqab-z8iQ1XSSKX4JFb7AdYn_ZgJzzXULqO2Y-biykypfCkEoXlmmuDg59JvtqBbTSt7zlltA0DU_qEgVc6c2PxePWm7wjmMK1UqPZw-QM4lQCDOtHqNYwRegUkinM8tA2897UPkicXIwfSOKmeEpTgdbbF3qnaoBWYjuVOXzSMoLiOWPYjAHVCTQW2e4okiggKw8P0YkHiKWp2iCIPeJoOBjBieOVK3h1oVnya89VxcOPVLNISV1h1iayj1NmE4VMcX-DAFhLHWbrDUpxRZ03BZBdS5GPBC_xCRSTnXEaCHgADOZo-pIz8zj2cTtKiJAfpiegbOwtojITj6_VtlQAAAAE9gIqFAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
