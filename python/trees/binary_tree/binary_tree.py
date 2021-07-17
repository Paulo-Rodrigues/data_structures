class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_left(self, value):
        self.left = BinaryTree(value)
        return self.left
        
    def insert_right(self, value):
        self.right = BinaryTree(value)
        return self.right

    def __repr__(self):
        return 'BinaryTree({0})'.format(self.value)

    def __str__(self):
        return 'BinaryTree({0})'.format(self.value)

    def __iter__(self):
        return inorder(self)

    def preorder(self):
        yield self
        if self.left:
            for node in self.left:
                yield node
        if self.right:
            for node in self.right:
                yield node

    def inorder(self):
        if self.left:
            for node in self.left:
                yield node
        yield self
        if self.right:
            for node in self.right:
                yield node

    def postorder(self):
        if self.left:
            for node in self.left:
                yield node
        if self.right:
            for node in self.right:
                yield node
        yield self

    def breadth_first(self):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def levelorder(self):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def get_depth(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_depth()
        elif self.right is None:
            return 1 + self.left.get_depth()
        else:
            return 1 + max(self.left.get_depth(), self.right.get_depth())

    def get_height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_height()
        elif self.right is None:
            return 1 + self.left.get_height()
        else:
            return 1 + max(self.left.get_height(), self.right.get_height())

    def get_size(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_size()
        elif self.right is None:
            return 1 + self.left.get_size()
        else:
            return 1 + self.left.get_size() + self.right.get_size()

    def get_height_recursive(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_height_recursive()
        elif self.right is None:
            return 1 + self.left.get_height_recursive()
        else:
            return 1 + max(self.left.get_height_recursive(), self.right.get_height_recursive())

    def get_size_recursive(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_size_recursive()
        elif self.right is None:
            return 1 + self.left.get_size_recursive()
        else:
            return 1 + self.left.get_size_recursive() + self.right.get_size_recursive()

    def get_height_iterative(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_height_iterative()
        elif self.right is None:
            return 1 + self.left.get_height_iterative()
        else:
            height = 0
            queue = deque([self])
            while queue:
                node = queue.popleft()
                height += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return height

    def get_size_iterative(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_size_iterative()
        elif self.right is None:
            return 1 + self.left.get_size_iterative()
        else:
            size = 0
            queue = deque([self])
            while queue:
                node = queue.popleft()
                size += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return size
            

