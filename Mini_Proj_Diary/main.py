def new_entry(entry, file_path="diary_entries.txt", timestamp=False):
    
    try:
        
        with open(file_path, "a") as file:
            
            if timestamp:
                
                import datetime
                
                timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                file.write(f"{timestamp_str}: {entry}\n")
            else:
                
                file.write(f"{entry}\n")
    
    except Exception as e:
        
        print(f"error: {e}")

def old_entry(file_path="diary_entries.txt"):
   
    try:
 
        with open(file_path, "r") as file:
  
            entries = file.readlines()
  
            for entry in entries:
  
                print(entry.strip())
 
    except FileNotFoundError:
 
        print("empty")
 
    except PermissionError:
 
        print("denied access")

new_entry("dear diary")

old_entry()

try:
  
    new_entry("new entry with timestamp", timestamp=True)
  
    old_entry()

except Exception as e:
 
   print(f"error: {e}")