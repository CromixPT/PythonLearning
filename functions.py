# 1 - Defining Functions
def greet():
    print("Hello,")
    print("Welcome aboard!")


def greeting(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard!")


greeting("Mosh", "Hamedammi")


# set up a defult value on the by argument, making it optional
def increment(number, by=1):
    return number + by


print(increment(number=2))
print(increment(number=2, by=2))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4))


# uses a dictionary to save the multiple keyword arguments
def save_user(**user):
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Mosh")
