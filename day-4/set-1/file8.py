def findFactorial(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        ans = 1
        for i in range(1, number + 1):
            ans *= i
        return ans


number = 5
ans = findFactorial(number)
if ans is not None:
    print("Factorial of", number, "is", ans)

