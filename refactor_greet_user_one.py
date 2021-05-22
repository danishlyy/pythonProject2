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


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = get_stored_username()
    except FileNotFoundError:
        json.dump(filename, file_object)
        print('we will remember you when you come back, ' + username + ' !')
    else:
        print('welcome back, ' + username)


greet_user()
