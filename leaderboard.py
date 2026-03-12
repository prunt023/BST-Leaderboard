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


class Leaderboard:
    # Manages all players and each statistic category

    def __init__(self):
        # Each stat becomes it's own BST 
        self.pts_tree = BST()
        self.ast_tree = BST()
        self.reb_tree = BST()
        self.stl_tree = BST()
        self.blk_tree = BST()

        self.players = {}                               # Dictionary for each players name for quick access


    def add_player(self, name, pts, ast, reb, stl, blk):
        # Insert all player stats into corresponding tree

        player = Player(name, pts, ast, reb, stl, blk)

        self.players[name] = player # Add players name into dictionary

        # Player value inserted into each stat tree
        self.pts_tree.insert(pts, player)
        self.ast_tree.insert(ast, player)
        self.reb_tree.insert(reb, player)
        self.stl_tree.insert(stl, player)
        self.blk_tree.insert(blk, player)

    
    def display_all_categories(self,  k):
        # Sets up display for player ranking in each category

        categories = [  
            ("Points", self.pts_tree),                       # Pair each tree with a statistic
            ("Assists", self.ast_tree),
            ("Rebounds", self.reb_tree),
            ("Steals", self.stl_tree),
            ("Blocks", self.blk_tree)
        ]

        for name, tree in categories:
            # Iteration through each category
            result = []
            self.reverse_inOrder(tree.root, result, k)      # Reverse order of traversal so largest values come first
            print(f"Top {k} {name}:")

            for player in result:
                stat = getattr(player, name.lower())        # Print every player name and accompanying stat for each category
                print(f"{player.name}: {stat}")
            print("-" * 20)


    def reverse_inOrder(self, node, result, k):
        # Reverses order of traversal through each tree, making largest values appear first

        if node == None or len(result) >= k:            # Stop if node is empty or k amount of players has been reached
            return
        
        self.reverse_inOrder(node.right, result, k)     # Traverse through right (larger) subtree first
        if len(result) < k:
            result.append(node.player)
        self.reverse_inOrder(node.left, result, k)      # Traverse through left subtree to fill k players if necessary


   def range_of_players(self, tree, low, high):
        # Return all players within a given range 
        result = []

        def in_between(node):
            # Recursive helper for traversal through subtrees
            if node == None:
                return
            
            if low < node.key:                  # Iterate left subtree till reaching the given low
                in_between(node.left)

            if low <= node.key <= high:         # Add all players in between given low and high values
                result.append(node.player)

            if high > node.key:
                in_between(node.right)          # Search right subtree for values that are <= high 

        in_between(tree.root)                   # Start at root

        return result
