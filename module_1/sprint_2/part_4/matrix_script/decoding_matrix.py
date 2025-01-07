# If you dont want to input use this instead
# matrix = ["Tsi",r"h%x","i #", "sM ", "$a ", "#t%", "ir!"]
import re

def main():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    matrix = []
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    my_string = matrix_to_string(matrix)
    print(decode(my_string))

def matrix_to_string(matrix):
    transposed_matrix = []
    for new_row in zip(*matrix):
        for s in new_row:
            transposed_matrix.append(s)
    return "".join(transposed_matrix)

def decode(my_string):
    code, part_string = find_begining(my_string)
    my_string = my_string.replace(part_string, "")
    decoded = code
    while code:
        try:
            code, part_string = find_begining(my_string)
        except AttributeError:
            break
        my_string = my_string.replace(part_string, "")
        decoded = f"{decoded} {code}"
    return decoded + my_string

def find_begining(string):
    my_match = re.match(r"(^[\W]*([\w]+))", string)
    return my_match.group(2), my_match.group(1)

# use if __name__ == "__main__": main() for tests
# Not using it here as requirement for exercise is no if's
main()
