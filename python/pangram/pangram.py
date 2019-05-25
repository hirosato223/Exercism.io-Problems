def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    for letter in sentence:
        dict[letter] = True
    for letter in alphabet:
        if dict.get(letter) == None:
            return False
    return True