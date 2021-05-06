import networkx as nx
import matplotlib.pyplot as plt
import random
import PySide2
import os


class RedBlackTreeNode:
    """definition of red black tree node

    Attributes:
        val    : value of node
        color  : color of node, 'r' for red node, 'b' for black node
        left   : left child node
        right  : right child node
        parent : parent node
    """
    def __init__(self, x: int, color: str, left=None, right=None, parent=None) -> None:
        self.val = x
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    """definition of red black tree

    Attributes:
        root : root of red black tree
    """
    def __init__(self) -> None:
        self.root = None