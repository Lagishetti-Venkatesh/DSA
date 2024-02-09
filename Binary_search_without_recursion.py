def binary_search(a, x):
  i = 0
  j = len(a) - 1
  mid = 0
  while i != j:
    mid = i+ ((j-i)//2)
    if a[mid] == x:
      return mid
    elif a[mid] <x:
      i = mid+1
    else:
      j = mid -1
  if i == j:
    if a[i] == x:
      return i
array = [10, 23, 35, 67, 75, 86, 90]

#iterating through the each element to see its working 
for i in array[::-1]:
  result = binary_search(array, i)
  print(f"Searching value : {i} is present at index: {result}")

