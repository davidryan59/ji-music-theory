import math
from src.functions import gcd


L2 = math.log(2)

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



    def value(self):
        return self.num / self.denom


    def cents(self, dps: int=2):
        res = 1200 * math.log(self.value()) / L2
        if dps < 1:
            return int(res)
        else:
            return round(res, dps)


    # TODO: add __mul__, __truediv__, etc
