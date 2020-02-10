import os 
def get_os_user_lower():
    username = os.getenv('USER')
    if username is None:
        raise OSError('USER enviroment is not set')
    return username.lower()

get_os_user_lower()
