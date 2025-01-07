import sys
import io

def main():
    lines = sys.stdin.read().splitlines()

    for index in range(1,len(lines),2):
        cubes = lines[index+1].split()
        print(validate_pile_creation(cubes))

def validate_pile_creation(cubes, bottom_cube=None):
    while cubes:
        longer_cube, cubes = take_longer_cube(cubes)  
        if bottom_cube is None or bottom_cube >= longer_cube:
            bottom_cube = longer_cube       
        else:
            return "No"

    return "Yes"

def take_longer_cube(cubes):
    if len(cubes) == 1:
        return int(cubes[0]), []
    left_cube = int(cubes[0])
    right_cube = int(cubes[-1])
    if left_cube >= right_cube:
        longer_cube = cubes.pop(0)
    else:
        longer_cube = cubes.pop()
    return int(longer_cube), cubes

if __name__ == "__main__":
    sys.stdin = io.StringIO("2\n6\n4 3 2 1 2 3 4\n3\n1 3 2")
    main()