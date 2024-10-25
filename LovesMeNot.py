def loves_me(petals):
    LoveList = []
    for i in range(petals):
        if i%2 == 0:
            LoveList.append("Loves me")
        else:
            LoveList.append("Loves me not")
    LoveList[-1]=LoveList[-1].upper()
    finalString = ", ".join(LoveList)
    return finalString

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))