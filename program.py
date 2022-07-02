region = input("Wybierz swój region(EU/USA): ")
if region == "USA":
        print("Wybrales swoj region: " + region)
elif region == "EU":
                print("Wybrales swoj region: " + region)
else:
        exit("Mozesz wybrac tylko EU lub USA")
wiek = input("Podaj wiek użytkownika: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być podany jako liczba")
wiek = int(wiek)
if wiek >= 21 and wiek <= 50 and region == "USA" :
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50 and region == "USA":
    print("Witaj w naszym sklepie z alkoholem dla USA")
    print("W Twoim wieku alkohol jest już szkodliwy")

elif wiek >= 18 and wiek <= 50 and region == "EU" :
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50 and region == "EU":
    print("Witaj w naszym sklepie z alkoholem dla EU")
    print("W Twoim wieku alkohol jest już szkodliwy")
else:
    exit("Jesteś za młody na alkohol!")
