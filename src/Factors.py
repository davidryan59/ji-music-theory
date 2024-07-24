import math
from src.Fraction import Fraction
from src.functions import isprime, factorise, factorise2, update_factor_dict


# Constants
L2 = math.log(2)
L3 = math.log(3)
CHARS_NOTES = ["F", "C", "G", "D", "A", "E", "B"]
FRACTIONS_NOTES = [[4, 3], [1, 1], [3, 2], [9, 8], [27, 16], [81, 64], [243, 128]]
FRACTION_SHARP = [2187, 2048]
CHAR_SHARP = "#"
CHAR_FLAT = "b"
CHAR_DOUBLE_SHARP = "x"
CHAR_5_UP = "’"  # Use a slanted quote mark, so two of them does not look like 11
CHAR_5_DOWN = "."
MAX_5_CHARS = 3  # Use "625" instead of ’’’’


# This Factors class is a wrapper around a factorisation of a rational number such as 90/5 = {2:1, 5:-1, 7:2}
# allowing these representations to be multiplied, divided, etc
class Factors:

    # Initialise the Factors object in several ways
    # 1a. from a numerator and denominator
    # 1b. from a number
    # 2.  from a dict of prime factors and powers
    # TODO: from a Fraction
    def __init__(self, num: int=None, denom: int=None, factors: dict=None) -> None:
        self._factors: dict = {}

        if type(num) == int and num > 0:
            if type(denom) == int and denom > 0:
                # 1a. Initialised from num and denom, overwrite the factors dict
                self._factors = factorise2(num, denom)
            else:
                # 1b. Initialised from num only, overwrite the factors dict
                self._factors = factorise(num)

        elif factors is not None:
            # 2. Initialised from factors only
            for prime, power in factors.items():
                if not isprime(prime):
                    continue

                if not type(power) == int or power == 0:
                    continue

                update_factor_dict(fact_dict=self.get_factor_dict(), prime=prime, add_power=power)


    # Return a dictionary representing factors, like {prime1: power1, prime2: power2}
    def get_factor_dict(self) -> dict:
        return self._factors


    # Return number of prime factors
    def count_prime_factors(self) -> int:
        return len(self.get_factor_dict().keys())


    # Return the power of a specific prime factor
    def get_power(self, prime) -> int:
        return self.get_factor_dict().get(prime, 0)


    # Set a power of a specific prime factor
    def set_power(self, prime, power) -> None:
        update_factor_dict(fact_dict=self.get_factor_dict(), prime=prime, power=power)


    # Clear a specific prime power out of an object
    def clear_power(self, prime) -> None:
        self.set_power(prime, 0)


    # Return a list of (prime, power) of the factors, e.g. to iterate over
    def get_factor_items(self) -> list:
        return list(self.get_factor_dict().items())


    # Copy an existing object
    def copy(self):
        return Factors(factors=self.get_factor_dict())


    # Return string representation of this object
    def __repr__(self):
        return f"Factors {self.get_factor_dict()}"


    # Return new Factors equal to self * fs
    def __mul__(self, fs):
        res = self.copy()
        for prime, power in fs.get_factor_items():
            update_factor_dict(fact_dict=res.get_factor_dict(), prime=prime, add_power=power)

        return res


    # Return new Factors equal to self / fs
    def __truediv__(self, fs):
        res = self.copy()
        for prime, power in fs.get_factor_items():
            update_factor_dict(fact_dict=res.get_factor_dict(), prime=prime, subtract_power=power)

        return res


    # Raise a Factors instance to an integer power
    def __pow__(self, pow: int):
        if type(pow) != int:
            raise Exception(f"{pow} is not an integer")
        
        if pow == 0:
            return Factors()

        if pow == 1:
            return self

        if pow < 0:
            return Factors() / self ** -pow

        pow2 = int(pow / 2)
        self2 = self * self
        selfn2 = self2 ** pow2
        if pow % 2 == 0:
            return selfn2
        else:
            return selfn2 * self


    # Return a Fraction object that has equal numerator and denominator to this object
    def get_fraction(self) -> Fraction:
        num = 1
        denom = 1
        for prime, power in self.get_factor_items():
            if power > 0:
                num *= prime ** power
            elif power < 0:
                denom *= prime ** -power

        return Fraction(num, denom)


    # Return a Factors object representing 1/1
    @classmethod
    def one(cls):
        return Factors()  # empty parameters for constructor evaluates to 1


    # Calculate a prime comma for a prime number using DR method
    @classmethod
    def get_prime_comma(cls, prime):
        if not isprime(prime) or prime < 5:
            raise Exception(f"{prime} is not a prime number greater than 4")

        # Make a range of potential values for -b
        lp = math.log(prime)
        mid3 = 0.5 * lp / L3
        min3A = round(mid3 - 5.5)
        max3A = round(mid3 + 5.5)
        min3B = 0
        max3B = round(mid3 * 2)
        min3 = min(min3A, min3B)
        max3 = max(max3A, max3B)
        # Try all values of -b between min3 and max3

        res = []
        for b in range(-max3, -min3 + 1):
            height2 = lp + b * L3
            a = -round(height2 / L2)
            interval_size = abs(lp + a * L2 + b * L3)
            interval_complexity = lp + abs(a) * L2 + abs(b) * L3
            comma_measure = interval_size * interval_complexity
            row = [comma_measure, a, b]
            res.append(row)

        res.sort(key=lambda item: item[0])  # Sort rows by comma measure increasing
        selected_comma_data = res[0]
        a = selected_comma_data[1]
        b = selected_comma_data[2]
        fs = Factors(factors={
            prime: 1,
            2: a,
            3: b,
        })
        return fs

    # Split this object into a Pythagorean component {2:a, 3:b} and a product of prime commas
    def get_pythag_split(self):
        comma_powers = []
        for prime, power in self.get_factor_items():
            if prime > 4:
                comma = Factors.get_prime_comma(prime)
                comma_power = comma ** power
                comma_powers.append(comma_power)

        # Make 2 new objects to calculate the results with
        fs_pythag = self.copy()
        fs_commas = Factors.one()
        for comma_power in comma_powers:
            fs_pythag /= comma_power
            fs_commas *= comma_power
        
        return fs_pythag, fs_commas


    # Return a musical notation string for this object
    # TODO formatting options:
    # - which number represents C4, at the moment 1/1 is hard-coded
    # - whether to use double sharp, or not (bool)
    # - how many 5-comma chars to use (int 0+)
    def get_notation_data(self):
        fs23, fs5 = self.get_pythag_split()
        pow2 = fs23.get_power(2)
        pow3 = fs23.get_power(3)
        note_name_idx = (pow3 + 1) % 7  # 0=F, 1=C, 2=G... 6=B
        sharp_idx = int(((pow3 + 1) - note_name_idx) / 7)  # 0 = natural, 1 = #, 2 = ##, -1 = b, -2 = bb, etc
        count_sharps = max(0, sharp_idx)
        count_flats = max(0, -sharp_idx)
        note_name = CHARS_NOTES[note_name_idx]
        sharps = CHAR_DOUBLE_SHARP * int(count_sharps / 2) + CHAR_SHARP * (count_sharps % 2)
        flats = CHAR_FLAT * count_flats
        accs3 = f"{sharps}{flats}"  # 3-limit accidentals
        fs2 = fs23 / (NOTE_FS[note_name_idx] * (SHARP_FS ** sharp_idx))
        pow2 = fs2.get_power(2)
        oct2 = pow2 + 4

        # Make copy of fs5 and use it to construct the comma (higher prime) data
        # Every comma is of form 2^a * 3^b * p,
        # so can remove powers of 2 and 3 to get all remaining comma information
        fs5c = fs5.copy()
        fs5c.clear_power(2)
        fs5c.clear_power(3)
        # Now fs5c represents the set of commas applied to the original note

        # If there are not too many 5 commas, use a shorthand for them
        pow5 = fs5c.get_power(5)
        accs5 = ""  # 5-limit accidentals
        if abs(pow5) <= MAX_5_CHARS:
            fs5c.clear_power(5)
            if pow5 >= 1:
                accs5 = CHAR_5_UP * pow5
            elif pow5 <= -1:
                accs5 = CHAR_5_DOWN * -pow5

        commas_p = fs5c.get_fraction()
        commas_p = "" if fs5c.count_prime_factors() == 0 else f" [{commas_p}]"

        return note_name, oct2, accs3, accs5, commas_p


    # Return a musical notation string for this object
    # TODO: allow various formatting options here
    # - positioning of the commas_p text
    def get_ji_notation(self) -> str:
        note_name, oct2, accs3, accs5, commas_p = self.get_notation_data()
        return f"{note_name}{accs3}{accs5}{oct2}{commas_p}"


    # TODO: function to turn a notation back into a Factors object


NOTE_FS = [Factors(num=item[0], denom=item[1]) for item in FRACTIONS_NOTES]
SHARP_FS = Factors(num=FRACTION_SHARP[0], denom=FRACTION_SHARP[1]) 
