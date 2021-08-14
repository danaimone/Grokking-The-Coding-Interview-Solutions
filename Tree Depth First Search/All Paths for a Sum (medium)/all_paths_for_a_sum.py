class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths_recursive(current_node, required_sum, current_path, all_paths):
    if current_node is None:
        return

    current_path.append(current_node.val)

    if current_node.val == required_sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        updated_sum = required_sum - current_node.val
        find_paths_recursive(current_node.left, updated_sum, current_path, all_paths)
        find_paths_recursive(current_node.right, updated_sum, current_path, all_paths)

    del current_path[-1]


def find_paths(root, required_sum):
    all_paths = []
    find_paths_recursive(root, required_sum, [], all_paths)
    return all_paths


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))

