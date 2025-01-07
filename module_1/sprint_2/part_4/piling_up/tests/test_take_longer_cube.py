from piling_up import take_longer_cube


def test_longer_cube_function_basic():
    assert take_longer_cube(["1", "2", "3", "4"]) == (4, ["1", "2", "3"])
    assert take_longer_cube(["4", "2", "3", "1"]) == (4, ["2", "3", "1"])

def test_longer_cube_from_one_cube():
    assert take_longer_cube(["1"]) == (1, [])