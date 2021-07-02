# Using classes
class Restauraunt():
    def __init__(self, restauraunt_name, cuisine_type):
        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("This restaurant is called " + self.restauraunt_name + " and it serves " + self.cuisine_type + " food.")
    def open_restaurant(self):
        print(self.restauraunt_name + " is now open.")
restaurant_1 = Restauraunt("Chipotle", "Mexican")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restauraunt("Sushi Nori", "Japanese")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restauraunt("Subway", "American")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()

class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is " + str(self.age) + " years old and they live in " + self.location)
    def greet_user(self):
        print("Hello " + self.first_name + ", how is the weather in " + self.location)
person_1 = User("Kassidy", "Jenkins", "30", "Illinois")
person_1.describe_user()
person_1.greet_user()

# Updating Classes
class Restauraunt():
    def __init__(self, restauraunt_name, cuisine_type):
        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("This restaurant is called " + self.restauraunt_name + " and it serves " + self.cuisine_type + " food.")
    def open_restaurant(self):
        print(self.restauraunt_name + " is now open.")
    def amount_served(self):
        print("We have served " + str(self.number_served) + " customers.")
    def increment_numbers(self, served):
        self.number_served += served
restaurant_1 = Restauraunt("Chipotle", "Mexican")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.number_served = 9
restaurant_1.amount_served()
restaurant_1.increment_numbers(100)
restaurant_1.amount_served()

class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is " + str(self.age) + " years old and they live in " + self.location)
    def greet_user(self):
        print("Hello " + self.first_name + ", how is the weather in " + self.location)
    def attempts(self):
        print("You have " + str(self.login_attempts) + " login attempts.")
    def increment_attempts(self):
        self.login_attempts += 1
        print("You have " + str(self.login_attempts) + " login attempts.")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Your login attempts have been set to " + str(self.login_attempts))
person_1 = User("Kassidy", "Jenkins", "30", "Illinois")
person_1.describe_user()
person_1.greet_user()
person_1.attempts()
person_1.increment_attempts()
person_1.increment_attempts()
person_1.increment_attempts()
person_1.increment_attempts()
person_1.increment_attempts()
person_1.reset_login_attempts()

# Inheritance
class IceCreamStand(Restauraunt):
    def __init__(self, restauraunt_name, cuisine_type):
        super().__init__(restauraunt_name, cuisine_type)
        self.icecream_flavours = ["strawberry", "chocolate", "vanilla"]
    def flavours(self):
        for flavour in self.icecream_flavours:
            print("We serve " + flavour + " ice cream here.")
user = IceCreamStand("Marble Stone", "ice cream")
user.open_restaurant()
user.describe_restaurant()
user.flavours()

class Privileges():
    def __init__(self):
        self.priviliges = ["can add posts", "can delete posts", "can ban users"]
    def show_privileges(self):
        for privilege in self.priviliges:
            print("Admins " + privilege)
            
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()  
user = Admin("Nicole", "Zhang", "14", "Vancouver")
user.describe_user()
user.greet_user()
user.privileges.show_privileges()

