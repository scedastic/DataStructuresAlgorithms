def insertion_sort(my_list):
    """	
    • Always start with the second item in the list.
	• Compare it to the previous item.
	• If it's less, then swap.
    • Move to the next item (and compare it to the previous ones (all the way back) 
        until its' not less than the previous - hence it's in the right spot.
    """
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            # Slide it backward
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list
            



if __name__ == '__main__':
    my_list = [4,2,6,5,1,3]
    print(insertion_sort(my_list))