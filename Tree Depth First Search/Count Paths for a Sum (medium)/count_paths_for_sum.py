class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths_recursive(current_node, required_sum, current_path):
    if current_node is None:
        return 0

    current_path.append(current_node.val)

    path_count, path_sum = 0, 0
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        if path_sum == required_sum:
            path_count += 1

    path_count += count_paths_recursive(current_node.left, required_sum, current_path)
    path_count += count_paths_recursive(current_node.right, required_sum, current_path)

    del current_path[-1]

    return path_count


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))
