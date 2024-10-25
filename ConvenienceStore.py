#Done by myself
def changeEnough(change, price):
    totalChange = 0
    totalChange += (float(change[0]) * 0.25)
    totalChange += (float(change[1]) * 0.10)
    totalChange += (float(change[2]) * 0.05)
    totalChange += (float(change[3]) * 0.01)
    if totalChange>=price:
        return True
    else:
        return False

print(changeEnough([2, 100, 0, 0], 14.11))
print(changeEnough([0, 0, 20, 5], 0.75))
print(changeEnough([30, 40, 20, 5], 12.55))
print(changeEnough([10, 0, 0, 50], 3.85))
print(changeEnough([1, 0, 5, 219], 19.99))

## Acording to chatgpt, this one's better, but i don't really understand it
def changesEnough(change, price):
    coin_values = [0.25, 0.10, 0.05, 0.01]
    totalChange = sum(c * v for c, v in zip(change, coin_values))
    return totalChange >= price

# Test cases
print(changesEnough([2, 100, 0, 0], 14.11))  # False
print(changesEnough([0, 0, 20, 5], 0.75))    # True
print(changesEnough([30, 40, 20, 5], 12.55))  # True
print(changesEnough([10, 0, 0, 50], 3.85))    # True
print(changesEnough([1, 0, 5, 219], 19.99))   # True