# Making lists
names = ["Kaylee", "Michelle", "Erin", "Joanna"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = "Hi "
print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])

brands = ["Kia", "Tesla", "Mercedez"]
sentance = "I would like a "
car = " car."
print(sentance + brands[0] + car)
print(sentance + brands[1] + car)
print(sentance + brands[2] + car)


# Moving list items
guests = ["Christine", "Kamaji", "Slakey"]
letter = "You are invited to my dinner, "
print(letter + guests[0])
print(letter + guests[1])
print(letter + guests[2])

print(guests[1])
del guests[1]
guests.insert(1, "Furr-aji")
print(letter + guests[0])
print(letter + guests[1])
print(letter + guests[2])

print("More people can attend the dinner!")
guests.insert(0, "Kaylee")
guests.insert(2, "Erin")
guests.append("Michelle")
print(letter + guests[0])
print(letter + guests[1])
print(letter + guests[2])
print(letter + guests[3])
print(letter + guests[4])
print(letter + guests[5])

print("We can only invite 2 people!")
guests.pop(5)
guests.pop(3)
guests.pop(0)
guests.pop(2)
print(letter + guests[0])
print(letter + guests[1])

del guests[1]
del guests[0]
print(guests)


# Sorting lists
places = ["England", "Paris", "Korea", "California", "Italy"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

guests = ["Christine", "Kamaji", "Slakey"]
print("There are " + str(len(guests)) + " people attending the party.")
