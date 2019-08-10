#  defines a list
numbers = [1, 2, 3]
letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5

# can concatnate 2 lists
combined = zeros + letters

# can print a full list
print(combined)

# can use a iterable to create a list
incrementals = list(range(1, 21))
print(incrementals)

# strings are also iterable
word = list("Hello World")
print(word)

# get the number of items(size) in a list
size = len(incrementals)
print(f"Incrementals list size: {size}")

# acess items use the index
char = letters[1]
print(f"letters[1]: {char}")

# can also change the value at an index
letters[0] = "A"
print(letters)

# slice a list
sliced = letters[2:3]
print(f"Original: {letters}")
print(f"Sliced: {sliced}")

# it is possible to specify a step on slicing a list
new_number_list = list(range(20))
print(new_number_list[::2])  # prints every other item in the list

# now in reverse order
print(f"now in reverse: {new_number_list[::-2]}")

#looping in lists
for letter in letters:
    print(letter)

# to get the index
for letter in enumerate(letters):  # gives a tupple with (index,value)
    print(letter)

# add items
letters.append("e")
letters.insert(0, "-")

print(letters)


# remove items
letters.pop(0)
letters.remove("e")

print(letters)

# find items
if "d" in letters:
    print(letters.index("d"))

# number of ocourences of the item in a list
print(letters.count("d"))


# sort lists
numbers_list = [3, 52, 2, 8, 6]

numbers_list.sort()

print(numbers_list)

numbers_list.sort(reverse=True)

print(numbers_list)

# sorting into a new list
original = [3, 52, 2, 8, 6]

sorted_list = sorted(original)

print(sorted_list)

reversed_list = sorted(original, reverse=True)

print(reversed_list)


# A list of products, shopping list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    # can define a function to sort based on value
    return item[1]


# call the sort using the order/key function
items.sort(key=sort_item)
print(items)

# can use a lambda expression to order it
# lambda expression --> parameters:expression
items.sort(key=lambda item: item[1], reverse=True)
print(items)

# using a map funtion transforms items list into price list
prices = list(map(lambda item: item[1], items))

print(prices)


# filter the list with a lambda
high_prices = list(filter(lambda item: item[1] >= 10, items))

print(high_prices)

# list comprehensions
# another way to map and filter a list
new_map = [item[1] for item in items]
new_filter = [item for item in items if item[1] >= 10]

print(f"new map: {new_map}")
print(f"new filter: {new_filter}")


# zip fucntion combines 2 or more iterable objects into a tupple set
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]

final = list(zip(list1, list2, list3))


# stacks
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
last = stack.pop()
print(f"last = {last}")
print("Stack: ", stack)
if not stack:
    print("Disable back button")
else:
    print("Redirect: ", stack[-1])
