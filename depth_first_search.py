from Trees import BinarySearchTree

class DFSTree(BinarySearchTree):
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        
        traverse(self.root)
        return results
            
    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
            
        traverse(self.root)
        return results


if __name__ == "__main__":
    """
    Create a tree that looks like this

               47
             /     \
           21      76
          /  \    /  \
        18   27  52  82
    """
    my_tree = DFSTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.dfs_pre_order())
    print(my_tree.dfs_post_order())
    print(my_tree.dfs_in_order())