class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " + str(level) + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, node):
        self.children.append(node)
        

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

tree.add_child(cold)
tree.add_child(hot)

coffe = TreeNode('Coffe', [])
tea = TreeNode('Tea', [])
cola = TreeNode('Cola', [])
lemonade = TreeNode('Lemonade', [])

cold.add_child(cola)
cold.add_child(lemonade)
hot.add_child(coffe)
hot.add_child(tea)

print(tree)
