import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input('what is your name')
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print('welcome back, ' + username)
    else:
        username = get_new_username()
        print('we will remember you when you come back, ' + username + ' !')


greet_user()
