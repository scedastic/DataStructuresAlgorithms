class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    
class Stack:
    """Stack implemented as a linked list with a pointer to top
        Each Node (next) points to the previous node 
        and the first node points to None
    """
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)        
        
        if self.height > 0:
            new_node.next = self.top

        self.top = new_node
        self.height += 1

    def pop(self) -> Node:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

if __name__ == '__main__':
    my_stack = Stack(7)
    my_stack.push(23)
    my_stack.push(3)
    my_stack.push(11)
    my_stack.print_stack()
    
    x = my_stack.pop()
    print(f'We popped {x.value}\n')
    my_stack.print_stack()