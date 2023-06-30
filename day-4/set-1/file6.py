def countVowel(str):
    vowels = "aeiouAEIOU"
    ans = 0
    for i in str:
        if i in vowels:
            ans += 1
    return ans


str = "masai"
ans = countVowel(str)
print("Number of vowels:", ans)
