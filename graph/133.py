"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                # we created the node already, don't need to recreate
                # return the new node
                return oldToNew[node]

            new = Node(node.val)
            oldToNew[node] = new
            for nei in node.neighbors:
                prev_created_new_node = dfs(nei)
                prev_created_new_node.neighbors.append(new)
            return new

        if node == None:
            return None
        return dfs(node)