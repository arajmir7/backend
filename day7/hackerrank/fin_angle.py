import math

# Read inputs
AB = int(input().strip())
BC = int(input().strip())

# Calculate angle in radians
angle_rad = math.atan(AB / BC)

# Convert to degrees and round
angle_deg = round(math.degrees(angle_rad))

# Print result with degree symbol (ASCII-safe)
print(str(angle_deg) + chr(176))
