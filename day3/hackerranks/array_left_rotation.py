import os
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    n = len(a)
    d = d % n
    return a[d:] + a[:d]


if __name__ == '__main__':

    # Handle HackerRank OUTPUT_PATH or local stdout
    output_path = os.environ.get('OUTPUT_PATH')
    fptr = open(output_path, 'w') if output_path else sys.stdout

    # Read first line: n and d
    first_line = input().strip().split()
    n = int(first_line[0])
    d = int(first_line[1])

    # Read array
    a = list(map(int, input().strip().split()))

    # Rotate array
    result = rotLeft(a, d)

    # Write output
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    if output_path:
        fptr.close()
