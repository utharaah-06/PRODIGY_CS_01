# ===== Caesar Cipher Program - Customized Version =====

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ===== Main Program =====
if __name__ == "__main__":
    print("=== Welcome to My Customized Caesar Cipher! ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")

    choice = input("Enter your choice (1 for Encrypt / 2 for Decrypt): ")
    message = input("What is your secret message? ")
    shift = int(input("Enter your shift number (e.g., 3): "))

    if choice == "1":
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
        print("You did it! ✅")
    elif choice == "2":
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
        print("You did it! ✅")
    else:
        print("Oops! Invalid choice. Please try again.")

