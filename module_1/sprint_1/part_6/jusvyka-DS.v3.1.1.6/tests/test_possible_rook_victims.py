from chess import possible_rook_victims


def test_rook_with_three_victims():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "bishop", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": "queen", "c": None, "d": "rook", "e": "pawn", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_rook_victims(board, "d5") == {"pawn e5", "bishop d2", "queen b5"}


def test_rook_with_zero_victims():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_rook_victims(board, "d5") == set()


def test_rook_with_edge_victim():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "rook", "e": None, "f": None, "g": None, "h": "pawn"},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_rook_victims(board, "d5") == {"pawn h5"}


def test_rook_multiple_victims_in_row():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "rook", "e": "pawn", "f": "pawn", "g": "pawn", "h": "pawn"},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert possible_rook_victims(board, "d5") == {"pawn e5"}


def test_rook_multiple_victims_in_every_direction():
    board = [{"a": None, "b": None, "c": None, "d": "bishop", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": "pawn", "d": "bishop", "e": "pawn", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": "pawn", "d": None, "e": "pawn", "f": "pawn", "g": None, "h": None},
            {"a": "queen", "b": None, "c": None, "d": "rook", "e": "pawn", "f": "pawn", "g": "pawn", "h": "pawn"},
            {"a": None, "b": None, "c": "pawn", "d": None, "e": "pawn", "f": "pawn", "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "king", "e": "pawn", "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": "king", "e": None, "f": None, "g": None, "h": None}]

    assert possible_rook_victims(board, "d5") == {"pawn e5", "bishop d3", "queen a5", "king d7"}
