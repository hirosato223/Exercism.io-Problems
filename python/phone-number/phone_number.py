import re

class Phone(object):
    def __init__(self, phone_number):
        self.number = self.removeFormatting(phone_number)
        self.validateCodeRanges()
        self.area_code = self.number[:3]

    def removeFormatting(self, phoneNumber):
        cleanNumber = re.sub(r"\D", "", phoneNumber)
        if len(cleanNumber) <= 9 or len(cleanNumber) >=12:
            raise ValueError("The submitted phone number has too many digits!")
        if len(cleanNumber) == 11:
            if cleanNumber[0] != '1':
                raise ValueError("If length is 11, must start with 1")
            else:
                cleanNumber = cleanNumber[1:]
        return cleanNumber

    def validateCodeRanges(self):
        if self.number[0] == '0' or self.number[0] == '1':
            raise ValueError("Area code must start with digit in 2-9 range")
        if self.number[-7] == '0' or self.number[-7] == '1':
            raise ValueError("Exchange code must start with digit in 2-9 range")

    def pretty(self):
        return f'({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}'