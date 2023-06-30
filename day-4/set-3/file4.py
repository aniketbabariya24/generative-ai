# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def checkPalindrome(str):
    bag=str[::-1]

    if bag==str:
        return True
    
    return False;      

str="maddsam"

if checkPalindrome(str):
    print("The word", str,"is palindrome")
else:
    print("The word", str,"is not palindrome")    