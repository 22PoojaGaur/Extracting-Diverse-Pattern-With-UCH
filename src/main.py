# author 22PoojaGaur

import sys
import copy
import patterns


class Node(object):

    # tree node
    def __init__(self, id, value, children=[]):
        super(Node, self).__init__()
        self.id = id
        self.value = value
        self.children = copy.deepcopy(children)


class Tree(object):
    def __init__(self):
        super(Tree, self).__init__()
        self.root = None
        self.node_count = 0

    def Insert_nodes(self, nodes):
        # if root empty insert root
        if self.root is None:
            self.node_count == 1
            self.root = Node(self.node_count, nodes[0])

        # insert remaining nodes in tree
        current = self.root
        for node in nodes[1:]:
            if node == '':
                continue

            child_vals = [c.value for c in current.children]
            # print("node" + str(node))
            if node not in child_vals:
                self.node_count == 1

                current.children.append(Node(self.node_count, node))
            child_vals = [c.value for c in current.children]

            for cnum in range(0, len(current.children)):
                if current.children[cnum].value == node:
                    current = current.children[cnum]
                    break

    def print_tree(self):

        if self.root is None:
            print("Tree is not built")
            return

        print(self.root.value + "\n")
        queue = [self.root]

        while len(queue) > 0:
            current = queue[0]
            has_child = 0
            for child in current.children:
                print(child.value + ' - ', end='')
                queue.append(child)
                has_child = 1
            if has_child:
                print("\n")
                has_child = 0
            if len(queue) >= 1:
                queue = queue[1:]

        return


def read_input():
    if len(sys.argv) < 3:
        print("file expect name of input file")
        sys.exit(1)

    try:
        in_filename = sys.argv[1]
        pat_filename = sys.argv[2]
        file = open(in_filename, 'r')
        fpat = open(pat_filename, 'r')
    except IOError:
        print("file not exist")
        sys.exit(1)

    is_item = 1
    # pattern threshold = 4
    freq_patterns = patterns.extract_frequent_patterns(fpat, 4)
    line = ''
    path = []
    CH = Tree()
    for line in file.readlines():
        if line.strip() == '':
            continue

        if is_item:
            # line is item
            item = line.strip()
            is_item = 0
        else:
            # line is path
            path = line.strip().split(' ')

            CH.Insert_nodes(path)
            is_item = 1

    return CH


def main():
    CH = read_input()
    CH.print_tree()


if __name__ == '__main__':
    main()
