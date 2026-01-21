import os
import sys

# Complete the solve function below.
def solve(s):
    result = []
    capitalize_next = True

    for ch in s:
        if ch == ' ':
            result.append(ch)
            capitalize_next = True
        else:
            if capitalize_next and ch.isalpha():
                result.append(ch.upper())
            else:
                result.append(ch)
            capitalize_next = False

    return ''.join(result)


if __name__ == '__main__':
    # Works both on HackerRank and locally
    output_path = os.environ.get('OUTPUT_PATH')

    if output_path:
        fptr = open(output_path, 'w')
    else:
        fptr = sys.stdout  # local VS Code fallback

    s = input()
    result = solve(s)
    fptr.write(result + '\n')

    if output_path:
        fptr.close()
