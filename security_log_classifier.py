failed_logins = 0
successful_logins = 0
internal = 0
external = 0

users = []
ips = []
results = []
failed_by_user = {}

with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.")

for line in lines:
    username, ip, result = line.strip().split()

    users.append(username)
    ips.append(ip)
    results.append(result)

    # Count internal vs external
    if ip.startswith(("192.168.", "10.")):
        internal += 1
    else:
        external += 1

    # Count success vs failure
    if result == "FAILURE":
        failed_logins += 1

    # Track Failures    
        if username in failed_by_user:
            failed_by_user[username] += 1
        else: 
            failed_by_user[username] = 1

    else:
        successful_logins += 1


# Printing standard Data
print("Internal:", internal, "External:", external)
print("Success:", successful_logins, "Failure:", failed_logins)


# Detect Brute Force after Loop
for user, count in failed_by_user.items():
    if count >= 3:
        print("\nPossible Brute Force Attempt!")
        print(f"  {user} has {count} failed login attempts")