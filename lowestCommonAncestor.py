import TreeNode


# 236. 二叉树的最近公共祖先
# 1581. 面试题68 - II. 二叉树的最近公共祖先
# 思路：
# 深度优先递归，找到P或Q就直接返回本身节点，若到底还没找到就返回None
# 若左右两边均不为None，则当前节点为解
# 若只找到一个节点（如只找到P，未找到Q）则另一节点一定为此节点的子节点，找到的节点为解
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
class LowestCommonAncestorSolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        right = self.lowestCommonAncestor(root.right, p, q)
        left = self.lowestCommonAncestor(root.left, p, q)
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
