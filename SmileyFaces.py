def countSmileys(arr):
    faces=arr.split()
    for face in faces:
        if len(face)>2:
        # if (face[0]==";") | (face[0]==":"):


print(countSmileys([":)", ";(", ";}", ":-D"]))
print(countSmileys([";D", ":-(", ":-)", ";~)"]))
print(countSmileys([";]", ":[", ";*", ":$", ";-D"]))