"""
Caesar Cipher Encryption/Decryption
-----------------------------------
This program encrypts or decrypts text using the Caesar Cipher method.
Each letter is shifted by a given number of positions.
"""

def encrypt(text: str, shift: int) -> str:
    """Encrypt the text with Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def decrypt(cipher: str, shift: int) -> str:
    """Decrypt text encrypted with Caesar Cipher."""
    return encrypt(cipher, -shift)


def main():
    """Main program loop for Caesar Cipher."""
    print("🔐 Caesar Cipher Encryption Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("❌ Invalid option.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("❌ Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = encrypt(text, shift)
        print(f"🔒 Encrypted message: {encrypted}")
    else:
        decrypted = decrypt(text, shift)
        print(f"🔓 Decrypted message: {decrypted}")


if __name__ == "__main__":
    main()
