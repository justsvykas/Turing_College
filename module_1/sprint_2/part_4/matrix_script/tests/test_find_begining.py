from decoding_matrix import find_begining

def test_find_begining_basic():
    assert find_begining("This$#is% Matrix#  %!") == ("This", "This")

def test_find_begining_with_extra_nonalphanumeric_at_begining():
    assert find_begining("!@#@#This$#is% Matrix#  %!") == ("This", "!@#@#This")