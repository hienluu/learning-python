import string


def decrypt(ab_cipher_msg, ab_cleartext_msg):
    """
    Decrypts a message that was encrypted using a simple substitution cipher.

    Parameters:
    - ab_encoded_message (str): The encrypted message to be decrypted.
    - key (dict): A dictionary mapping each character in the encrypted message
                  to its corresponding character in the original message.

    Returns:
    - str: The decrypted message.
    """
    decrypted_message = ''.join(key.get(char, char) for char in ab_encoded_message)
    return decrypted_message

def encrypt(ab_cleartext_msg: str, mapping_key: dict[str, str]) -> str:
    """
    Encrypts a message using a simple substitution cipher.

    Parameters:
    - ab_cleartext_msg (str): The original message to be encrypted.
    - mapping_key (dict): A dictionary mapping each character in the original message
                          to its corresponding character in the encrypted message.

    Returns:
    - str: The encrypted message.
    """
    encrypted_message = ''.join(mapping_key.get(char, char) for char in ab_cleartext_msg)
    return encrypted_message

def mapping_key(ab_cipher_msg, ab_cleartext_msg) -> dict[str, str]:
    """
    Creates a mapping key for a simple substitution cipher based on the provided
    encrypted and cleartext messages.

    Parameters:
    - ab_cipher_msg (str): The encrypted message.
    - ab_cleartext_msg (str): The original cleartext message.

    Returns:
    - dict: A dictionary mapping each character in the encrypted message
            to its corresponding character in the original message.
    """
    mapping:dict[str, str] = {char: char for char in string.ascii_lowercase}
    for index in range(len(ab_cipher_msg)):
        mapping[ab_cipher_msg[index]] = ab_cleartext_msg[index]

    return mapping
    #return {cipher_char: cleartext_char for cipher_char, cleartext_char in zip(ab_cipher_msg, ab_cleartext_msg)}

if __name__ == "__main__":
    print("Enter the encrypted message:")

    print(f"mapping_key('gsv jfrxp yildm', 'the quick brown') = {mapping_key('gsv jfrxp yildm', 'the quick brown')}")
    print(f"mapping_key('xyz dfmnp tbcho', 'the quick brown') = {mapping_key('xyz dfmnp tbcho', 'the quick brown')}")