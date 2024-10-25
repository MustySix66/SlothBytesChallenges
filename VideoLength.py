def converter(length):
    min, sec = length.split(":")
    minutes=int(min)
    seconds=int(sec)
    if seconds>=60:
        return -1
    else:
        totalSec = (minutes*60)+seconds
    return totalSec

print(converter("01:00"))
print(converter("13:56"))
print(converter("10:60"))
print(converter("121:49"))