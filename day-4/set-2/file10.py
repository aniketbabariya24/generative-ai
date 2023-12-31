# ### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**
# tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

list1 = list(tuple1)

list1[1][0] = 222

ans = tuple(list1)

print(ans)
