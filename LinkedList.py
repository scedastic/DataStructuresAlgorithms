class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node        
        self.length += 1
        return True

    def pop(self) -> Node:
        """Remove and return the last Node"""
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        """Remove and return the first Node"""
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index) -> Node:
        """Return the node at that index"""
        
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value) -> bool:
        """Set the value at that index"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:
        """Insert a new node at the index"""
        if index < 0 or index > self.length:
            return False
        # Insert at the head
        if index == 0:
            return self.prepend(value)
        # Insert at the tail
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        # reuse get() to traverse the list
        temp = self.get(index - 1)  
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def reverse(self) -> None:
        """
        Swap head and tail
        "reverse the arrows"- Have 3 pointers travel together from tail to head

        """
        self.head, self.tail = self.tail, self.head
        temp = self.tail
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
if __name__ == '__main__':
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)

    my_linked_list.reverse()
    my_linked_list.print_list()