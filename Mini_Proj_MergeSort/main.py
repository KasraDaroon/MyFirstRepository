list = [756, 634, 899, 234, 456, 983, 175, 305]

def merge_sort(arr):
    
    if len(arr) > 1:
        
        middle = len(arr) // 2
        
        left = arr[:middle]
        
        right = arr[middle:]

        merge_sort(left)
        
        merge_sort(right)

        x = y = z = 0
       
        while x < len(left) and y < len(right):
            
            if left[x] < right[y]:
                
                arr[z] = left[x]
                
                x += 1
            else:
                
                arr[z] = right[y]
                
                y += 1
            
            z += 1

        while x < len(left):
            
            arr[z] = left[x]
            
            x += 1
            
            z += 1

        while y < len(right):
            
            arr[z] = right[y]
           
            y += 1
            
            z += 1

merge_sort(list)

print(list)