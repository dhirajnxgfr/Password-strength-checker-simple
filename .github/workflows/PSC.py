import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1

    # Number check
    if re.search(r"[0-9]", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength evaluation
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")


if __name__ == "__main__":
    main()
