# Opens the text file to read the data from it

with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")