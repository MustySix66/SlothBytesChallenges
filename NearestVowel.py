def nearest_vowel(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if letter in vowels:
        return letter
    
    closest_vowel = vowels[0]
    print(closest_vowel)
    letter_index = alphabet.index(letter)
    print(letter_index)
    closest_vowel_index = alphabet.index(closest_vowel)
    print(closest_vowel_index)
    
    # Loop through the vowels to find the closest one
    for vowel in vowels:
        vowel_index = alphabet.index(vowel)
        print(vowel_index)
        
        # Check if the current vowel is closer than the previously set closest vowel
        if abs(letter_index - vowel_index) < abs(letter_index - closest_vowel_index):
            closest_vowel = vowel
            closest_vowel_index = vowel_index
    
    return closest_vowel



print(nearest_vowel("b"))
print(nearest_vowel("s"))
print(nearest_vowel("c"))
print(nearest_vowel("i"))