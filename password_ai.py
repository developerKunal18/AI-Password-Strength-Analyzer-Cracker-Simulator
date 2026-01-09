import math
import re

def password_strength(pw):
    length = len(pw)
    lower = bool(re.search("[a-z]", pw))
    upper = bool(re.search("[A-Z]", pw))
    digit = bool(re.search("[0-9]", pw))
    special = bool(re.search("[^a-zA-Z0-9]", pw))

    pool = 0
    if lower: pool += 26
    if upper: pool += 26
    if digit: pool += 10
    if special: pool += 32

    entropy = length * math.log2(pool)
    return entropy

def crack_time(entropy):
    guesses_per_sec = 1e9  # 1 billion guesses/sec
    seconds = (2 ** entropy) / guesses_per_sec

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"

print("🔐 Password Strength AI \n")

pw = input("Enter password: ")
entropy = password_strength(pw)
time = crack_time(entropy)

print("\n📊 Analysis")
print("Entropy:", round(entropy, 2))
print("Estimated crack time:", time)

if entropy < 40:
    print("❌ Weak password")
elif entropy < 60:
    print("⚠️ Medium strength")
else:
    print("✅ Strong password")
