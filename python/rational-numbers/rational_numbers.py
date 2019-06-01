from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        updatedNumer = self.numer * other.denom + self.denom * other.numer
        updatedDenom = self.denom * other.denom
        return Rational(0, 1) if updatedNumer == 0 else Rational(updatedNumer, updatedDenom)

    def __sub__(self, other):
        updatedNumer = self.numer * other.denom - self.denom * other.numer
        updatedDenom = self.denom * other.denom
        return Rational(0, 1) if updatedNumer == 0 else Rational(updatedNumer, updatedDenom)

    def __mul__(self, other):
        updatedNumer = self.numer * other.numer
        updatedDenom = self.denom * other.denom
        return Rational(0, 1) if updatedNumer == 0 else Rational(updatedNumer, updatedDenom)

    def __truediv__(self, other):
        updatedNumer = self.numer * other.denom
        updatedDenom = self.denom * other.numer
        return Rational(0, 1) if updatedNumer == 0 else Rational(updatedNumer, updatedDenom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        elif power < 0:
            return Rational(self.numer ** abs(power), self.denom ** abs(power))
        pass

    def __rpow__(self, base):
        pass
