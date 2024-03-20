def pal(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

i = input("Podaj słowo: ")


if pal(i):
    print("Jest palindromem!")
else:
    print("Nie jest palindromem!")
