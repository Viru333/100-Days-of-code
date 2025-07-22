class User: # PascalCase
    # initialize or create starting values of attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "aman")

# user_1.id = "001"
# user_1.username = "aman"
#
print(user_1.username)
print(user_1.id)
user_1.follower = 1
print(user_1.follower)
user_2 = User("002","angela")
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.following)
print(user_2.follower)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "angela"

