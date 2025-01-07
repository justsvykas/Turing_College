import re


matrix = ["Tsi",r"h%x","i #", "sM ", "$a ", "#t%", "ir!"]

def main():
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


if __name__ == "__main__":
    main()


