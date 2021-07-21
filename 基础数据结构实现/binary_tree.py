
# 二叉树实现

class Node(object):
    """
    节点实现
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree(object):
    """
    二叉树实现
    """
    def __init__(self):
        self.root = None

    def add(self, data):
        """
        添加节点
        :param data: 添加的数据
        :return:
        """
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        queue = list()
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """
        层次遍历（广度遍历）
        :return:
        """
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data, end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder(self, root_node):
        """
        前序遍历 根左右
        :return:
        """
        if root_node is None:
            return
        print(root_node.data, end=" ")
        self.preorder(root_node.left)
        self.preorder(root_node.right)

    def inorder(self, root_node):
        """
        中序遍历 左根右
        :return:
        """
        if root_node is None:
            return
        self.inorder(root_node.left)
        print(root_node.data, end=" ")
        self.inorder(root_node.right)

    def postorder(self, root_node):
        """
        后序遍历 左右根
        :return:
        """
        if root_node is None:
            return
        self.postorder(root_node.left)
        self.postorder(root_node.right)
        print(root_node.data, end=" ")




if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)








