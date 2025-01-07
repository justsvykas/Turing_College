import sys
import io

sys.stdin = io.StringIO("2\n6\n4 3 2 1 2 3 4\n3\n1 3 2")

lines = sys.stdin.read().splitlines()

for index in range(1,len(lines),2):
    cubes = lines[index+1].split()
    print(cubes)