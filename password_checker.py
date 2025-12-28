import re

def check_password_strength(password: str) -> bool:
    """
    Checks whether the given password meets the strength criteria.
    Returns True if strong, False otherwise.
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):  # Uppercase letter
        return False

    if not re.search(r"[a-z]", password):  # Lowercase letter
        return False

    if not re.search(r"[0-9]", password):  # Digit
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Special character
        return False

    return True


# ---------------- Main Script ----------------

password = input("Enter your password: ")

if check_password_strength(password):
    print("✅ Password is STRONG. It meets all security requirements.")
else:
    print("❌ Password is WEAK.")
    print("Password must:")
    print("- Be at least 8 characters long")
    print("- Contain at least one uppercase letter (A-Z)")
    print("- Contain at least one lowercase letter (a-z)")
    print("- Contain at least one digit (0-9)")
    print("- Contain at least one special character (!@#$%^&*)")
