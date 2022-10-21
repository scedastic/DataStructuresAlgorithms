from types import new_class


class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value) -> bool:
        """Add to the head"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        """Remove Node from the tail"""
        if self.length == 0:
            return None            
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self) -> Node:
        """Remove Node from the head"""
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        temp = self.head

        # optimize for DLL to go backwards if index is in the upper half of the list
        if index <= self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value) -> bool:        
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.next.prev = temp.prev  # Set `after` to `temp.next` and substitute as `after.prev = temp.prev`
        temp.prev.next = temp.next  # Set `before` to `temp.prev` and substitute as `before.next = temp.next`
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



if __name__ == '__main__':
    my_doubly_linked_list = DoublyLinkedList(0)
    my_doubly_linked_list.append(1)
    my_doubly_linked_list.append(2)

    my_doubly_linked_list.remove(1)
    my_doubly_linked_list.print_list()