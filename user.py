class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('user_name: ' + self.last_name + " " + self.first_name)

    def greet_user(self):
        full_name = self.last_name + ' ' + self.first_name
        print('hello,' + full_name)


user = User('san', 'zhang')
user.describe_user()
user.greet_user()
