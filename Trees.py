"""
    Full Tree: each node either points to no Nodes or 2 nodes.
    Perfect Tree: Balanced all the way up - equal nodes on the left and right of the root.
    Complete: Nodes are filled left to right.
    Leaf: Nodes without children.
"""
from logging import root


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Given a node, all nodes to the left are less than and all nodes to the right are greater than
        Big O - Omega (log n) for searching, adding and removing
              - Omicron (n)
              - We look at it as if it were log n
    """
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        """Create new node, go through the tree one node at a time. 
            if tree is empty (root == None) set root to new node
            while loop
                If value < node then left
                Else if value > node then right
                Else if == return False
                If None, insert new_node
                Else goto next node
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:   # Spot is open
                    temp.left = new_node
                    return True                
                temp = temp.left
            else:   # Greater...
                if temp.right is None:   # Spot is open
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value) -> bool:
        """Does the tree have the value?
            If root is None -> False
            Start at the root.
            Travel the tree.
                If we ever get to a point that temp is None -> False and stop searching
                if value < temp -> left
                elif value > temp -> right
                else -> True
            return False
        """
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: # it is equal
                return True
        # We went through the tree and didn't find value
        return False
            
    def min_value_node(self, current_node) -> Node:
        """Return node with the lowest value under `current_node`
            Keep going left until node.left is None
        """
        while current_node.left:
            current_node = current_node.left
        return current_node




    
if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.min_value_node(my_tree.root).value)
    print(my_tree.min_value_node(my_tree.root.right).value)
