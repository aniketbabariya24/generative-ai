# ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:
# AuKellylt


str1 = "Ault"
str2 = "Kelly"

mid = len(str1) // 2
ans = str1[:mid] + str2 + str1[mid:]

print(ans)
