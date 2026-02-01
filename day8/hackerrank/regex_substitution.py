import re

n = int(input())

for _ in range(n):
    line = input()
    
    # Replace && with 'and' (with spaces)
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    
    # Replace || with 'or' (with spaces)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    
    print(line)