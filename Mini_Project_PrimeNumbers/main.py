N = int(input("enter number: "))

for index in range(2, N + 1):
    
    is_prime = True
    
    for div in range(2, int(index**0.5) + 1):
        
        if index % div == 0:
            
            is_prime = False
            
            break
    
    if is_prime:
        
        print(index)