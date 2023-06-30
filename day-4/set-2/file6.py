list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

ans=[]

for i in range(0,2):
    for j in range(0,2):
      ans.append(list1[i]+list2[j])

print(ans)   