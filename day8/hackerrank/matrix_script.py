

import re




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Read column by column
decoded = ""
for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

# Replace symbols/spaces between alphanumeric with single space
decoded = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)

print(decoded)