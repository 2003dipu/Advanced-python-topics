"""def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase : ")))"""
#          ALTERNATIVE CODES - 1
"""def translate(phrase):
    translation = ''.join(['G' if letter.lower() in 'aeiou' and letter.islower() else letter for letter in phrase])
    return translation

print(translate(input("Enter a phrase: ")))"""
#           ALTERNATIVE CODES -2
"""def translate(phrase):
    translation_dict = {vowel: 'G' if vowel.islower() else 'g' for vowel in 'aeiou'}
    translation = ''.join([translation_dict.get(letter.lower(), letter) for letter in phrase])
    return translation

print(translate(input("Enter a phrase: ")))"""
#         ALTERNATIVE CODES -3
def translate(phrase):
    translation_table = str.maketrans('aeiouAEIOU', 'gggggGGGGG')
    translation = phrase.translate(translation_table)
    return translation

print(translate(input("Enter a phrase: ")))





