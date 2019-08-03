# Comparison Operators < > <= >= != ==
print("\nComparison Operators: ")
print(f"10 > 3: {10 > 3}")
print(f"10 >= 3: {10 >= 3}")
print(f"10 < 3: {10 < 3}")
print(f"10 <= 3: {10 <= 3}")
print(f"10 == 10: {10 == 10}")
print(f"10 != 3: {10 != 3}")

print(f"bag > apple: {'bag' > 'apple'}")

print(f"bag == BAG: {'bag' == 'BAG'}")

print(f"b: {ord('b')}")
print(f"B: {ord('B')}")

# conditional statments
temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink enough water!")
elif temperature >= 20:
    print("Its nice")
else:
    print("It's cold")
print("done")


# Ternary Operator
print("-"*70)
print("Ternary Operator:")
age = 22

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# for loops
print("-"*70)
print("For loops:")

sucessfull = False
for number in range(1, 4):
    print("Attempt",  number, (number) * ".")
    if sucessfull:
        print("Sucessful")
        break
else:
    print("Attempeted 3 times and failed")

# nested loops
print("-"*70)
print("nested loops:")

for x in range(5):
    for y in range(3):
        print(f"Coordinates({x},{y})")
