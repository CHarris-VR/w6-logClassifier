failed_logins = 0
successful_logins = 0
internal = 0
external = 0

users = []
ips = []
results = []

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
    else:
        successful_logins += 1

print("Interal:", internal, "External:", external)
print("Success:", successful_logins, "Failure:", failed_logins)
