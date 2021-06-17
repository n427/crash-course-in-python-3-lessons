# For loops
pizzas = ["Cheese", "Salmon", "Bacon"]
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizzas!")
print("I love pizza!")

animals = ["Hamster", "Dog", "Cat"]
for animal in animals:
    print(animal)
    print("A " + animal + " would make a great pet!")
print("All of these animals are great!")


# Numbers with For loops
for number in range(1, 21):
    print(number)

million = list(range(1, 1000001))
'''print(million)'''
print(min(million))
print(max(million))
print(sum(million))

odds = list(range(1, 21, 2))
print(odds)

threes = list(range(3, 31, 3))
for three in threes:
    print(three)

cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

cubes_2 = [c**2 for c in range(1, 11)]
print(cubes_2)


# Slicing Lists
pizzas = ["Cheese", "Salmon", "Bacon", "Pepperoni", "Veggie"]
print("The first three items in the list are:")
for pizza in pizzas[:3]:
    print(pizza)
print("\n")
print("Three items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)
print("\n")
print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)


# Copying lists
my_pizzas = ["Cheese", "Salmon", "Bacon"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Veggie")
friend_pizzas.append("Canadian")
print("My favourite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)
print("\n")
print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print("\n")


# Tuples
foods = ("Sushi", "Ramen", "Spaghetti", "Pizza", "Cookies")
for food in foods:
    print(food)
print("\n")
foods = ("Sushi", "Ramen", "Spaghetti", "Chicken", "Corndogs")
for food in foods:
    print(food)