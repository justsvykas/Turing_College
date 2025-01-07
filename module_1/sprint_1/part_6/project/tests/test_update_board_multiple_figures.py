from chess import update_board

def test_input_two_figures():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert update_board(update_board(board, "pawn f8"), "knight a5") == [
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "knight", "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": "pawn", "g": None, "h": None}]


def test_input_four_figures():
    board = [{"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None}]

    assert update_board(update_board(update_board(update_board(board, "queen d5"), "bishop h1"), "pawn f8"), "knight a5") == [
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": "bishop"},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": "knight", "b": None, "c": None, "d": "queen", "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None},
            {"a": None, "b": None, "c": None, "d": None, "e": None, "f": "pawn", "g": None, "h": None}]

