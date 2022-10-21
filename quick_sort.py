
def pivot(my_list, pivot_index, end_index):
    """Rearrange the array and return the swap index 
        (which had the pivot value?)
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def swap(my_lists, index1, index2):
    my_list[index1],  my_list[index2] = my_list[index2], my_list[index1]


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

if __name__ == "__main__":
    my_list = [4,6,1,7,3,2,5]
    print(quick_sort(my_list))