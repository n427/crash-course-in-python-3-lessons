# Input()
car = "car" #input()
print("Let me see if I can find you a " + car)

seats = 9 #input()
if seats > 8:
    print("You'll have to wait a while.")
else:
    print("Come with me.")

number = int(input("Is this number divisbible by 10?\n"))
if number % 10 == 0:
    print("It is divisible by 10")
else:
    print("It is not divisible by 10")