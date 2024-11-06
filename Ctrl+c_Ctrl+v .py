def keyboardShortcut(sentence):
    words = sentence.split()
    clipboard = ""
    result = []
    i = 0
    while i < len(words):
        if words[i] == "Ctrl" and i+2 <len(words):
            if words[i+2] == "C":
                clipboard = " ".join(result)
                i +=3
                continue
            elif words[i+2] == "V":
                if clipboard:
                    result.append(clipboard)
                i+=3
                continue
        else:
            result.append(words[i])
            i+=1
    return " ".join(result)

print(keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon"))  # Output: "the egg and the egg and the spoon"
print(keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V"))  # Output: "WARNING WARNING"
print(keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"))  # Output: "The The Town The The Town"
