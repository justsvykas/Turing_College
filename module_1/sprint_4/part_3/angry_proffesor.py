from itertools import filterfalse


def angryProfessor(k, a):
    print(list(filterfalse(lambda x: x > 0, a)))


# Example call
angryProfessor(3, [-1, -3, 4, 2])
