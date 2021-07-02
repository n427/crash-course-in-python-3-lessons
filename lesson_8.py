# Def functions
def display_message():
    print("The 'def' function defines a function for you to call later on")
display_message()

def favourite_books(book):
    print("One of my favourite books is " + book)
favourite_books("Alice In Wonderland")

# Multiple arguments
def make_shirt(size, message):
    print("The shirt will be a size " + size + " with the message: " + message)
make_shirt("small", "Hiiii~")

def make_shirt(size, message):
    print("The shirt will be a size " + size + " with the message: " + message)
make_shirt(size = "medium", message= "OwO")

def make_shirt(size, message = "I love python!"):
    print("The shirt will be a size " + size + " with the message: " + message)
make_shirt(size = "large")

def describe_city(city, country = "Canada"):
    print(city.title() + " is in " + country.title())
describe_city("Vancouver")
describe_city("Ottawa")
describe_city("Irvine", "America")

def city_country(city, country):
    print(city.title() + " " + country.title())
city_country("vancouver", "canada")

def make_album(name, album, tracks = " "):
    info = {"Name" : name, "Album Title" : album}
    if tracks != " ":
        info['tracks'] = tracks
    return info
Album = make_album(name = "Olivia Rodrigo", album = "Sour")
print(Album)
Album = make_album(name = "Olivia Rodrigo", album = "Sour", tracks = "7")
print(Album)

# Using break functions
def make_album(name, album):    
    info = {"Name" : name, "Album Title" : album}
    return info  
while True:
    print("Please tell me the album info \n Enter 'q' at any time to quit.")
    name = "Olivia Rodrigo" #input("What is the name of your artist?: \n")
    if name == "q":
        break
    album = "Sour" #input("What is the album name?: \n")
    if album == "q":
        break
    Album = make_album(name.title(), album.title())
    print(Album)
    break

# Using lists
def show_magicians(names):
    for name in names:
        print(name)
magician_names = ["Jenny", "Erin", "Michelle"]
show_magicians(magician_names)

def show_magicians(names):
    for name in names:
        print(name)
def make_great(names):
    for name in names:
        print("The great " + name)
magician_names = ["Jenny", "Erin", "Michelle"]
make_great(magician_names)

def sandwhich(*toppings):
    for topping in toppings:
        print("Adding " + topping+ " to your sandwhich")
sandwhich("Tomato", "Cucumber", "Bacon")

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Nicole', 'Zhang', location='Vancouver', field='Computer Science')
print(user_profile)

def make_car(manufacturer, model, **other_info):
    car = {}
    car["Manufacturer"] = manufacturer
    car["Model"] = model
    for key, value in other_info.items():
        car[key] = value
    return car
carsss = make_car("Kia", "Subaru", color = "White", leather = "Black")
print(carsss)

