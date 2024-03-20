
def change(sentence):
    newLet = {'o': '0', 'e': '3', 'i': '1', 'a': '4'}
    newSent = ''
    for letters in sentence:
        if letters.lower() in newLet:
            newSent += newLet[letters.lower()]
        else:
            newSent += letters
    return newSent

sentencja_uzytkownika = input("Podaj zdanie: ")
print("Zamienione :", change(sentencja_uzytkownika))
