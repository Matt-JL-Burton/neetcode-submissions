class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        visited_nodes = []
        visited_nodes_set = set()

        def dfs(current_node):
            if not current_node:
                return False

            if dfs(current_node.left):
                return True

            visited_nodes.append(current_node.val)
            if len(visited_nodes) == k:
                return True

            if dfs(current_node.right):
                return True
            
            return False
            
        dfs(root)
        return visited_nodes[-1]