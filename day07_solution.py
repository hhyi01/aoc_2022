import sys

with open("day07_input.txt") as f:
    terminal_output = f.readlines()


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.files = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_tree(terminal_lines):
    root_dir_name = terminal_lines[0].strip().split(" ")[2]
    root_dir = TreeNode(root_dir_name)
    curr_dir = root_dir

    terminal_lines = terminal_lines[1:]

    for idx, output in enumerate(terminal_lines):
        line = output.strip()
        if "$ ls" in line:
            # listing contents
            continue
        elif "$ cd" in line:
            if ".." in line:
                # move up directory
                curr_dir = curr_dir.parent
            else:
                # moved into new directory
                next_dir_name = line.split(" ")[2]
                for c in curr_dir.children:
                    if c.data == next_dir_name:
                        curr_dir = c
        elif "dir " in line:
            dir_name = line.split(" ")[1]
            child_dir = TreeNode(dir_name)
            child_dir.parent = curr_dir
            curr_dir.add_child(child_dir)
        else:
            curr_dir.files.append(line)
    return root_dir


def traverse_directories(root_directory):
    directories = [root_directory]
    dir_size_lte_100k = 0
    total_disk_space = 70000000
    required_unused = 30000000
    space_to_free = 0
    directory_delete_size = sys.maxsize
    while directories:
        curr_dir = directories.pop()
        directory = [curr_dir.data]
        parent_dir = curr_dir.parent
        while parent_dir:
            directory.append(parent_dir.data)
            parent_dir = parent_dir.parent
        directory.reverse()
        dir_path = "/".join(directory)
        dir_size = get_directory_size(curr_dir)
        print("Current path:", dir_path, "Size:", dir_size)
        if curr_dir.data == "/":
            size_of_root_dir = dir_size
            space_to_free = required_unused - (total_disk_space - size_of_root_dir)
        if dir_size <= 100000:
            dir_size_lte_100k += dir_size
        if dir_size >= space_to_free:
            if dir_size < directory_delete_size:
                directory_delete_size = dir_size
        if curr_dir.children:
            directories.extend(curr_dir.children)
    print("Total size of directories of at more 100k:", dir_size_lte_100k)
    print("Smallest directory size to delete:", directory_delete_size)
    return dir_size_lte_100k, directory_delete_size


def get_directory_size(root_directory):
    directories = [root_directory]
    total_size = 0
    while directories:
        curr_dir = directories.pop()
        file_sum = 0
        if curr_dir.files:
            for file in curr_dir.files:
                file_size = int(file.split(" ")[0])
                file_sum += file_size
            total_size += file_sum
        if curr_dir.children:
            directories.extend(curr_dir.children)
    return total_size


# puzzle 1 & 2
root = build_tree(terminal_output)
print(traverse_directories(root))
