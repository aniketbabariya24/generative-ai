str = "MaSaI"

lower = ""
upper = ""

for char in str:
    if char.islower():
        lower += char
    else:
        upper += char

ans = lower + upper

print(ans)
