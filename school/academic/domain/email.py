import re

from school.academic.domain.value_object import ValueObject


class Email(ValueObject):
    ADDRESS_PATTERN = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$"

    def __init__(self, address: str) -> None:
        if address is None or not re.match(self.ADDRESS_PATTERN, address):
            raise ValueError("Invalid e-mail!")
        self.address = address

    def __repr__(self) -> str:
        return self.address
