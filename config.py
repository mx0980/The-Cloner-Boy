from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQFRNDIAXv9EBv8drVlqMrHXaihM3yikM6P9LxjnElFcDvb3Df1xk5NHzQgV0zZhiQdzgRLdvgADyNXyovVNfcIhIXkNC1_y17E0zKyQch95s_W8JelP40z3VXa8szPEy4Qw29V_-P9xHtD_nEL02BpCcqwUbnofXJ-ycCJKuWqCpz83NxEjrsqtJIzJPirpiIc4Dakxwz8Xv93ZOArM2vmIYXauqZArLS-2hTCJJqI9RYSLBlHQa0At9N908M7ZwlNK95_VG-5WL5pbYzt3bcE3S_iUng_1LieMw-9CZ-Fg4jH40C9jI2fMFdXmxljcOajaaXrmadvuGsE9JwqWX0qhKVdxxAAAAAGeBZcgAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
