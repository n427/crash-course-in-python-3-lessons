# Dictionaries
person = {"first_name" : "Nicole",
    "last_name" : "Zhang",
    "age" : "14",
    "city" : "North Vancouver"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

favourite_numbers = {"Nicole" : "14",
    "Kaylee" : "6",
    "Erin" : "25",
    "Michelle" : "72",
    "Christine" : "40"}
print(favourite_numbers["Nicole"])
print(favourite_numbers["Kaylee"])
print(favourite_numbers["Erin"])
print(favourite_numbers["Michelle"])
print(favourite_numbers["Christine"])

glossary = {"String" : "Words",
    "Loop" : "Repeated action",
    "Comments" : "Words that don't affect the code",
    "Dictionaries" : "Things that store values and meanings", 
    "List" : "Data"}
print("String: " + glossary["String"] + "\n")
print("Loop: " + glossary["Loop"] + "\n")
print("Comments: " + glossary["Comments"] + "\n")
print("Dictionaries: " + glossary["Dictionaries"] + "\n")
print("List: " + glossary["List"] + "\n")


# Looping through dictionaries
glossary = {"String" : "Words",
    "Loop" : "Repeated action",
    "Comments" : "Words that don't affect the code",
    "Dictionaries" : "Things that store values and meanings", 
    "List" : "Data"}
for word in glossary:
    print(word + ": " + glossary[word] + "\n")

rivers = {"egypt" : "nile",
    "south america" : "amazon",
    "china" : "yangtze"}
for place in rivers:
    print("The " + rivers[place].title() + " river is located in " + place.title())

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }
people = ["jen", "sarah", "edward", "phil", "kaylee", "michelle", "erin"]
for person in people:
    if person not in favorite_languages:
        print("Answer the poll " + person.title() + "!")


# Nesting
michelle = {"first_name" : "Michelle",
    "last_name" : "Hang",
    "age" : "14",
    "city" : "West Vancouver"}
kaylee = {"first_name" : "Kaylee",
    "last_name" : "Liu",
    "age" : "13",
    "city" : "West Vancouver"}
erin = {"first_name" : "Erin",
    "last_name" : "An",
    "age" : "13",
    "city" : "West Vancouver"}
people = [michelle, kaylee, erin]
for person in people:
    print(person)

sid = {"Owner" : "Nicole",
    "Animal" : "Rabbit"}
oliver = {"Owner" : "Christine",
    "Animal" : "Cat"}
dibbs = {"Owner" : "Slake",
    "Animal" : "Dog"}
pets = [sid, oliver, dibbs]
for pet in pets:
    print(pet)

slake = {"Slake" : "California"}
christine = {"Christine" : "Illinois"}
nicole = {"Nicole" : "Canada"}
favourite_places = [slake, christine, nicole]
for favourite_place in favourite_places:
    print(favourite_place)