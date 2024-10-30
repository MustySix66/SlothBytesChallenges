oneDigit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teenDigits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numToEng(digitNum):
    if (digitNum < 10):
        return (oneDigit[digitNum])
    elif (digitNum < 20):
        return (teenDigits[digitNum - 10])
    elif(digitNum<100):
        if digitNum % 10 == 0:
            return tens[(digitNum // 10) - 1]
        else:
            return tens[(digitNum // 10) - 1] + " " + oneDigit[digitNum % 10]
    elif(digitNum<1000):
        hunds = oneDigit[digitNum // 100] + " hundred"
        rem = digitNum % 100
        if rem == 0:
            return hunds
        elif rem < 10:
            return hunds + " " + oneDigit[rem]
        elif rem < 20:
            return hunds + " " + teenDigits[rem - 10]
        else:
            tensPart = tens[(rem // 10) - 1]
            unitsPart = oneDigit[rem % 10] if (rem % 10 != 0) else ("")
            return hunds + " " + tensPart + (" " + unitsPart if unitsPart else "")
    else:
        return "number exceeds capacity"

print(numToEng(0))
print(numToEng(18))
print(numToEng(58))
print(numToEng(126))
print(numToEng(909))
print(numToEng(1909))
