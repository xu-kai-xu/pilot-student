
from multiprocessing.sharedctypes import Value


class TreeNode:
    def __init__(self, name='root', data=None, parent=None, children=None):
        self.name = name
        self.data = data
        
        if parent:
            # 确认parent参数是TreeNode类型
            assert isinstance(parent, TreeNode)
            parent.add_child(self)
        self.parent = parent
        
        self.children = []
        if children:
            for child in children:
                self.add_child(child)
                
    def add_child(self, node):
        # 1. 确认node参数是TreeNode类型
        # 2. 将要加入的子节点的parent属性设为自己
        # 3. 然后将其加入children列表
        assert isinstance(node, TreeNode)
        # 检查重复的 node.name 
        child_name_lst = [child.name for child in self.children]
        if node.name in child_name_lst:
            raise ValueError(f"Node name *{node.name}* has been used! Choose another one name!")

        node.parent = self
        self.children.append(node)
        print (f"add node *{node.name}* as child of  node *{self.name}*!")

    def find_parent(self):
        #print ({self.parent.name: self.parent.data})
        return self.parent

    def find_children(self):
        # child_dict = {}
        # for child in self.children:
        #     child_dict[child.name] = child.data
        # #print(child_dict)
        return self.children

    def find_child(self, name=None, data=None):
        """
        根据子节点的名字和数据查找子节点

        如果没有找到怎么办
        """
        
        child_dict = self.find_children()
        if name:
            for child in child_dict:
                if child.name == name:
                    return child
            else:
                raise ValueError(f"Sorry, no node with the name *{name}*.")
        
        elif data:
            for child in child_dict:
                if child.data == data:
                    return child
            else:
                raise ValueError(f"Sorry, no node with the data *{data}*.")

        else:
            raise ValueError("You should provide attributes of the node to search it.")


    def find_same_tier(self, flatten=False):
        """
        给出一个 node，找出它所有的同层的节点
        flatten：是否将列表展平。
        """
        if self.parent == None:
            return [self]
        parent = self.parent
        sibs = parent.find_siblings(include=True)
        generation = []
        for node in sibs:
            generation.append(node.find_children())
        
        if flatten:
            return [item for sub in generation for item in sub]
        else:
            return generation

    def find_siblings(self, include=True):
        """
        找出相同父节点的所有子节点。
        include：是否包括self节点本身。
        """
        if self.parent == None:
            return [self]
        all_sib = self.find_parent().find_children()
        if include:
            siblings = all_sib
        else:
            siblings = [i for i in all_sib if i != self]
        return siblings

    def find_descendants(self):
        """
        找出所有的后代，包括 child 和所有 child 的 child。
        区分第几代
        当 self.child 返回 None 时结束。

        返回一个字典，字典关键字为代。字典值为包含树节点的列表。
        """
        descendants = {}
        generation = 0
        descendants[generation] = self.find_children()

        while True:
            tmp = []
            for node in descendants[generation]:
                if len(node.find_children()) == 0:
                    continue
                tmp.append(node.find_children())

            if len(tmp) == 0:
                break
            
            descendants[generation + 1] = [item for sublst in tmp for item in sublst]

            generation += 1

        return descendants

    
    def node_tier(self):
        """
        给定一个node，确定他的层级，tier
        """
        tier = 0
        node = self

        while True:
            if node.parent == None:
                return tier
            else:
                node = node.parent
                tier += 1
                

    def find_ancestors(self):
        """
        给定一个节点，找出它的所有祖先节点。
        """
        lst = []
        tmp = self
        while tmp.parent != None:
            ances = tmp.find_parent()
            level = ances.find_siblings()
            lst.append(level)
            tmp = ances
        return lst

    def find_path(self, node):
        """
        计算从 self 到 node 的路径和距离。
        """
        path1 = [self]
        path2 = [node]
        tier1 = self.node_tier()
        tier2 = node.node_tier()
        if tier1 > tier2:
            tmp1 = self
            for i in range(tier1 - tier2):
                path1.append(tmp1.parent)
                tmp1 = tmp1.parent
            tmp2 = node
        elif tier1 < tier2:
            tmp2 = node
            for i in range(tier2 - tier1):
                path2.append(tmp2.parent)
                tmp2 = tmp2.parent
            tmp1 = self
        else:
            tmp1 = self
            tmp2 = node
        
        if tmp1 == tmp2:
            return path1[:-1] + path2[::-1]
        elif tmp1.parent == tmp2.parent:
            path1.append(tmp1.parent)
            return path1 + path2[::-1]
        else:
            while tmp1.parent != tmp2.parent:
                tmp1 = tmp1.parent
                tmp2 = tmp2.parent
                path1.append(tmp1)
                path2.append(tmp2)
            path1.append(tmp1.parent)
            return path1 + path2[::-1]

    def find_distance(self, node):
        return (len(self.find_path(node)) - 1)

    def del_node(self):
        """
        删除一个节点及其所有子节点。
        要删除
        """
        sibs = self.parent.find_children()
        for item in sibs:
            if item.name == self.name:
                sibs.remove(item)
        self.parent = None

    def set_parent(self, node):
        """
        将本节点self的父节点设置为node节点
        """
        assert isinstance(node, TreeNode)
        sibs = self.parent.find_children()
        for item in sibs:
            if item.name == self.name:
                sibs.remove(item)
        self.parent = node
        node.add_child(self)






            
    









