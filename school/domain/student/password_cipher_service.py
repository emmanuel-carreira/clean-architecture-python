class PasswordCipher:
    def cipher_password(self, password: str) -> str:
        raise NotImplementedError

    def validate_ciphered_password(self, ciphered_password: str, password: str) -> bool:
        raise NotImplementedError
