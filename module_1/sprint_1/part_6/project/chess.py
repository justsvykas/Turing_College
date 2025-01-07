import sys

# Notes: mock funkcija pytests.
# Notes: pytests use only 1 assert
# Dnske quant future prospects
# Quants as galeciau panaudoti matematikos zinias

def main():
    board = initialize_board()
    # Update board with white figure
    print_white_instructions()
    user_white_input = ask_for_input("white")
    board = update_board_with_white(board, user_white_input)
    # update board with black figures
    print_black_instructions()
    board = update_board_with_black(board)
    # print possible victims
    print_possible_victims(board, user_white_input)


def initialize_board(size=8):
    """
    Creates a list representing the chessboard, where each element is dict and represents one row on chess board (1 to 8) 
    and each key are columns of chess board ('a' to 'h'), whereas values represent whats in the position.
    """
    return [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None} for _ in range(size)]


def print_white_instructions():
    print("Choose your champion - it can either be 'knight' or 'rook'")
    print("Choose your position on chess board: eg. 'a5'")
    print("Your answer should be provided in similar fashion as this eg. 'knight a5'")


def print_black_instructions():
    print("Now provide black figures one by one.")
    print("Your answer should be provided in similar fashion as this eg. 'bishop a5'")
    print("You can choose up to 16 enemies or write 'done' when difficulty pleases you")


def ask_for_input(color):
    done = False
    while not done:
        try:
            user_input = input("Choose wisely: ").strip().lower()
        except EOFError:
            sys.exit("\nThank you for using the program")
        done = check_user_input(user_input, color)
    return user_input


def check_user_input(user_input, color):
    if len(user_input.split()) == 1:
        check_for_quit(user_input)
        return check_for_done(user_input, color)
    elif len(user_input.split()) == 2:
        if check_for_valid_figures(user_input, color):
            return check_for_valid_coordinates(user_input.split()[1])
        else:
            return False
    else:
        print("Invalid number of arguments")
        return False


def check_for_quit(user_input):
    if user_input == "quit":
        sys.exit("Exiting the program")


def check_for_done(user_input, color):
    if color == "black" and user_input == "done":
        return True
    else:
        print("Invalid number of arguments")
        return False


def check_for_valid_figures(user_input, color):
    if color == "white" and user_input.split()[0] in ["knight","rook"]:
        return True
    elif user_input.split()[0] in ["knight", "rook", "pawn", "king", "queen", "bishop"]:
        return True
    else:
        print("Invalid chess figure")
        return False


def check_for_valid_coordinates(coordinates):
    if len(list(coordinates)) == 2:
        try:
            if int(coordinates[1])-1 in range(8) and coordinates[0] in list("abcdefgh"):
                return True
        except(ValueError):
            pass
    print("Invalid coordinates")
    return False


def update_board_with_white(board, data):
    while True:
        try:
            return update_board(board, data)
        except UserWarning as warning:
            print(warning)
            data = input("Choose wisely: ").strip().lower()


def process_data(data):
    figure, position = data.split()
    col = list(position)[0]
    row = int(list(position)[1])
    return figure, position, col, row


def update_board(board, data):
    figure, position, col, row = process_data(data)
    if board[row-1][col] is not None:
        raise UserWarning(f"Figure already exists at {position}, choose another")
    else:
        board[row-1][col] = figure
        print(f"Figure {figure} was succesfully added to position {position}")
        return board


def update_board_with_black(board):
    figure_number = 0
    done = False
    chess_set = ["king", "queen", "knight", "knight", "bishop", "bishop", "rook", "rook",
           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
    while not done:
        try:
            board, done, figure_number, chess_set = add_one_black_figure(board, ask_for_input("black"), figure_number, chess_set)
        except UserWarning as warning:
            print(warning)
            continue
    return board


def add_one_black_figure(board, user_input, figure_number, chess_set):
    if user_input == "done" and figure_number == 0:
        print("Input at least one black figure before inputting 'done'")
        return board, False, 0, chess_set
    elif user_input == "done":
        return board, True, figure_number, chess_set
    elif user_input.split()[0] in chess_set:
        if figure_number == 15:
            print("16th enemy adding to the board . . .")
            updated_board = update_board(board, user_input)
            chess_set.remove(user_input.split()[0])
            return updated_board, True, figure_number+1, chess_set
        else:
            updated_board = update_board(board, user_input)
            chess_set.remove(user_input.split()[0])
            return updated_board, False, figure_number+1, chess_set
    else:
        print(f"{user_input.split()[0]} can't be added. Choose from remaining pieces in a set {chess_set}")
        return board, False, figure_number, chess_set


def print_possible_victims(board, user_input):
    victims = possible_victims(board, user_input)
    if victims is None:
        print("No possible targets")
    else:
        print(f"Possible victims: {', '.join(f"'{victim}'" for victim in victims)}")


def possible_victims(board, white):
    figure, position = white.split()
    if figure == "knight":
        return possible_knight_victims(board, position)
    elif figure == "rook":
        return possible_rook_victims(board, position)


def possible_knight_victims(board, position):
    knight_attack_pattern = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    victims = set()
    for knight_attack in knight_attack_pattern:
        victim = find_victim(board, position, knight_attack)
        if victim is None:
            continue
        # Galima else 
        elif victim[0] is not None:
            victims.add(str(victim[0] + " " + victim[1] + str(victim[2])))
    return victims


def find_victim(board, position, attack):
    """
    Determine the value at a target position on the board based on the given position and attack direction.

    Parameters:
        board (list): A list representing the chessboard, where each element is dict and represents one row on chess board (1 to 8) 
                      and each key are columns of chess board ('a' to 'h'), whereas values represent whats in the position
        position (str): The starting position on the board in chess notation (e.g., 'e4').
        attack (tuple): A tuple of two integers representing the attack direction as column and row offsets 
                        (e.g., (-1, 1) for up-left diagonal).

    Returns:
        tuple: A tuple containing the value at the target position, its column letter, and its row number 
               (e.g., ('pawn', 'd', 5)).
        None: If the calculated position is out of bounds.
    """

    row_figure = int(list(position)[1])-1
    col_figure = list(position)[0]
    alphabet_coordinates = list("abcdefgh")
    col_index_figure = alphabet_coordinates.index(col_figure)
    row_victim = row_figure+attack[1]
    if row_victim < 0 or row_victim > 7 or col_index_figure + attack[0] < 0 or col_index_figure + attack[0] > 7:
        return None
    else:
        col_victim = alphabet_coordinates[col_index_figure + attack[0]]
        return (board[row_victim][col_victim], col_victim, (row_victim+1))


def possible_rook_victims(board, position):
    rook_attack_directions = [[1,0], [0,-1], [-1,0], [0,1]]
    victims = set()
    for rook_direction in rook_attack_directions:
        new_direction = rook_direction
        while True:
            victim = find_victim(board, position, new_direction)
            if victim is None:
                break
            elif victim[0] is not None:
                victims.add(str(victim[0] + " " + victim[1] + str(victim[2])))
                break
            else:
                new_direction = [a + b for a,b in zip(new_direction, rook_direction)]
    return victims


if __name__ == "__main__":
    main()


# My assumptions:
# - if user inputs figure in the same position - ignore input and ask for another.
# - If user inputs more specific figures than in chess set, eg. second king - prompt the user for different figure.
