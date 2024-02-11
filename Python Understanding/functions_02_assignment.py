print("NAME:: RAYAN AHMED")
print("ROLL NO:: BITF20M535")

print("\n ***ASSIGNMENT FUNCTIONS (HUNGER)***\n")

def validUser(code):
    if(code <= 10 and code > 0):
        return bool(1)
    else:
        return bool(0)


def hungerFunc():
    hunger = input("\nAre you Hungery???\n 'TRUE' OR 'FALSE' :: ")

    if hunger == "TRUE":
        print("let's eat some food...\n")
    elif hunger == "FALSE":
        print("Go to Sleep...")
    else:
        print("Not a Valid Option...")



code = int(input("Enter code (1-10):: "))


if(validUser(code)):
    print("(~~~ You are a Valid User ~~~)")

    print("\n...Calling Hunger Function...")
    hungerFunc()
else:
    print("(~~~ You are not a Valid User ~~~)")


print("\n%%Thankyou%%")