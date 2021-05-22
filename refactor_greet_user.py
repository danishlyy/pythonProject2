import json


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        json.dump(filename, file_object)
        print('we will remember you when you come back, ' + username + ' !')
    else:
        print('welcome back, ' + username)


greet_user()
