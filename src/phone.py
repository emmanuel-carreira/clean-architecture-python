import re


class Phone:
    DDD_PATTERN = r"^\d{2}$"
    NUMBER_PATTERN = r"^\d{4,5}\-\d{4}$"

    def __init__(self, ddd: str, number: str) -> None:
        if ddd is None or not re.match(self.DDD_PATTERN, ddd):
            raise ValueError("Invalid DDD!")
        if number is None or not re.match(self.NUMBER_PATTERN, number):
            raise ValueError("Invalid number!")

        self.ddd = ddd
        self.number = number
