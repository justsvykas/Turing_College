from chess import find_victim


def test_multiple_victims_in_row():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": "bishop", "c": "pawn", "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [-1,0]) == ("pawn", "c", 5)


def test_multiple_distractions():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": "knight", "f": None, "g": None, "h": None},
            {"a": None, "b": "bishop", "c": None, "d": "knight", "e": None, "f": "knight", "g": None, "h": None},
            {"a": "bishop", "b": "pawn", "c": "knight", "d": "rook", "e": "knight", "f": None, "g": None, "h": None},
            {"a": None, "b": "queen", "c": None, "d": "knight", "e": "knight", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert find_victim(board, "d5", [-2,0]) == ("pawn", "b", 5)
