import re

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[@$!%*?&]", password)

    score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

password = input("Enter your password: ")
print("Password strength:", check_password_strength(password))
