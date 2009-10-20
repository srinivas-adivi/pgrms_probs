#! /usr/bin/python

def make_node(value, left=None, right=None):
    """
    >>> make_node(1, make_node(2, make_node(4), None), make_node(3, None, make_node(5)))
    [1, [2, [4, None, None], None], [3, None, [5, None, None]]]
    """
    return [value, left, right]

def getvalue(node):
    """
    >>> node = make_node(1, make_node(2, make_node(4), None), make_node(3, None, make_node(5)))
    >>> getvalue(node[1])
    2
    >>> getvalue(node[1][1])
    4
    >>> getvalue(node[2][1])
    """
    if node: return node[0]

def leftchild(node):
    """
    >>> node = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> leftchild(node)
    [2, [4, None, None], [5, None, None]]
    >>> leftchild(node[1])
    [4, None, None]
    >>> leftchild(node[2])
    [6, None, None]
    """
    if node: return node[1]

def rightchild(node):
    """
    >>> node = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> rightchild(node)
    [3, [6, None, None], [7, None, None]]
    >>> rightchild(node[1])
    [5, None, None]
    >>> rightchild(node[2])
    [7, None, None]
    """
    if node: return node[2]
 
def is_leaf(node):
    """
    >>> node = make_node(1, make_node(2, make_node(4), None), make_node(3))
    >>> is_leaf(node[1])
    False
    >>> is_leaf(node[2])
    True
    """
    return leftchild(node) is None and rightchild(node) is None

def leafcount(root):
    """
    >>> root = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> leafcount(root)
    4
    >>> root = make_node(1, make_node(2), make_node(3))
    >>> leafcount(root)
    2
    """
    if root is None:
        return 0
    elif is_leaf(root):
        return 1
    else:
        return leafcount(leftchild(root)) + leafcount(rightchild(root))

def treeheight(root):
    """
    >>> treeheight(make_node(1))
    1
    >>> a = make_node(1, make_node(2), make_node(3, make_node(4), None))
    >>> treeheight(a)
    3
    >>> treeheight(leftchild(a))
    1
    >>> treeheight(rightchild(a))
    2
    """
    if root is None:
        return 0
    elif is_leaf(root):
        return 1
    else:
       return max(treeheight(leftchild(root))+1, treeheight(rightchild(root))+1)

def maximum(a, b):
    return a < b and b or a

def inorder_traversal(root):
    """
    >>> root = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> inorder_traversal(root)
    [1, 2, 4, 5, 3, 6, 7]
    """
    if root is None:
        return []
    else:
        return [getvalue(root)] + inorder_traversal(leftchild(root)) +                                     inorder_traversal(rightchild(root))

def preorder_traversal(root):
    """
    >>> root = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> preorder_traversal(root)
    [4, 2, 5, 1, 6, 3, 7]
    """
    if root is None:
        return []
    else:
        return preorder_traversal(leftchild(root)) + [getvalue(root)] +                preorder_traversal(rightchild(root))

def postorder_traversal(root):
    """
    >>> root = make_node(1, make_node(2, make_node(4), make_node(5)), make_node(3, make_node(6), make_node(7)))
    >>> postorder_traversal(root)
    [7, 6, 3, 5, 4, 2, 1]
    """
    if root is None:
        return []
    else:
        return postorder_traversal(rightchild(root)) +postorder_traversal(leftchild(root)) + [getvalue(root)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()    
    
    
