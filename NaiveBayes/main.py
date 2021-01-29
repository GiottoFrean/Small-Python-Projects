import numpy as np

number_of_elements = 10
array = np.random.randint(0,10,number_of_elements) # make a random array
sorted_array_copy_for_validation = np.sort(array.copy()) # store a copy, to check the results.

print(array, "  <- original array")
print("")

# This is a special method to print the array in sections, to show which bits are being operated on (before and after). 
# Good for debugging, and checking process.
def print_array_sections(array, number_of_sections, gap_size):
	for section in range(number_of_sections):
		print(array[section * gap_size:(section+1) * gap_size],end="")
	print("")

# Main loop: 
for depth in range(1,int(np.ceil(np.log2(number_of_elements)))+1): # At most log_2(number_of_elements)+1 depth needed. 
	gap_size = 2**depth # show many items are being merged/sorted at one time. 
	number_of_sections = int(np.ceil(number_of_elements/gap_size))
	print_array_sections(array, number_of_sections, gap_size) # show array in sections, before processing the depth. 

	for section in range(number_of_sections):
		lower = section * gap_size
		upper = section * gap_size + int(gap_size/2)
		for i in range(min(gap_size,number_of_elements-lower)-1):
			if(upper>=number_of_elements or upper==(section+1)*gap_size or lower==upper): # special case ending conditions.
				break
			else:
				if array[lower]<=array[upper]:
					lower += 1
				else: 
					temp = array[upper]
					for j in range(upper,lower,-1): # push all elements forward 1 space, to make room for insertion.  
						array[j]=array[j-1]
					array[lower] = temp
					lower += 1
					upper += 1
	
	print_array_sections(array, number_of_sections, gap_size) # show array after this step. 

print(array, "  <- final sorted array")
assert((array==sorted_array_copy_for_validation).all()) # Check the solution was correct. 


