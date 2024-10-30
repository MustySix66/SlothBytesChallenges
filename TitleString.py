def checkTitle(Titles):
    WordsList=Titles.split()
    for word in WordsList:
        if not (word[0].isupper()):
            return False
    return True

print(checkTitle("A Mind Boggling Achievement"))
print(checkTitle("A Simple C++ Program!"))
print(checkTitle("Water is transparent"))