# Step 1) Board
# Step 2) Pieces
# Step 3) Turns
# Step 4) Move Pieces on each turn

board = [0] * 8

for i in range(len(board)):
	board[i] = ["  "] * 8
	
# [8 x 8]
# (0, 0) -> a8
def print_board(board):
	for i, row in enumerate(board):
		print(8 - i, end = ": ")
		for j, col in enumerate(row):
			print(col, end = " ")
		print("\n")
	print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2	+ "h")
	

white_pieces_map = {
	"wP": [(6,0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
	"wN": [(7, 1), (7, 6)],
	"wB": [(7, 2), (7, 5)],
	"wR": [(7, 0), (7, 7)],
	"wQ": [(7, 3)],
	"wK": [(7, 4)]
}

black_pieces_map = {
	"bP": [(1,0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
	"bN": [(0, 1), (0, 6)],
	"bB": [(0, 2), (0, 5)],
	"bR": [(0, 0), (0, 7)],
	"bQ": [(0, 3)],
	"bK": [(0, 4)]
}

col_map = {
	"a": 0,
	"b": 1,
	"c": 2,
	"d": 3,
	"e": 4,
	"f": 5,
	"g": 6,
	"h": 7
}

def put_pieces(board):
	# White Pieces
	for piece, squares in white_pieces_map.items():
		for square in squares:
			x, y = square
			board[x][y] = piece
	
	# Black Pieces
	for piece, squares in black_pieces_map.items():
		for square in squares:
			x, y = square
			board[x][y] = piece
			
put_pieces(board)

curr_turn = 1
while(True):
	print_board(board)
	print("")
	
	curr_player = ""
	if curr_turn % 2 == 1:
		curr_player = "White"
	else:
		curr_player = "Black"
	
	curr_turn += 1
	
	print(curr_player + " to move!")
	print("")
	
	starting_square = input("Enter the square whose piece you'd like to play: ")
	start_col, start_rank = starting_square[0], starting_square[1]
	start_y = col_map[start_col]
	start_x = 8 - int(start_rank)
	
	ending_square = input("Enter the square you'd like to move your piece to: ")
	end_col, end_rank = ending_square[0], ending_square[1]
	end_y = col_map[end_col]
	end_x = 8 - int(end_rank)
	
	temp = board[start_x][start_y]
	board[start_x][start_y] = "  "
	board[end_x][end_y] = temp
	
