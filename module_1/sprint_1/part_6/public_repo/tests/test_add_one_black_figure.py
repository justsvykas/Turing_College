from chess import add_one_black_figure


def test_user_done():
    chess_set = ["king", "queen", "knight", "knight", "bishop", "bishop", "rook", "rook",
           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert add_one_black_figure(board, "done", 1, chess_set) == (board, True, 1, chess_set)


def test_figure_number():
    chess_set = ["king", "queen", "knight", "knight", "bishop", "bishop", "rook", "rook",
           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
    board = [{"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": "pawn", "h": "pawn"},
            {"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": "pawn", "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert add_one_black_figure(board, "pawn h2", 15, chess_set) == (board, True, 16, chess_set)


def test_add_figure():
    board = [{"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": "pawn", "h": "pawn"},
            {"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}] 
    chess_set = ["king", "queen", "knight", "knight", "bishop", "bishop", "rook", "rook",
           "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]

    assert add_one_black_figure(board, "queen h8", 14, chess_set) == ([
            {"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": "pawn", "h": "pawn"},
            {"a": "pawn", "b": "pawn", "c": "pawn", "d": "pawn", "e": "pawn", "f": "pawn", "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": "queen"}],
            False, 15, chess_set)
