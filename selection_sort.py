"""
    Go through each index of the list 
    Get the index of the smallest item
    ....
"""

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i < min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


if __name__ == "__main__":
    my_list = [4,2,6,5,1,3]
    print(selection_sort(my_list))