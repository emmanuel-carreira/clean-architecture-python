import re


class CPF:
    NUMBER_PATTERN = r"^(\d{3}\.){3}\-\d{2}$"
    def __init__(self, number: str) -> None:
        if number is None or not re.match(self.NUMBER_PATTERN, number):
            raise ValueError("Invalid CPF!")
        self.number = number
