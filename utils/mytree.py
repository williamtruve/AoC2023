class TreeNode:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class Tree:
    def __init__(self, root_data=None):
        self.root = TreeNode(root_data)

    def display_tree(self, node, level=0):
        if node is not None:
            print("  " * level + str(node.data))
            for child in node.children:
                self.display_tree(child, level + 1)

    def dfs(self, node, order='pre'):
        if node is not None:
            if order == 'pre':
                print(node.data)
            for child in node.children:
                self.dfs(child, order)
            if order == 'post':
                print(node.data)

    def bfs(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)
            print(current.data)

            for child in current.children:
                queue.append(child)

    def find_node(self, data, node=None):
        if node is None:
            node = self.root

        if node.data == data:
            return node

        for child in node.children:
            found_node = self.find_node(data, child)
            if found_node:
                return found_node

    def count_nodes(self, node=None):
        if node is None:
            node = self.root

        count = 1  # Count the current node

        for child in node.children:
            count += self.count_nodes(child)

        return count
    
    def height(self, node=None):
        if node is None:
            node = self.root

        if not node.children:
            return 0

        # Calculate the height of each child
        child_heights = [self.height(child) for child in node.children]

        # Return the maximum child height + 1 for the current node
        return max(child_heights) + 1

    def is_balanced(self, node=None):
        if node is None:
            node = self.root

        if not node.children:
            return True

        # Check if the heights of the children differ by more than one
        child_heights = [self.height(child) for child in node.children]
        return max(child_heights) - min(child_heights) <= 1 and all(self.is_balanced(child) for child in node.children)

    def lca(self, node1, node2):
        ancestors1 = set()
        while node1 is not None:
            ancestors1.add(node1)
            node1 = node1.parent

        while node2 not in ancestors1:
            node2 = node2.parent

        return node2

    def serialize(self, node=None):
        if node is None:
            node = self.root

        serialized_data = {'data': node.data, 'children': []}
        for child in node.children:
            serialized_data['children'].append(self.serialize(child))

        return serialized_data

    @classmethod
    def deserialize(cls, serialized_data):
        tree = cls(serialized_data['data'])
        print(tree)
        for child_data in serialized_data['children']:
            child_node = cls.deserialize(child_data)
            tree.root.add_child(child_node)

        return tree

# Example usage:
my_tree = Tree("Root")
# ... (Add nodes to the tree)
my_tree.root.add_child(TreeNode("Child 1"))
my_tree.root.add_child(TreeNode("Child 2"))

# Display the tree
my_tree.display_tree(my_tree.root)

# Depth-First Search (Pre-order)
print("DFS (Pre-order):")
my_tree.dfs(my_tree.root, order='pre')

# Depth-First Search (Post-order)
print("DFS (Post-order):")
my_tree.dfs(my_tree.root, order='post')

# Breadth-First Search
print("BFS:")
my_tree.bfs()

# Find Node
data_to_find = "Child 1"
found_node = my_tree.find_node(data_to_find)
if found_node:
    print(f"Node with data '{data_to_find}' found: {found_node.data}")
    found_node.add_child(TreeNode("Grandchild 1"))

# Count Nodes
node_count = my_tree.count_nodes()
print(f"Total number of nodes in the tree: {node_count}")


# Example usage:
# ... (previous code)

# Height of the Tree
tree_height = my_tree.height()
print(f"Height of the tree: {tree_height}")

# Check if Tree is Balanced
balanced = my_tree.is_balanced()
print(f"Is the tree balanced? {'Yes' if balanced else 'No'}")

# Lowest Common Ancestor (LCA)
node1 = my_tree.find_node("Grandchild 1")
node2 = my_tree.find_node("Child 2")
lca_node = my_tree.lca(node1, node2)
print(f"LCA of '{node1.data}' and '{node2.data}': {lca_node.data}")

# Serialize and Deserialize
serialized_tree = my_tree.serialize()
print("Serialized Tree:")
print(serialized_tree)

# Deserialize the tree from the serialized data
new_tree = Tree.deserialize(serialized_tree)
print("Deserialized Tree:")
new_tree.display_tree(new_tree.root)
