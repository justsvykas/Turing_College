# I looked at HackerRank discussion board and I found a lot more concise solution
# I wanted to save it here so i remember everything can be done simpler
import re

matrix = ["Tsi",r"h%x","i #", "sM ", "$a ", "#t%", "ir!"]
n = 7
m = 3
tekst = ""
for i in range(m):
    for j in range(n):
        tekst += matrix[j][i]

# This regex matches non-alphanumeric characters ([^a-zA-Z0-9])
# only when they are surrounded by alphanumeric characters.
# ?<= does not bring a match but it looks in front of match
# ?= looks after the match
print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', tekst))