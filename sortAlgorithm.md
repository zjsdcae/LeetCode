## Bubble Sort
```python
def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        flag = True
        for j in range(1,length-i):
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                flag = False
        if flag: return arr
    return arr
```

## Selection Sort
```python
def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        temp = i
        for j in range(i+1,length):
            if arr[j] < arr[temp]: temp = j
        arr[i], arr[temp] = arr[temp],arr[i]
    return arr    
```

## Insert Sort
```python
def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        cur = arr[i]
        j = i
        while j>0 and arr[j-1]>cur:
            a[j] = a[j-1]
            j -= 1
        arr[j] = cur
    return arr
```