import random

def gtn():
    num = random.randint(1, 100)
    attempts = 0

    print("Zgdanij wylosowaną losowo liczbe z przedziału 1 do 100")

    while True:
        guess = int(input("Podaj swoją liczbe: "))
        attempts += 1

        if guess == num:
            print(f"Gratulacje!!! Udało Ci się odgadnąć liczbę {num} w [{attempts}] próbach")
            break
        elif guess < num:
            print("Zbyt niska! Spróbuj ponownie \n")
        else:
            print("Zbyt wyoska! Spróbuj ponownie \n")

gtn()
