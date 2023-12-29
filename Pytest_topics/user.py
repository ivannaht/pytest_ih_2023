from Pytest_topics.users_excel import get_users


class User:

    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def show_user(self):
        return f"username: {self.username}, first_name: {self.first_name}, last_name: {self.last_name}"


user1 = User("sadmin", "Super", "Admin")
print(user1.show_user())

user_excel = get_users()[1]
user2 = User(user_excel['username'], user_excel['first_name'], user_excel['last_name'])
print(user2.show_user())