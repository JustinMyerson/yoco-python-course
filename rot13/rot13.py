from pydoc import plain


def rot13(plaintext: str) -> str:
    """Returns the ciphertext resulting from encrypting `plaintext` using the rot13 algorithm"""
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ""

    if str(plaintext).isdigit():
        decrypted_text = plaintext
        return decrypted_text

    for char in plaintext:
        if char.isalpha():
            if char.islower():
                decrypted_text += lower_alphabet[(
                    lower_alphabet.index(char) + 13) % 26]
            elif char.isupper():
                decrypted_text += upper_alphabet[(
                    upper_alphabet.index(char) + 13) % 26]
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == "__main__":
    print(rot13("ohvyqvat n jro NCV sebz fpengpu"))
    print(rot13("n arj fbpvny zrqvn cyngsbez"))
