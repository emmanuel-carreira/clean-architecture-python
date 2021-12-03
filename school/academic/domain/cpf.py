import re

from school.academic.domain.value_object import ValueObject


class CPF(ValueObject):
    NUMBER_PATTERN = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
    def __init__(self, number: str) -> None:
        if number is None or not re.match(self.NUMBER_PATTERN, number):
            raise ValueError("Invalid CPF!")
        self.number = number

    def __repr__(self) -> str:
        return self.number
