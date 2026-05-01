def caesar_encrypt(plaintext, shift):
    """Encrypts a message using the Caesar Cipher."""
    ciphertext = ""

    for char in plaintext:
        if char.isupper():
            position     = ord(char) - ord('A')
            new_position = (position + shift) % 26
            new_char     = chr(new_position + ord('A'))
            ciphertext  += new_char

        elif char.islower():
            position     = ord(char) - ord('a')
            new_position = (position + shift) % 26
            new_char     = chr(new_position + ord('a'))
            ciphertext  += new_char

        else:
            ciphertext += char

    return ciphertext


def caesar_decrypt(ciphertext, shift):
    """Decrypts a Caesar Cipher message."""
    return caesar_encrypt(ciphertext, -shift)


def caesar_brute_force(ciphertext):
    """Tries all 25 possible shifts."""
    print("\n--- Brute Force Results ---")
    print("(Read through these and find the one that makes sense)\n")

    for shift in range(1, 26):
        attempt = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {attempt}")


def caesar_frequency_crack(ciphertext):
    """Uses frequency analysis to guess the shift."""
    letter_counts = {}

    for char in ciphertext.upper():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    if not letter_counts:
        print("No letters found in the ciphertext.")
        return

    most_frequent = max(letter_counts, key=lambda k: letter_counts[k])
    guessed_shift = (ord(most_frequent) - ord('E')) % 26

    print(f"\n--- Frequency Analysis ---")
    print(f"Most frequent letter in ciphertext: '{most_frequent}'")
    print(f"Assuming it represents 'E', guessed shift = {guessed_shift}")
    print(f"Decrypted attempt: {caesar_decrypt(ciphertext, guessed_shift)}")
    print("(This guess may be wrong for short messages — use brute force to confirm)")


def main():
    print("=" * 45)
    print("      🔐 CAESAR CIPHER TOOL")
    print("=" * 45)

    while True:
        print("\nWhat do you want to do?")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Brute force crack a message")
        print("  4. Frequency analysis crack")
        print("  5. Quit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift   = int(input("Enter the shift key (1-25): "))
            shift   = shift % 26
            result  = caesar_encrypt(message, shift)
            print(f"\n✅ Encrypted: {result}")
            print(f"   (Key used: {shift})")

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift   = int(input("Enter the shift key (1-25): "))
            result  = caesar_decrypt(message, shift)
            print(f"\n✅ Decrypted: {result}")

        elif choice == "3":
            message = input("Enter the ciphertext to brute force: ")
            caesar_brute_force(message)

        elif choice == "4":
            message = input("Enter the ciphertext for frequency analysis: ")
            caesar_frequency_crack(message)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
```