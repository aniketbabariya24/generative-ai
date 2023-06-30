# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def checkPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        return True
    
num=14
result= checkPrime(num)    

if result:
    print(num,"is Prime")

else:
    print(num, "is Not prime")