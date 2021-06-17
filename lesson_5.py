# If statements
alien_colour = "green"
if alien_colour == "green":
    print("You have just earned 5 points.")
alien_colour = "red"
if alien_colour == "green":
    print("You have just earned 5 points.")


# Else statements
alien_colour = "yellow"
if alien_colour == "yellow":
    print("You have just earned 5 points.")
else:
    print("You have just earned 10 points.")
alien_colour = "blue"
if alien_colour == "green":
    print("You have just earned 5 points.")
else:
    print("You have just earned 10 points.")


# Elif statements
alien_colour = "green"
if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")
alien_colour = "yellow"
if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")
alien_colour = "red"
if alien_colour == "green":
    print("You have just earned 5 points.")
elif alien_colour == "yellow":
    print("You have just earned 10 points.")
elif alien_colour == "red":
    print("You have just earned 15 points.")

age = 14
if age < 2:
    print("The person is a baby.")
elif 2 < age < 4:
    print("The person is a toddler.")
elif 4 < age < 13:
    print("The person is a kid.")
elif 13 < age < 20:
    print("The person is a teenager.")
elif 20 < age < 65:
    print("The person is an adult.")
elif 65 < age:
    print("The person is an elder.")

favourite_fruits = ["Strawberries", "Kiwis", "Cherries"]
if "Strawberries" in favourite_fruits:
    print("You really like strawberries!")
if "Kiwis" in favourite_fruits:
    print("You really like kiwis!")
if "Cherries" in favourite_fruits:
    print("You really like cherries!")

# Adding lists
usernames = ["Admin", "cHolk", "Slake", "Kamaji", "Christine"]
for username in usernames:
    if username == "Admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")
if usernames:
    print("There are users here!")
else:
    print("There are no users in here!")

current_users = ["Admin", "cHolk", "Slake", "Kamaji", "Christine"]
new_users = ["cHolk", "Christine", "Erin", "Michelle", "Kaylee"]
for new_user in new_users:
        if new_user in current_users:
            print(new_user + " is taken.")
        else:
            print(new_user + " is avaliable.")

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    if number == 2:
        print(str(number) + "nd")
    if number == 3:
        print(str(number) + "rd")
    if number in range(4, 10):
        print(str(number) + "th")