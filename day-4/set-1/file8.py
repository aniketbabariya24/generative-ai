# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def fect(N):
  if N == 0 or N == 1:
    return 1
    
  return N * fect(N-1)


num=5

ans=fect(num)

print("Factorial of", num, "is", ans)