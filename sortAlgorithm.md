# Sort 

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

## Quick Sort

```python
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSork(arr,low,high):
    if low < high:  
        m = partition(arr,low,high)
        quicksort(arr,low,m-1)
        quicksork(arr,m+1,high)
    return arr
```

## Merge Sort

```python
def merge(a,b):
    c = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: 
            c.append(a[i])
            i += 1
        else: 
            c.append(a[j])
            j += 1
    if i == len(a):
        for num in b[j:]: c.append(num)
    elif j == len(b):
        for num in a[i:]: c.append(num)
    return c 

def mergeSort(a):
    if len(a) <= 1: return a
    mid = len(a) // 2
    left = mergeSort(a[0:mid])
    right = mergeSort(a[mid:])
    return merge(left,right)
```
