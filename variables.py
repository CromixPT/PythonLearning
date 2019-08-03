import math

students_count = 1000
rating = 4.99
is_published = True


print(students_count)

# strings
course_name = "Python Programming"
string_length = len(course_name)
print(string_length)

print(course_name[0])

# using negative index starts counting from the end of string
print(course_name[-1])

print(course_name[0:3])

print(course_name[3:])


first = "John"
last = "Doe"

full_name = first + " " + last
print(full_name)


# another way
first_name = "Johny"
last_name = "English"

full = f"{first_name} {last_name}"
print(full)


# string methods
course = "   python programming    "

print(course.upper())
print(course.title())
# trims the string
print(course.strip())

print(course.find("pro"))

print(course.replace("p", "j"))

print("pro" in course)


# numbers
print(round(2.6))
print(abs(-2.9))

print(math.ceil(2.2))


print(math.factorial(4))


x = input("x: ")
y = int(x)+1
print(f"x: {x}, y: {y}")
