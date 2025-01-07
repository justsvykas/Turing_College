from chess import find_victim


def test_minus_col_direction():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "pawn", "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [-4,0]) == None


def test_plus_col_direction():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "pawn", "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [5,0]) == None



def test_minus_row_direction():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "pawn", "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [0,-5]) == None


def test_plus_row_direction():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "pawn", "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [0,5]) == None
