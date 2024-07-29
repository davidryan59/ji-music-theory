from src.functions import gcd


class Fraction:

    # TODO: add some different methods of initialisation
    def __init__(self, num: int, denom: int) -> None:
        if type(num) != int or type(denom) != int:
            raise Exception("Cannot initialise Fraction on non-integer numerator or denominator")

        if denom < 1:
            raise Exception("Cannot initialise Fraction on denominator < 1")

        _gcd = gcd(num, denom)
        self.num = int(num / _gcd)  # int shouldn't change the result, but does change the type from float to int
        self.denom = int(denom / _gcd)


    def __repr__(self, shorten: bool=True):
        if self.denom == 1 and shorten:
            return f"{self.num}"
        else:
            return f"{self.num}/{self.denom}"


    # TODO: add __mul__, __truediv__, etc
