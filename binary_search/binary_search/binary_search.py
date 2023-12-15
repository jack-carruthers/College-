# Jack Carruthers 

# Binary Search 

# initial value as not found value yet 
found = False 

# list of numbers 
nlist = [6, 9, 12, 21, 29, 38, 40, 64, 78, 80, 92, 100]

# term looking for 
print("\n", nlist)
search_term = int(input("Enter a number you wish to look for."))

# First and last pointers 
first = 0 
last = len(nlist) - 1

while (found == False and last >= first): # loop 
    
    mid = (first + last)//2 # finds mid term 
    
    
    if (search_term == nlist[mid]):
        print(f"Item you searched for,", search_term, "\n was found") # produces message if seach term found 
        found = True # stops loop 
    
    else: 
        
        if (search_term > nlist[mid]): # is the search term greater than the midpoint
            first = mid+1
            
        elif (search_term < nlist[mid]): # is the search term less than the midpoint
            last = mid-1 
            
