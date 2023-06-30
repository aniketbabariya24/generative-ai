def fibonacci(n):
    ans = [0, 1]  
    if n <= 2:
        return ans[:n]
    else:
        for i in range(2, n):
            next = ans[i-1] + ans[i-2]
            ans.append(next)
        return ans


n = 5
ans = fibonacci(n)
print(ans)
