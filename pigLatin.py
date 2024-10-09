def sentencePig(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pigWords = []

    for word in words:
        if word[0] in vowels:
            pigWords.append(word + "way")
        else:
            # Find the index of the first vowel
            for i in range(len(word)):
                if word[i] in vowels:
                    pigWords.append(word[i:] + word[:i] + "ay")
                    break
            else:
                pigWords.append(word) # Don't know what to do if there's not vowels in the word, so i'll just do this
    return " ".join(pigWords)

example1 = sentencePig("hope this works because")
example2 = sentencePig("i dont know what i am doing")
example3 = sentencePig("just chilling in the crypts")

print(example1)
print(example2)
print(example3)