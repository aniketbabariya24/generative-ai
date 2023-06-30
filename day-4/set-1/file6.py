# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

str= "ABCDE"
ans=0
vowels= "aeiouAEIOU"

for i in str:
    if i in vowels:
        ans=ans+1

print(ans)        