def main():
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()    

# Ask user for their name
##name = input("What is your name? ").strip().title()

# Remove whitespace from str and capitalize user's name
#name = name.strip().title()

# Split user's name into first and last name
#first, last = name.split(" ")

# Say hello to user
#print("hello,", name)
##print(f"hello, {name}")