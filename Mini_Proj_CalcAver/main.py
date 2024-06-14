def calculate_average(numbers):
    
    sum = sum(numbers)  # Get the sum of the list
    
    items = len(numbers)  # Get the length of the list
    
    average = sum / items  # Calculate the average
    
    return average


list = [756, 634, 899, 234, 456, 983, 175, 305]

result = calculate_average(list)

print("average is", result)