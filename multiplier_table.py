# Python program to print the multiplication table of 6 from 1 to 50 using a while loop
number = 6
multiplier = 1

while True:
    result = number * multiplier
    if result > 50:
        break
    print(f"{number} x {multiplier} = {result}")
    multiplier += 1
