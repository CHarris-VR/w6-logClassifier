# Opens the text file to read the data from it

with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")

# Stores data into lists
for line in lines:
    parts = line.strip().split()
    # parts = [username, ip, result]


# Added this for the loop below
failed_logins = 0
successful_logins = 0

# if failure, add a failed logins counter + 1 else success counter + 1

if parts[2] == "FAILURE":
    failed_logins += 1
else:
    successful_logins += 1

print("successful logins: ", successful_logins)