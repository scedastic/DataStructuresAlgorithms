"""As you iterate the list, the larger ones will move to the end."""

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                # perform the python swap a,b = b,a
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


if __name__ == "__main__":
    print(bubble_sort([4,2,6,1,5,3]))