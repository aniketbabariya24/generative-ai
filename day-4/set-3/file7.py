# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")