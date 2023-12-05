#MessageDecryptorClass.py
from cryptography.fernet import Fernet

class MessageDecryptor:
    def __init__(self, key):
        """
        Constructor for MessageDecryptor.

        @Param:key (bytes): The key used for decryption.
        """
        self.key = key
        self.cipher = Fernet(self.key)

    def decrypt(self, encrypted_message):
        """
        Decrypt the provided message.

        @Param: encrypted_message (bytes): The encrypted message.

        @return: str: The decrypted message as a UTF-8 encoded string.
        """
        try:
            # Decrypt the message
            decrypted_message = self.cipher.decrypt(encrypted_message)
            return decrypted_message.decode('utf-8')
        except Exception as e:
            print(f"Error during decryption: {e}")
            return None

