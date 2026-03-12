class Player:
    # Define a player and the various statistics

    def __init__(self, name, pts, ast, reb, stl, blk):
        self.name = name
        self.points = pts
        self.assists = ast
        self.rebounds = reb
        self.steals = stl
        self.blocks = blk

        
class Node: 
    def __init__(self, key, player):
        self.key = key
        self.player = player
        self.left = None
        self.right = None
      
# Self is the current BST stat (such as pts, ast, stl, ..) that is being called on
# Key is the specific value you're sorting by (if self is points, key is 39, then player x has 39 points)
# Node is the specific node in the tree during traversal (i.e. a player)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, player):
        # Create first (player) stat tree and insert all remaining stats of the same category in order

        if self.root == None:
            self.root = Node(key, player)
        else:
            self.inserter(self.root, key, player)
            
    def inserter(self, node, key, player):
        # helper for insert
        # Add each entry of a given statistic to the rest of the related tree

        if key < node.key:
            if node.left == None:
                node.left = Node(key, player)           # Add left node if current player has a smaller value of statistic than root player
            else:
                self.inserter(node.left, key, player)   # Continue through the newly added left node
        else:
            if node.right == None:
                node.right = Node(key, player)          # Add right node if current player has a larger value of statistic than root player
            else:
                self.inserter(node.right, key, player)  # Continue through the newly added right node


