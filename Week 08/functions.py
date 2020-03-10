import random

#functions go here
def be_nice(name):
    print("Hello " + name + ", it's so nice to meet you!")



# k here's the rest
quit = False

while not quit:
    name = input("What's your name? (or 'quit' to quit")

    if name == "quit":
        break

    choice = random.randint(1, 4)

    if choice == 1:
        be_nice(name)
    elif choice == 2:
        be_mean(name)
    elif choice == 3:
        be_weird(name)
    elif choice == 4:
        be_dead(name)


