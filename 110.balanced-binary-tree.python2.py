# @leet start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def checkHeight(node):
            if not node:
                return 0  # Высота пустого дерева = 0

            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1  # Левое поддерево несбалансировано

            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1  # Правое поддерево несбалансировано

            if abs(left_height - right_height) > 1:
                return -1  # Текущий узел несбалансирован

            return max(left_height, right_height) + 1  # Возвращаем высоту текущего узла

        return checkHeight(root) != -1


# @leet end
