class BinaryTreeNode:
    """ binary tree node

    The definition of binary tree's node.
    This class overloads the greater than, less than, and equal operators.

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

    def __eq__(self, other) -> bool: return self.val == other.val
    def __lt__(self, other) -> bool: return self.val < other.val
    def __gt__(self, other) -> bool: return self.val > other.val


class BinarySearchTree:
    """binary search tree node

    The definition of binary search tree and it's methods

    Attributes:
        root : the root of the tree
    """
    def __init__(self) -> None:
        self.root = None

    def treeSearch(self, key: int) -> bool:
        """search key in the tree

        Args:
            key : the value input to search

        Returns:
            whether key is in the tree
        """
        return self.__treeSearch(self.root, key)

    def __treeSearch(self, root: BinaryTreeNode, key: int) -> bool:
        """private method of searching if key in the input subtree (backtracking version)

        Args:
            root: the root of the target tree
            key : the value input to search

        Returns:
            whether key is in the tree
        """
        if root == None: return False
        if root.val == key: return True
        return self.treeSearch(root.left, key) or self.treeSearch(root.right, key)

    def __iterativeTreeSearch(self, root: BinaryTreeNode, key: int) -> bool:
        """private method of searching if key in the input subtree (iterative version)

        Args:
            root: the root of the target tree
            key : the value input to search

        Returns:
            whether key is in the tree
        """
        while root != None:
            if root.val == key: return True
            elif root.val < key: root = root.right
            else: root = root.left
        return False

    def treeMinimum(self) -> int:
        """find the minimum value in tree

        Returns:
            the minimum value
        """
        return self.__treeMinimum(self.root).val

    def __treeMinimum(self, root: BinaryTreeNode) -> BinaryTreeNode:
        """private method find the minimum value in the input subtree

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
        """private method find the maxinum value in the input subtree

        Returns:
            the node with maxinum value
        """
        while root.right != None:
            root = root.right
        return root  

    def treeInsert(self, key: int) -> None:
        pass

    def treeDelete(self, key: int) -> None:
        pass

    def __transplant(self) -> None:
        pass

    def __eq__(self, other) -> bool: return self.__cmp_tree(self.root, other.root)

    def __cmp_tree(self, root1: BinaryTreeNode, root2: BinaryTreeNode) -> bool:
        """private method of comparing 2 input subtree

        Args:
            root1 : first input subtree
            root2 : second input subtree

        Returns:
            whether 2 input trees are equal
        """
        if root1 == None and root2 == None: return True
        elif root1 == None or root2 == None: return False
        return root1 == root2 and self.__cmp_tree(root1.left, root2.left) and self.__cmp_tree(root1.right, root2.right)