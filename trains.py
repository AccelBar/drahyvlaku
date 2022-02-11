train1mins = int(input("Kolik minut trvá cesta prvního vlaku? "))
train1secs = int(input("Kolik sekund k tomu bude trvat cesta prvnímu vlaku? "))
train1time = train1mins * 60 + train1secs
print(f"Cesta prvního vlaku trvá {train1mins}min {train1secs}s.")
train2mins = int(input("Kolik minut trvá cesta druhého vlaku? "))
train2secs = int(input("Kolik sekund k tomu bude trvat cesta druhému vlaku? "))
train2time = train2mins * 60 + train2secs
print(f"Cesta druhého vlaku trvá {train2mins}min {train2secs}s.")
choice = 0

if train1mins > train2mins:
    longertrain = train1mins
    longertrainsecs = train1secs
    fastertrain = train2mins
    fastertrainsecs = train2secs
elif train2mins > train1mins:
    longertrain = train2mins
    longertrainsecs = train2secs
    fastertrain = train1mins
    fastertrainsecs = train1secs
elif train1mins == train2mins:
    if train1secs > train2secs:
        longertrain = train1mins
        longertrainsecs = train1secs
    elif train2secs > train1secs:
        longertrain = train2mins
        longertrainsecs = train2secs
    elif train2secs == train1secs:
        print("Oba vlaky se potkají při každém průjezdu stanicí,")
        print(f"tudíž každých {train1mins}min a {train1secs}s. ")


class Funkce1:
    def neplatnahodnotachoice():
        print("zadal jsi neplatnou hodnotu, hodnota musí být 1 nebo 2")
        return

    def spolecnynasobek():
        setkani = longertrain * train2time
        setkanimins = setkani // 60
        setkanisecs = setkani % 60
        print("Setkají se po uplynutí každého časového úseku")
        print(f"o délce {setkanimins}min a {setkanisecs}s. ")
        return

    def jinadoba():
        prodleva = int(input("O kolik minut vyrazí vlak později?"))
        longertrain1 = longertrain + prodleva
        setkani = longertrain1 * train2time
        setkanimins = setkani // 60
        setkanisecs = setkani % 60
        print("Setkají se po uplynutí každého časového úseku")
        print(f"o délce {setkanimins}min a {setkanisecs}s. ")


print("Vyráží vlaky ze stanice ve stejný moment?")
choice = int(input("(1 - ANO, 2 - NE)"))
if choice < 1:
    Funkce1.neplatnahodnotachoice()
if choice > 2:
    Funkce1.neplatnahodnotachoice()
if choice == 1:
    Funkce1.spolecnynasobek()
elif choice == 2:
    Funkce1.jinadoba()
    print("N/A")
