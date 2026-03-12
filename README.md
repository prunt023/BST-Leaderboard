# BST-Leaderboard

Leaderboard BST Structure Reference Guide:

Overview:
	This program is designed to implement a basketball leaderboard using Binary Search Trees, where each player is stored into multiple trees for each statistic.

The stats being tracked are:
Points
Assists
Rebounds
Steals
Blocks

The readily-available tools are:
Player insertion
Displaying the leaderboard
Displaying a range of players
Player deletion

Program Organization:

Player Class:
	This class represents each player with all recorded stats
name = Player name
points = Pts scored
assists = Ast
rebounds  = Reb
steals = Stl
blocks = Blk

Node Class:
	This class represents each node in the BSTs
key = Statistic value for sorting
player = Current player object
left = Left leaf/child node
right = right child node

BST Class:
	This class handles all operations done on a Binary Search Tree
insert:		Insert a player into tree
inserter: 	A helper function recursively designed to add leaf nodes        after root node (player) is inserted

delete: 	Remove a player from tree
deleter: 	A helper function designed to reassign nodes after a node is deleted

min_value_node:	Finds a successor node after deletion

Leaderboard Class:
	This class manages all stat trees and a dictionary for player lookup when deleting.

	Contains trees: 
points tree
assists tree
rebounds tree
steals tree
blocks tree
players (Dictionary for player names)

Program Features:
add_player: 		Adds a player to the leaderboard and all stat trees.

delete_player:	Deletes a player from all stat trees and player dictionaries.

display_all_categories: 	Shows top k players of all stat categories. Uses reverse-inorder traversal to locate players with the highest stat value.

range_of_players: 	Displays a range of players within a specific stat category.

