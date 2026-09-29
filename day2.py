#Arithmetic operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#Logical operators
#and
age = 22
print(age >= 18 and age <= 30)

#or
age = 22
print(age < 18 or age > 60)

#not
is_student = True
print(not is_student)

#if/elif/else
marks = 75

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 60:
    print("C")

else:
    print("D")

#Nested conditionals
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("you can enter.")
    else:
        print("ID required.")
else:
    print("you are under 18.")

#Practice 1 - Grading system
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

else:
    print("Grade: F")

#Practice 2- Basic Calculator
print("_________Calculator________")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result", num1 + num2)

elif choice == "2":
    print("Result", num1 - num2)

elif choice == "3":
    print("Result", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result", num1 / num2)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid choice.")
    