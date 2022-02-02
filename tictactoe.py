import random

X = "X"
O = "O"
EMPTY = "*"

# Bigger board sizes are less likely
RANDOM_SIZES = [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Type aliases
Player = str
Board = list[list]
Coords = tuple[int, int]


def create_board(size: int) -> Board:
    """
    Create an empty game board.

    :param size: the size of the board
    :return: the initialized board
    """
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(EMPTY)
        board.append(row)
    return board


def check_rows(board: Board, player: Player) -> bool:
    """
    Check if a player has won in one of the rows

    :param board: the board to check
    :param player: the player to check if won
    :return: if the player has won
    """
    for row in board:
        if row.count(player) == len(row):
            return True
    return False


def check_columns(board: Board, player: Player) -> bool:
    """
    Check if a player has won in one of the columns

    :param board: the board to check
    :param player: the player to check if won
    :return: if the player has won
    """
    for i, row in enumerate(board):
        marks = 0
        for j in range(len(row)):
            marks += board[j][i] == player
        if marks == len(row):
            return True
    return False


def check_diagonals(board: Board, player: Player) -> bool:
    """
    Check if a player has won in one of the diagonals

    :param board: the board to check
    :param player: the player to check if won
    :return: if the player has won
    """
    diagonal_one = board[0][0] == player == board[1][1] == board[2][2]
    diagonal_two = board[0][2] == player == board[1][1] == board[2][0]
    return diagonal_one or diagonal_two


def won(player: Player, board: Board) -> bool:
    """
    Check if a player has won in any direction

    :param player: the player to check if won
    :param board: the board to check
    :return: if the player has won
    """
    return check_rows(board, player) or check_columns(board, player) or check_diagonals(board, player)


def update_board(board: Board, player: Player, coords: Coords):
    """
    Updates a game board with a given player's move.

    :param board: the board to update
    :param player: the player that made the move
    :param coords: the coordinates (row, column) of the player's move
    """
    board[coords[0]][coords[1]] = player


def get_move(player: Player) -> Coords:
    """
    Asks a player for their next move.

    :param player: the player whose turn it is to play
    :return: the coordinates the player chose
    """
    row, col = input(f"{player}'s move: ").split()
    return int(row), int(col)


def show_board(board: Board):
    """
    Print the current state of the game board.

    :param board: the board to display
    """
    for row in board:
        print(" ".join(row))


def show_winner(player: Player):
    """
    Print an endgame message with the name of the winner.

    :param player: the player who won
    """
    print(f"\nAnd the WINNER is: .....\n!!!!!!!!!!!! {player} !!!!!!!!!!!!")


def switch_player(current_player: Player) -> Player:
    """
    Determine whose turn it is next.

    :param current_player: the player who played last
    :return: the player who will play next
    """
    return X if current_player == O else O


def check_empty_coords(board: Board, coords: Coords) -> bool:
    """
    Check if the board is empty in the given coordinates

    :param board: the board to check
    :param coords: pair of coordinates (row, column)
    :return: if the tile is empty
    """
    return board[coords[0]][coords[1]] == EMPTY


def check_draw(board: Board) -> bool:
    """
    Check if the board has no more empty tiles, resulting in a draw

    :param board: the board to check
    :return: if the game ended in a draw
    """
    for row in board:
        if row.count(EMPTY) > 0:
            return False
    return True


def play_game(board_size: int = None):
    """
    Play a game of Tic-Tac-Toe.

    :param board_size: the size of the game board. randomized by default.
    """
    if not board_size:
        board_size = random.choice(RANDOM_SIZES)
    board = create_board(board_size)
    show_board(board)
    current_player = X
    game_won = False
    while not game_won:
        coordinates = get_move(current_player)
        empty_coords = check_empty_coords(board, coordinates)
        if(not empty_coords):
            print('Spot taken! Choose another')
            continue
        update_board(board, current_player, coordinates)
        show_board(board)
        game_won = won(current_player, board)
        if not game_won:
            if(check_draw(board)):
                return print('Its a draw!')
            current_player = switch_player(current_player)
    show_winner(current_player)


if __name__ == '__main__':
    # play_game()
    play_game(3)