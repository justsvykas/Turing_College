from decoding_matrix import matrix_to_string


def test_matrix_to_string_numbers():
    my_matrix = ["123", "456", "789"]
    assert matrix_to_string(my_matrix) == "147258369"

def test_matrix_to_string_basic():
    my_matrix = ["Tsi",r"h%x","i #", "sM ", "$a ", "#t%", "ir!"]
    assert matrix_to_string(my_matrix) == "This$#is% Matrix#  %!"
