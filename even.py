total_even_numbers = 0

for number in range(1, 10):
    if number % 2 == 0:
        total_even_numbers += 1
        print(number)
print(f"We have {total_even_numbers} even numbers")
