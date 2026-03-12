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

