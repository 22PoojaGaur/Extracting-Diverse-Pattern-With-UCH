# author 22PoojaGaur

import sys
import copy

class Node(object):
    #tree node
    def __init__(self,id, value, children = []):
        super(Node, self).__init__()
        self.id = id
        self.value = value
        self.children = copy.deepcopy(children)

class Tree(object):
            
    def __init__(self, root, node_count):
        super(Tree, self).__init__()
        self.root = None
        self.node_count =0

    def Insert_nodes(self):
    
        # if root empty insert root
        if self.root == None:
            self.node_count == 1
            self.root = Nodes(self, node_count, nodes[0])

        #insert remaining nodes in tree
        current = self.root
        for node in nodes[1:]:
            if node == '':
                continue

            child_vals = [c.value for c in current.children]
            print("node" + str(node))
            if node not in child_vals:
                self.node_count == 1
               # print("appending" + node)
                current.children.append(node(self, node_count,node))
            child_vals = [c.value for c in current.children]

            for cnum in range(0,len(current.children)):
                if current.children[cnum].value == node:
                    current = current.children[cnum]
                    break
           # print (len(self.root.children)

        return

    def print_tree(self):

        if self.root is None:
            print ("Tree is not built")
            return

        print (self.root.value + "\n")
        queue = [self.root]

        while len(queue) > 0:
            current = queue[0]
            has_child = 0
            for child in current.children:
                print(child.value + " ")
                queue.append(child)
                has_child = 1
            if has_child:
                print("\n")
                has_child = 1
            if len(queue) > 1:
                queue = queue[1:]
            print (" length of queue" + str(len(queue)))
            print ("\n")

        return
        
        

def read_input():
    if len(sys.argv) < 2:
        print ("file expect name of input file")
        sys.exit(1)

    try:
        in_filename = sys.argv[1]
        file = open(in_filename, 'r')
    except:
        print ("file not exist")
        sys.exit(1)

    is_item =1
    line = ''
    path = []
    CH = Tree()
    for line in file.readline():
        if line.split(' ') == '':
            continue

        if is_item:
            #line is item
            item= line.strip().split(' ')
            is_item = 0
        else:
            #line is path
            path = line.strip().split(' ')
            CH = Tree.Insert_nodes(path)
            is_item = 1

    return CH
    CH.print_tree()

    
def main():
	CH = read_input()

if __name__ == '__main__':
	main()