class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isSubStructure(A:TreeNode,B:TreeNode) -> bool:
    def recur(A,B):
        if not B:return True
        if not A or A.val != B.val:return False
        return recur(A.left,B.left) and recur(A.right,B.right)
    return bool(A and B) and (recur(A,B) or isSubStructure(A.left, B) or isSubStructure(A.right, B))