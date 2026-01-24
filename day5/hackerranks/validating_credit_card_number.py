import re

n = int(input())

pattern = re.compile(r'^(4|5|6)\d{3}(-?\d{4}){3}$')

for _ in range(n):
    card = input().strip()

    # Step 1: basic regex validation
    if not pattern.match(card):
        print("Invalid")
        continue

    # Step 2: remove hyphens
    digits = card.replace("-", "")

    # Step 3: check for 4 consecutive repeated digits
    if re.search(r'(\d)\1{3,}', digits):
        print("Invalid")
    else:
        print("Valid")
