from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQEMD9UACuvyCI_Z0enjdgiBmYaKPCsqog5qMPkNAFYSbLJjh1LZWJykWCnxOWpDyI43b7KSaTLi6opKqUBRdxuDzJRE7OY6PXcgpR87PP-wva-mKjZ-CpXGqLJ1AqUgVUqjBdX8FA4l_2ixnubrWEYTz_HgJis4jNUrIOCjs6XqwxGwjF_GCIi7vRGBJhug4VDOYjJ1v1l0rloeKwCgMgNmSImKFBoXmqJRkLAWsV7RgIliNU-UCNQBSdmGDu-SIIxHCMQfeIjw1n6v8nrRkIgUJeTUI5fdafJShCP21jDxMoSggV_jD9-Z_-SPvVlRG4KsZHPi5Au62bz6OSSDu94cTJOU_wAAAAE9gIqFAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
