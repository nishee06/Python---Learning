#loop
for i in range(5):
    print("Hello")

#for loop
for i in range(6):
    print(i)

#range(stop)
for i in range(5):
    print(i)

#range(start,stop)
for i in range(2, 6):
    print(i)

#range(start, stop, step)
for i in range(2, 10, 2):
    print(i)

#while loop
count = 1

while count <=5:
    print(count)
    count = count + 1

#break
for i in range(1, 8):
    if i == 5:
        break
    print(i)

#continue
for i in range(1, 9):
    if i == 3:
        continue
    print(i)

#nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

#Practice 1- fizzBuzz
for i in range(1, 21):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

#practice2
#star triangle
for i in range(1, 6):
    print('*' * i)

#pyramid
for i in range(1, 6):
    space = " " * (5 - i)
    star = "*" * (2 * i - 1)
    print(space + star)

#practice3- number guessing game
secret_number = 7

while True:
    guess = int(input("Enter the guess number: "))
    if guess == secret_number:
        print("Correct! you guess it.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
