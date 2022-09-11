# class User :
#     def __init__(self) :
#         print("New user being created...")

# user_1 = User()
# user_1.id = "000"
# user_1.username = "Alex"

# user_2 = User()
# user_2.id = "001"
# user_2.username = "Alexis"

# print(user_2.username)


# class Car :
#     def __init__(self,seats) :
#         self.seats = seats

# my_car = Car(5)
# print(my_car.seats)


# class User :
#     def __init__(self,user_id,username) :
#         self.id = user_id
#         self.username = username
#         self.followers = 0
# user_1 = User("001","Alex")

# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)


class User : 
    def __init__(self, user_id, username) :
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user) :
        user.followers += 1
        self.following += 1


user_1 = User("001","Alex")
user_2 = User("002","Jane")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)