class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if target is root
        if self.value == target:
            return True
        # If target is less than root, check left
        elif target < self.value:
            if self.left is None:
                return False
            # if target == self.left.value:
            #     return True
            else:
                # if not call method again
                return self.left.contains(target)
        # If target is greater or equal than root, check right
        elif target >= self.value:
            if self.right is None:
                return False
            # if target == self.right.value:
            #     return True
            else:
                # if not call method again
                return self.right.contains(target)
        return False