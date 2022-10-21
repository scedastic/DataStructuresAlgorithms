"""Find items that appear in both lists"""

def inefficient_item_in_common(list1, list2) -> bool:
    """O(n^2)"""
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common(list1, list2) -> bool:
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

if __name__ == "__main__":
    list1 = [1,2,3,4]
    list2 = [5,4,3,7,9]
    print(inefficient_item_in_common(list1, list2))
    print(item_in_common(list1, list2))