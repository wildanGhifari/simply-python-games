print("Welcome to my first game!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

if age >= 18:
    print("You are old enough!")
elif age >= 13:
    print("You can play with supervision")
else:
    print("You are not old enough to play..")
