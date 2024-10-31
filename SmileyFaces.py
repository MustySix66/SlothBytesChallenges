def countSmileys(arr):
    finalArray = []
    for face in arr:
        if face[0] == ":" or face[0] == ";":
            # Verifica si el segundo carácter es una nariz o una sonrisa directa
            if len(face) == 2 and (face[1] == ")" or face[1] == "D"):
                finalArray.append(face)
            elif len(face) == 3 and (face[1] == "-" or face[1] == "~") and (face[2] == ")" or face[2] == "D"):
                finalArray.append(face)

    if len(finalArray) > 0:
        return "Hay " + str(len(finalArray)) + " smileys: " + str(finalArray)
    else:
        return "No hay Smileys :c"

print(countSmileys([":)", ";(", ";}", ":-D"]))
print(countSmileys([";D", ":-(", ":-)", ";~)"]))
print(countSmileys([";]", ":[", ";*", ":$", ";-D"]))
