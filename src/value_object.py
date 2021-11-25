class ValueObject:
    def __eq__(self, __o: object) -> bool:
        for attr in self.__dict__:
            if getattr(self, attr) != getattr(__o, attr):
                return False
        return True