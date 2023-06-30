# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selectionSort(arr):
    for i in range(len(arr)):
        minimunIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimunIndex]:
                minimunIndex = j

        arr[i], arr[minimunIndex] = arr[minimunIndex], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
ans = selectionSort(arr)
print(ans)
