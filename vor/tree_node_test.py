from anytree import SymlinkNode, Node, RenderTree
root = Node('root')
s1 = Node("sub1", parent=root, bar=17)
l = SymlinkNode(s1, parent=root, baz=18)
l0 = Node("l0", parent=l)
print(RenderTree(root))
