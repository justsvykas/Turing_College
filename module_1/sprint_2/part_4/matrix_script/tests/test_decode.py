from decoding_matrix import decode


def test_decode_basic():
    assert decode("This$#is% Matrix#  %!") == "This is Matrix#  %!"

def test_decode_with_begining_char():
    assert decode("@#@#$@This$#is% Matrix#  %!") == "This is Matrix#  %!"