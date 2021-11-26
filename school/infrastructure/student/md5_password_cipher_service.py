from hashlib import md5

from school.domain.student.password_cipher_service import PasswordCipher


class MD5PasswordCipherService(PasswordCipher):
    def cipher_password(self, password: str) -> str:
        return md5(password).digest()

    def validate_ciphered_password(self, ciphered_password: str, password: str) -> bool:
        return ciphered_password == self.cipher_password(password)
