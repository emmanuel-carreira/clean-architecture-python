import re


class Email:
    ADDRESS_PATTERN = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$"

    def __init__(self, address: str) -> None:
        if address is None or not re.match(self.ADDRESS_PATTERN, address):
            raise ValueError("Invalid e-mail!")
        self.address = address
