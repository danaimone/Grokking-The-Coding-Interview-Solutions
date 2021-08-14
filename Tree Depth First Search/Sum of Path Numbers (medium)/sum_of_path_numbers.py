class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers_recursive(current_node, current_path, all_paths):
    if current_node is None:
        return

    current_path.append(current_node.val)

    if current_node.left is None and current_node.right is None:
        for i in current_path:
            completed_num_path = int("".join(map(str, current_path)))
        all_paths.append(completed_num_path)
    else:
        find_sum_of_path_numbers_recursive(current_node.left, current_path, all_paths)
        find_sum_of_path_numbers_recursive(current_node.right, current_path, all_paths)

    del current_path[-1]

def find_sum_of_path_numbers(root):
    all_paths = []
    find_sum_of_path_numbers_recursive(root, [], all_paths)
    return sum(all_paths)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


