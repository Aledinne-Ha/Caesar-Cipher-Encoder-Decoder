# 🔐 Caesar Cipher Tool

A command-line encryption tool that implements the Caesar Cipher — one of the oldest encryption techniques in history. Includes an encoder, decoder, brute force cracker, and frequency analysis attack.

Built with Python. No external libraries required.

---

## Features

- **Encrypt** any message with a custom shift key
- **Decrypt** any Caesar-encrypted message with the correct key
- **Brute force** crack an unknown ciphertext (tries all 25 possible keys)
- **Frequency analysis** — statistically guesses the key based on letter frequency
- Preserves spaces, numbers, and punctuation unchanged
- Handles both uppercase and lowercase letters correctly

---

## How to Run

**Requirements:** Python 3.6+

```bash
# Clone the repo
git clone https://github.com/Aledinne-Ha/caesar-cipher.git
cd caesar-cipher

# Run
python cipher.py
```

---

## Example Output

```
=============================================
      🔐 CAESAR CIPHER TOOL
=============================================

What do you want to do?
  1. Encrypt a message
  2. Decrypt a message
  3. Brute force crack a message
  4. Frequency analysis crack
  5. Quit

Enter choice (1-5): 1
Enter the message to encrypt: Meet me at midnight
Enter the shift key (1-25): 13

✅ Encrypted: Zrrg zr ng zvqavtug
   (Key used: 13)
```

**Brute force output on the same ciphertext:**
```
--- Brute Force Results ---

Shift  1: Yqqf yq mf yupcmtfd
Shift  2: Xppe xp le xtoblsec
...
Shift 13: Meet me at midnight  ✅
...
Shift 25: Anns an bu anreusba
```

---

## How It Works

The Caesar Cipher shifts each letter in the alphabet by a fixed number (the key):

```
Plaintext:  H  E  L  L  O
Shift +3:   K  H  O  O  R
Ciphertext: KHOOR
```

Decryption reverses the shift. Since there are only 25 possible keys, the brute force attack tries all of them — cracking any Caesar-encrypted message in milliseconds.

---

## Why This Cipher Is Broken

- Only **25 possible keys** — a computer tries all of them instantly
- Vulnerable to **frequency analysis** — the letter `E` appears most in English, so the most frequent letter in the ciphertext reveals the key
- Modern encryption (AES, RSA) uses keys with `2^128` or more possibilities — computationally impossible to brute force

---

## What I Learned

- Core cryptography vocabulary: plaintext, ciphertext, key, algorithm
- How `ord()` and `chr()` work — Python's interface to ASCII values
- Using modulo `%` to handle alphabet wrap-around
- What a brute force attack is and why keyspace size matters
- How frequency analysis breaks substitution ciphers

---

## Concepts Covered

`ord()` · `chr()` · modulo arithmetic · dictionaries · `lambda` · `while True` loops · `str.isupper()` · `str.islower()`
