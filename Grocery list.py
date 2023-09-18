
# Jack Carruthers
# Grocery List


grocery_list = ('Apples', 'Pears', 'Bananas', 'Apricots', 'Plum', 'Peaches') # The grocery list 

inp_lst = (grocery_list)
length = len(inp_lst)
print("Your grocery list contains", length,"items.") # Tells user ammount of items in grocery list 

import time
time.sleep(1) # sleeps code for 3 secs 
end ='\n' # variable made for line space
print(end) # Adds a line space 

for readout in grocery_list:
    print(readout) # Outputs list

import time
time.sleep(1) 
print(end) # sleeps code for 3 seconds and adds line space

print ("The first item in your grocery list is",grocery_list[0]) # prints first item of list (is 0 as you have to count from 0)
print(end) # Adds a line space 
time.sleep(1) 
print ("The last item in your grocery list is",grocery_list[5]) # prints last item 

time.sleep(1) 
swap = list(grocery_list)
swap[1], swap[4] = grocery_list[4], grocery_list[1]
print(end) # Adds a line space 
print("Your swapped list is:")
print(swap) # This swap and outputs the change in the pears and plums in list

time.sleep(1) 
print(end)  
swap.append("Strawberry")
swap.append("Raspberry") # adds two new pieces of data to list 
print("Your new list is:")
print(swap) # prints updated list 

time.sleep(1)
print(end)
print("Your list in ascending order is:")
swap.sort() # Sorts list in ascending order
print(swap) 


