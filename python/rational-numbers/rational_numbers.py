from __future__ import division

class Rational(object):
    def __init__(self, numer, denom):
        reducedFraction = self.reduceFraction(numer, denom)
        self.numer = reducedFraction[0]
        self.denom = reducedFraction[1]

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

    def __rpow__(self, base):
        return base**(self.numer / self.denom)
    
    def reduceFraction(self, numer, denom):
        if numer == 0:
            return [0, 1]
        else:
            if numer * denom < 0:
                numer = -1 * abs(numer)
                denom = abs(denom)
            else:
                numer = abs(numer)
                denom = abs(denom)
            gcd = calculateGcd(abs(numer), abs(denom))
            return [numer//gcd, denom//gcd]

def calculateGcd(val1, val2):
    for i in range(1, min(val1, val2) + 1):
        if val1 % i == 0 and val2 % i == 0:
            gcd = i
    return gcd