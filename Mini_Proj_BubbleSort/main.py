list = [756,634,899,234,456,983,175,305]

items = len(list)

for x in list:
    
    for y in list:
        
        y_index = list.index(y)
        
        if (y_index + 1) < items and (y - list[y_index + 1]) > 0:
            
            list[y_index], list[y_index + 1] = list[y_index + 1], y

print(list)