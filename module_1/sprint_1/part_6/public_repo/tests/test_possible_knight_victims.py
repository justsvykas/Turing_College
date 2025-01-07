from chess import possible_knight_victims

def test_knight_in_middle():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": "pawn", "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": "pawn", "c": None, "d": None, "e": None, "f": "queen", "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": "bishop", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_knight_victims(board, "d5") == {"pawn c3", "pawn b6", "bishop e7", "queen f6"}


def test_knight_in_upper_edge():
    board = [{"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": "pawn", "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": "pawn", "d": None, "e": "bishop", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "None", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "queen", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_knight_victims(board, "d1") == {"pawn b2", "pawn c3", "bishop e3"}


def test_knight_left_lower_corner():
    board = [{"a": "knight", "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": "pawn", "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_knight_victims(board, "a1") == {"pawn c2"}


def test_no_victims():
    board = [{"a": "knight", "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "knight", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_knight_victims(board, "a1") == set()
