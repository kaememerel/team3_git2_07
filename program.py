age = input("Podaj wiek uzytkownika: ")
# Sprawdzamu, czy wiek jest zlozony z cyfr
if age.isdigit() == False:
    exit("Wiek musi byc podany jako liczba")
age = int(age)
if age >= 18 and age <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif age > 50:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest juz szkodliwy")
else:
    exit("Jestes za mlody na alkohol!")

region = input("Wybierz swój region(EU/USA): ")
if region != "EU" and region != "USA":
    exit("Mozesz wybrac tylko EU lub USA")
exit("Wybrales swoj region: " + region)

plec = input("Podaj swoją płeć: ")

if plec == "kobieta":
    print("aperol spritz gratis")

