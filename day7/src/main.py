from anytree import Node


def parse_terminal_output(terminal_output_file):
    with open(terminal_output_file, 'r') as terminal_output:
        root_node = Node("root", size=0)
        current_node = root_node
        for line in terminal_output.readlines():
            if line.startswith('$'):
                line_parts = line.split(' ')
                if line_parts[1] == 'cd':
                    current_node = change_directory(current_node, trim_blank_line(line_parts[2]))
            else:
                parts = line.split(' ')
                if parts[0] != 'dir':
                    add_size_to_branch(current_node, int(parts[0]))
        return root_node



def change_directory(current_node: Node, destination):
    if destination == '..':
        return current_node.parent
    else:
        return add_children_to_node(current_node, destination)

def add_size_to_branch(starting_node: Node, size: int):
    starting_node.size += size
    if starting_node.parent:
        add_size_to_branch(starting_node.parent, size)

def add_children_to_node(current_node: Node, children: str):
    if current_node.name == 'root' and children == '/':
        return current_node
    children_node = next(filter(lambda x: x.name == 'b', current_node.children), None)
    if children_node is None:
        children_node = Node(children, size=0, parent=current_node)
    return children_node

def find_node_closest_to(root_node: Node, size: int):
    sizes = []
    if root_node.size >= size:
        sizes.append(root_node.size)
    for children in root_node.children:
        children_size = find_node_closest_to(children, size)
        if children_size > 0:
            sizes.append(children_size)
    return min(sizes) if sizes else 0


    if (root_node.size < size):
        return 0
    else:
        if root_node.children:
            for children in root_node.children:
                children_total = find_nodes_with_size_bigger_than(children, size)
                total += children_total
            return total
        else:
            return root_node.size

def find_nodes_with_size_smaller_than(root_node: Node, size: int):
    total=root_node.size if root_node.size < size else 0
    for children in root_node.children:
        children_total = find_nodes_with_size_smaller_than(children, size)
        total += children_total
    return total

def trim_blank_line(line_fragment: str):
    return line_fragment.replace('\n', '')
def solve_part_1(input_file):
    root_node = parse_terminal_output(input_file)
    return find_nodes_with_size_smaller_than(root_node, 100000)

def solve_part_2(input_file):
    total_fs = 70000000
    space_needed = 30000000
    root_node = parse_terminal_output(input_file)
    free_space = total_fs - root_node.size
    space_needed = space_needed - free_space
    return find_node_closest_to(root_node, space_needed)