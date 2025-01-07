# this doesnt pass 3rd test, but in discussion part i found that there is error in inputs
import sys
import re

def validate(uid):
    if re.search(r"^.*[A-Z]{2,}.*$", uid):
        if re.search(r"^.*[0-9]{3,}.*$", uid):
            if re.search(r"^\w{10}$", uid):
                if re.search(r"^(?!.*(.).*\1).*$", uid):
                    return "Valid"
    return "Invalid"

lines = sys.stdin.read().splitlines()

for uid in lines[1:]:
    print(validate(uid))