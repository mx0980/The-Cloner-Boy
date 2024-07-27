from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQEMD9UAqDNSm-5mLHtmzttMg6-QiNr34DFHs-eHy_Ldld-PkrtaQtM0DHp8gTKYIUHy2fYrrp1AzzFdQ1PcH8bdxo7-nVRPJOhDmQWSoA0G0tHAOOKHB_5ktgg3R2yfE5XqKy0f24e7hyP-WsJxGJBz4JiYIIVgZesLrcl9eqy5fpRINpO2chqoMePZx7Er2txJbDO0JWnNOJKevY69Z9cNofQBrF_tEUnUbwAh36LhEn5ghUntjmi_48xLD6ODvTSj3TQMClYpeTv4cgN2plAGTb9bfnJT99k-9sQ8lfZypvmPW5AeiGZSURa5uKJ0ZwFUNfJGTE2AuyddX9Q6eXGcCpbu_wAAAAE9gIqFAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
