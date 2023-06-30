# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def finonacci(num):
    ans=[0,1]
    if num<=2:
        return ans[:num]
    for i in range(2,num):
        nextNum= ans[i-1]+ans[i-2]
        ans.append(nextNum)

    return ans    
    
num= 5
x= finonacci(num)
print(x)     
