#1

PI=3.14
print("Hello user!")
radius = float(input("Tell me the radius for a circle: "))
area = PI * radius * radius
print(f"the area for the circle is {area}")

#2

cm = float(input("How tall are you in cm?: "))
inches = cm / 2.54
feet = inches / 12
print(f"You are {cm} cm, {inches} inches and {feet} feet.")

#3

n = int(input("Enter a value for n: "))
print(n**2)
print(n**3)
print(n**4)

#4

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")

#5

name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")
age = input("Enter the student's age: ")
print(f"{name}, {student_class}, {age} years old")

#6

n = int(input("Enter a single digit: "))
three_digit_number = str(n) + str(n+1) + str(n+2)
print(three_digit_number)

#7

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print(f"Original values: {a}, {b}, {c}")
a_new = a + b
b_new = b + c
print(f"New values: {a_new}, {b_new}, {c}")















