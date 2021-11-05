class BST:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_bst(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return

        if self.key < data:
            if self.right_child:
                self.right_child.insert_bst(data)
            else:
                self.right_child = BST(data)
        else:
            if self.left_child:
                self.left_child.insert_bst(data)
            else:
                self.left_child = BST(data)

    def search_bst(self, data):
        if self.key == data:
            print("node is found", data)
            return
        if data < self.key:
            if self.left_child:
                self.left_child.search_bst(data)
            else:
                print("Node in not in the tree")
        else:
            if self.right_child:
                self.right_child.search_bst(data)
            else:
                print("Node in not in the tree")

if __name__ == '__main__':
    root = BST(15)
    root_el = vars(root)
    print(root_el)
    List = [16, 20, 5, 3, 27, 19, 34, 5, 77, 4, 3, 6, 3, 7, 9]
    for i in List:
        root.insert_bst(i)
    root.search_bst(34)
