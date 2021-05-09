import networkx as nx
import matplotlib.pyplot as plt
import random
import PySide2
import os


class BinarySearchTree:
    """binary search tree node

    The definition of binary search tree and it's methods,
    Overloads equal operator to compare tree.

    Attributes:
        root : the root of the tree
        fig  : default figure value
    """


    class BinaryTreeNode:
        """inner class of binary tree node

        The definition of binary tree's node.

        Attributes:
            val   : value of the node with the type of int
            left  : left child node
            right : right child node
            parent: parent node
        """
        def __init__(self, x: int, left=None, right=None, parent=None) -> None:
            self.val = x
            self.left = left
            self.right = right
            self.parent = parent


    def __init__(self) -> None:
        self.root = None
        self.fig = plt.figure(figsize=(15, 10))
        plt.ion()

    def __del__(self) -> None:
        plt.ioff()

    def treeSearch(self, key: int) -> bool:
        """search key in the tree

        Args:
            key : the value input to search

        Returns:
            whether key is in the tree
        """
        return self.__treeSearch(self.root, key) != None

    def __treeSearch(self, root: BinaryTreeNode, key: int) -> BinaryTreeNode:
        """private method of searching target node in the input subtree (backtracking version)

        Args:
            root: the root of the target tree
            key : the value input to search

        Returns:
            if key in the subtree return the node,
            else return None
        """
        if root == None or root.val == key: return root
        if root.val < key: return self.__treeSearch(root.right, key)
        else: return self.__treeSearch(root.left, key)

    def __iterativeTreeSearch(self, root: BinaryTreeNode, key: int) -> BinaryTreeNode:
        """private method of searching target node in the input subtree (iterative version)

        Args:
            root: the root of the target tree
            key : the value input to search

        Returns:
            if key in the subtree return the node,
            else return None
        """
        while root != None:
            if root.val == key: return root
            elif root.val < key: root = root.right
            else: root = root.left
        return None

    def treeMinimum(self) -> int:
        """find the minimum value in tree

        Returns:
            the minimum value
        """
        return self.__treeMinimum(self.root).val

    def __treeMinimum(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """private method find the minimum node in the input subtree

        Returns:
            the node with minimum value
        """
        while root.left != None:
            root = root.left
        return root

    def treeMaxinum(self) -> int:
        """find the maxinum value in the tree

        Returns:
            the maximum value
        """
        return self.__treeMaxinum(self.root).val

    def __treeMaxinum(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """private method find the maxinum node in the input subtree

        Returns:
            the node with maxinum value
        """
        while root.right != None:
            root = root.right
        return root  

    def treeInsert(self, key: int) -> None:
        """insert node with value of key to current tree.

        Args:  
            key : the value of new tree node.
        """
        if self.treeSearch(key): return # if key has already in this tree, we do nothing

        newNode = self.BinaryTreeNode(x=key)
        if self.root == None:
            self.root = newNode
            return

        cur = self.root
        pre = None
        while cur != None:
            if cur.val < key:
                pre, cur = cur, cur.right
            elif cur.val > key:
                pre, cur = cur, cur.left

        if key < pre.val: pre.left = newNode
        elif key > pre.val: pre.right = newNode
        newNode.parent = pre

    def treeDelete(self, key: int) -> None:
        """delete the node with value of key in the tree

        Args: 
            key : the target key to delete
        """
        target = self.__treeSearch(self.root, key)
        if not target: return # if key is not in the tree, we do nothing
        
        if target.left == None: self.__transplant(target, target.right)
        elif target.right == None: self.__transplant(target, target.left)
        else:
            tmp = self.__treeMinimum(target.right)
            if tmp.parent != target:
                self.__transplant(tmp, tmp.right)
                tmp.right = target.right
                tmp.right.parent = tmp
            self.__transplant(target, tmp)
            tmp.left = target.left
            tmp.left.parent = tmp

    def __transplant(self, u: BinaryTreeNode, v: BinaryTreeNode) -> None:
        """use subtree v to take u's position

        Args:
            u : input tree node
            v : input tree node
        """
        if u.parent == None: self.root = v
        elif u == u.parent.left: u.parent.left = v
        elif u == u.parent.right: u.parent.right = v
        if v != None: v.parent = u.parent

    def __eq__(self, other) -> bool: return self.__cmp_trees(self.root, other.root)

    def __cmp_trees(self, root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
        """private method of comparing 2 input subtree

        Args:
            root1 : first input subtree
            root2 : second input subtree

        Returns:
            whether 2 input trees are equal
        """
        if root1 == None and root2 == None: return True
        elif root1 == None or root2 == None: return False
        return root1.val == root2.val and self.__cmp_trees(root1.left, root2.left) and self.__cmp_trees(root1.right, root2.right)

    def __create_graph(self, G, root: BinaryTreeNode, pos={}, x=0, y=0, layer=1) -> None:
        """add edge for root node

        if root has left child, add edge between root and left child, 
        elif root has right child, add edge between root and right child.
        the y position is calulated by the layer of itself,
        the x position decays with the rate of 0.5.

        Args:
            G     : graph value
            root  : current node
            pos   : position dict
            x     : the x position of node root
            y     : the y position of node root
            layer : the layer of node root
        """
        pos[root.val] = (x, y)
        if root == self.root and root.left == None and root.right == None:
            G.add_node(root.val)
        else:
            if root.left:
                G.add_edge(root.val, root.left.val)
                l_x, l_y = x - 1 / 2 ** layer, y - 1
                l_layer = layer + 1
                self.__create_graph(G, root.left, x=l_x, y=l_y, pos=pos, layer=l_layer)
            if root.right:
                G.add_edge(root.val, root.right.val)
                r_x, r_y = x + 1 / 2 ** layer, y - 1
                r_layer = layer + 1
                self.__create_graph(G, root.right, x=r_x, y=r_y, pos=pos, layer=r_layer)
        return (G, pos)

    def __drawTree(self, root: BinaryTreeNode) -> None:
        """draw the subtree

        Args:
            root : the root of input subtree
        """
        plt.cla()
        plt.clf()
        graph = nx.DiGraph()
        graph, pos = self.__create_graph(graph, root)
        ax = self.fig.add_subplot()
        nx.draw_networkx(graph, pos, ax=ax, node_size=300)
        plt.pause(0.5)
        
    def drawTree(self) -> None:
        """draw the whole binary tree while self.root is not None.
        """
        if self.root: self.__drawTree(self.root)



def test():
    """the following code show the process of adding 10 nodes and delete them by step.
    """
    dirname = os.path.dirname(PySide2.__file__) 
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    tree = BinarySearchTree()
    keys = []
    for _ in range(10):
        tmp = random.randint(1, 100)
        keys.append(tmp)
        tree.treeInsert(tmp)
        tree.drawTree()
    random.shuffle(keys)
    for each in keys:
        tree.treeDelete(each)
        tree.drawTree()
    del tree

test()