import io
import sys

sys.stdin = io.StringIO("""3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
""")


def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == "__main__":
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep="\n")
