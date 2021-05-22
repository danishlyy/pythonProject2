import json

filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    json.dump(username, file_object)
    print('we will remember you when you come back, ' + username + ' !')
else:
    print('welcome back, ' + username)
