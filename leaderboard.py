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


    def delete(self, key, player):
        self.root = self.deleter(self.root, key, player)            # Ensures root node is reassigned if root is being deleted


    def deleter(self, node, key, player):
        # helper for delete
        # Checks child nodes and reassigns after deletion if necessary

        if Node == None:
            return None
        
        # Moves through left and right subtrees
        if key < node.key:
            node.left = self.deleter(node.left, key, player)       
        
        elif key > node.key:
            node.right = self.deleter(node.right, key, player)
        
        else:
        # Check that player selected is actually the player intended to delete
            if node.player != player:
                node.right = self.deleter(node.right, key, player)
                return node
            
            # 1st Option: Deleted node has no child (leaf) nodes
            if node.left == None and node.right == None:
                return None
            
            # 2nd Option: 1 child node
            if node.left == None:
                return node.right                                               # If child node is to the right
            
            if node.right == None:                                              # If child node is to the left
                return node.left
            
            # 3rd Option: Both child nodes
            succ = self.min_value_node(node.right)
            
            node.key = succ.key                                                 # Replace current node with successor's data
            node.player = succ.player

            node.right = self.deleter(node.right, succ.key, succ.player)        # Delete successor node
        return node
    

    def min_value_node(self, node):
        # Helper function for deleter
        # Finds the smallest value in a subtree

        current = node

        while current.left != None:                                             # Traverse through subtree until smallest value is found
            current = current.left

        return current

    
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

    
    def delete_player(self, name):
        # Remove a player from leaderboard and all stat BSTs

        if name not in self.players:                    # Check that player still exists
            print("Player not found (Names are case sensitive). ")
            return
        
        player = self.players[name]

        # Remove players from every stat tree
        self.pts_tree.delete(player.points, player)     
        self.ast_tree.delete(player.assists, player)
        self.reb_tree.delete(player.rebounds, player)
        self.stl_tree.delete(player.steals, player)
        self.blk_tree.delete(player.blocks, player)

        del self.players[name]                          # Remove player name from dictionary

        print(f" {name} removed from leaderboard.")     
        
    
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


    def get_tree_by_stat(self, stat):
        # Helper for range_of_players to select the correct stat tree
        stat = stat.lower()

        if stat == "points":
            return self.pts_tree
        elif stat == "assists":
            return self.ast_tree
        elif stat == "rebounds":
            return self.reb_tree
        elif stat == "steals":
            return self.stl_tree
        elif stat == "blocks":
            return self.blk_tree
        else:
            return None


# Main Interaction Hub

if __name__ == "__main__":

    lb = Leaderboard()

# Load 10 default players immediately
    given_players = [
        ("LeBron James", 26, 5, 8, 1, 2),
        ("Anthony Edwards", 38, 5, 7, 3, 4), 
        ("Stephen Curry", 27, 6, 2, 2, 1),
        ("Shai Gilgeous-Alexander", 30, 4, 3, 1, 2),
        ("Victor Wembanyama", 26, 3, 10, 1, 7),
        ("Giannis Antetokounmpo", 31, 6, 11, 1, 2),
        ("Luka Doncic", 29, 9, 8, 1, 0),
        ("Joel Embiid", 34, 4, 10, 1, 2),
        ("Kevin Durant", 24, 6, 7, 3, 5),
        ("Nikola Jokic", 34, 8, 10, 2, 5)
    ]
    
    for name, pts, ast, reb, stl, blk in given_players:
        lb.add_player(name, pts, ast, reb, stl, blk)

    def check_int(question):
            # Ensures that given input is an integer

            while True:
                k_input = input(question)

                try:
                    return int(k_input)
                
                except ValueError:
                    print("Please try again: ")


    while True:
        # Program loop

        print("\n ====== Leaderboard Menu ======")
        print("1. Add Player")
        print("2. Show Leaderboard")
        print("3. Select Stat Range")
        print("4. Delete player")
        print("5. Exit Leaderboard")

        option = input("\n Please select any option: ")

        if option == "1":
            # Add a player to the leaderboard
            name = input("\n What's your players name?: ")
            pts = check_int("Points: ")
            ast = check_int("Asists: ")
            reb = check_int("Rebounds: ")
            stl = check_int("Steals: ")
            blk = check_int("Blocks: ")

            lb.add_player(name, pts, ast, reb, stl, blk)


        elif option == "2": 
            # Display current leaderboard
            k = check_int("\n How many of the top players would you like to see?: ")
            print(f"\n Here are the top {k} players in each category:")
            lb.display_all_categories(k)


        elif option == "3":
            # Range of players in a specific stat
            stat = input("\n Please select a statistic (Points, Assists, Rebounds, Steals, Blocks): ").lower()
            
            tree = lb.get_tree_by_stat(stat)

            # Checks that given tree input is valid
            if tree == None:
                stat = input("Please try again: (points, assists, rebounds, steals, blocks) ")
                tree = lb.get_tree_by_stat(stat)
            
            low = check_int("Minimum value: ")
            high = check_int("Maximum value: ")

            # Flip low and high if low > high
            if low > high:
                tmp = high
                high = low
                low = tmp

            players = lb.range_of_players(tree, low, high)
            print(f"\n Players with {stat} between {low} and {high}: ")

            # Print players in the given range
            for p in players:
                player_stat = getattr(p, stat)
                print(f" {p.name}: {player_stat}:")

        elif option == "4":
            # Delete a player from leaderboard
            name = input("\n Please enter player name to delete: ")
            lb.delete_player(name)

        elif option == "5":
            # Exit program 
            print("\n Exiting Leaderboard...")
            break

        else:
            # Option not in menu
            option = input("Not an option. Please try again: ")
