class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        """Add a node to the Queue"""
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self) -> Node:
        if self.length == 0:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None            
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self) -> None:
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


if __name__ == "__main__":
    my_queue = Queue(1)
    my_queue.enqueue(2)

    my_queue.print_queue()

    print(f"removing {my_queue.dequeue().value}")
    print(f"removing {my_queue.dequeue().value}")
    print(my_queue.dequeue())