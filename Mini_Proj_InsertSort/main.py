list = [756, 634, 899, 234, 456, 983, 175, 305]

def insertion_sort(arr):
   
    for x in range(1, len(arr)):
    
        element = arr[x]
     
        y = x - 1
     
        while y >= 0 and element < arr[y]:
     
            arr[y + 1] = arr[y]
      
            y -= 1
     
        arr[y + 1] = element

insertion_sort(list)

print(list)