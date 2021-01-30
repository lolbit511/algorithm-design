# write a python program to calculate the sum of a list of numbers using recursion

# this is the recursive function to calculate the sum of numbers of the list
def list_sum(num_list):
    # checking if length of the list is equals 1, if it is, end the function
    if len(num_list) == 1:
        # end recursive function
        return num_list[0]
    else:
        # add first number in the current list, and then call the function again with the rest of the list ([1:])
        return num_list[0] + list_sum(num_list[1:])

# call the function and pass the list as a function to the parameter
print(list_sum([5,2,8,10,1]))