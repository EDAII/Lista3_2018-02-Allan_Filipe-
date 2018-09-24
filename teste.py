
# Python program for counting sort 
  
# The main function that sort the given string arr[] in  
# alphabetical order 
def countSort(dataset): 
  
    # The sorted_list character array that will have sorted arr 
    output_list = [0 for position in range(99999)] 
  
    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count_list = [0 for position in range(99999)] 
  
    # For storing the resulting answer since the  
    # string is immutable 
    sorted_list = [0 for number in dataset] 
  
    # Store count_list of each character 
    for number in dataset: 
        count_list[number] += 1
  
    # Change count_list[i] so that count_list[i] now contains actual 
    # position of this character in output_list array 
    for position in range(99999): 
        count_list[position] += count_list[position-1] 
  
    # Build the output_list character array 
    for position in range(len(dataset)): 
        output_list[count_list[dataset[position]]-1] = dataset[position] 
        count_list[dataset[position]] -= 1
  
    # Copy the output_list array to arr, so that arr now 
    # contains sorted characters 
    for position in range(len(dataset)): 
        sorted_list[position] = output_list[position] 
    return sorted_list  

lista = [34, 2, 56, 7, 8, 98, 12, 35, 765, 456]
print(countSort(lista))