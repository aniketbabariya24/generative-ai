# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:
# yaivePNT

str = "PyNaTive"

lower = ""
upper = ""

for i in str:
    if i.islower():
        lower += i
    else:
        upper += i

ans = lower + upper

print(ans)
