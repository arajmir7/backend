import os
import sys

#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumSwaps(arr):
    swaps = 0
    i = 0

    while i < len(arr):
        correct_pos = arr[i] - 1

        if arr[i] != arr[correct_pos]:
            # Swap current element with the element at its correct position
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            swaps += 1
        else:
            i += 1

    return swaps


if __name__ == '__main__':

    # Handle HackerRank OUTPUT_PATH or local stdout
    output_path = os.environ.get('OUTPUT_PATH')
    fptr = open(output_path, 'w') if output_path else sys.stdout

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    if output_path:
        fptr.close()
