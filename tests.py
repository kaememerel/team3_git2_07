wiek = input("Podaj wiek uzytkownika: ")
# Sprawdzamu, czy wiek jest zlozony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi byc podany jako liczba")
wiek = int(wiek)
if wiek >= 18 and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50:
    print("W Twoim wieku alkohol jest juz szkodliwy")
else:
    exit("Jestes za mlody na alkohol!")
