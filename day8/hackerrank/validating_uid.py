import re

n = int(input())

for _ in range(n):
    uid = input().strip()
    
    # Check if exactly 10 characters
    if len(uid) != 10:
        print("Invalid")
        continue
    
    # Check if only alphanumeric
    if not uid.isalnum():
        print("Invalid")
        continue
    
    # Check if no repeating characters
    if len(uid) != len(set(uid)):
        print("Invalid")
        continue
    
    # Check if at least 2 uppercase letters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        print("Invalid")
        continue
    
    # Check if at least 3 digits
    if len(re.findall(r'[0-9]', uid)) < 3:
        print("Invalid")
        continue
    
    print("Valid")