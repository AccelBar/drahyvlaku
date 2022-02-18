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
        global setkani
        setkani = longertrain * train2time
        setkanimins = setkani // 60
        setkanisecs = setkani % 60
        setkanimins = setkanimins / 2
        setkaniminsfull = setkanimins
        pocetpotkani = setkaniminsfull / timeofridefullmin
        pocetpotkani = round(pocetpotkani)
        print("Setkají se po uplynutí každého časového úseku")
        print(f"o délce {setkanimins}min a {setkanisecs}s. ")
        print(f"Potkají se tedy celkem {pocetpotkani}x.")
        return

    def jinadoba():
        global setkani
        pocetpotkani = 0
        prodleva = int(input("O kolik minut vyrazí první vlak později?"))
        longertrain1 = train2time + prodleva
        setkani = longertrain1 * train2time
        setkanimins = setkani // 60
        setkaniminsfull = setkanimins
        setkanimins = setkanimins / 2
        setkanisecs = setkani % 60
        pocetpotkani = setkaniminsfull / timeofridefullmin
        pocetpotkani = round(pocetpotkani)
        print("Setkají se po uplynutí každého časového úseku")
        print(f"o délce {setkanimins}min a {setkanisecs}s. ")
        print(f"Potkají se tedy celkem {pocetpotkani}x.")
        return

    def jinadoba1():
        global setkani
        global pocetpotkani
        pocetpotkani = 0
        prodleva = int(input("O kolik minut vyrazí druhý vlak později?"))
        longertrain1 = longertrain + prodleva
        setkani = longertrain1 * train2time
        setkanimins = setkani // 60
        setkaniminsfull = setkanimins
        setkanimins = setkanimins / 2
        setkanisecs = setkani % 60
        pocetpotkani = setkaniminsfull / timeofridefullmin
        pocetpotkani = round(pocetpotkani)
        print("Setkají se po uplynutí každého časového úseku")
        print(f"o délce {setkanimins}min a {setkanisecs}s. ")
        print(f"Potkají se tedy celkem {pocetpotkani}x.")
        return

    def odkdydokdy():
        global timeofrideh
        global timeofridemin
        global timeofridefullmin
        global startmin
        global endmin
        starthinp = int(input("V kolik hodin vyráží vlaky? "))
        startmininp = int(input("Kolik minut k tomu? "))
        endhinp = int(input("Do kolika hodin budou jezdit? "))
        endmininp = int(input("Kolik minut k tomu? "))
        startmin = starthinp / 60
        startmin = startmin + startmininp
        endmin = endhinp / 60
        endmin = endmin + endmininp
        timeofride = startmin - endmin
        timeofrideh = timeofride / 60
        timeofridemin = timeofride % 60
        timeofridefullmin = endmin - startmin
        return

    def urcitecasy():
        # pocetpotkani
        # timeofridefullmin
        # setkani
        timehours = timeofridefullmin // 60
        timemins = timeofridefullmin % 60
        mezikrok = 0
        setkanilist = []
        setkanihourint = 0
        while pocetpotkani != 0:
            mezikrok = timemins
            if mezikrok < 60:
                setkanihourint = setkanihourint + 1
                setkanicashour = timehours + setkanihourint
                setkaniminint = mezikrok - 60
                setkanifull = (f"{setkanicashour}h a {setkaniminint}min.")
                setkanilist.append(setkanifull)
            if mezikrok == 60:
                setkanihourint = setkanihourint + 1
                setkanicashour = timehours + setkanihourint
                setkaniminint = mezikrok - 60
                setkanifull = (f"{setkanicashour}h a {setkaniminint}min.")


print("Vyráží vlaky ze stanice ve stejný moment?")
choice = int(input("(1 - ANO, 2 - NE)"))
if choice < 1:
    Funkce1.neplatnahodnotachoice()
if choice > 2:
    Funkce1.neplatnahodnotachoice()
if choice == 1:
    Funkce1.odkdydokdy()
    Funkce1.spolecnynasobek()
elif choice == 2:
    choice2 = int(input("Vyráží později první nebo druhý vlak?"))
    if choice2 == 1:
        Funkce1.odkdydokdy()
        Funkce1.jinadoba()
    elif choice2 == 2:
        Funkce1.odkdydokdy()
        Funkce1.jinadoba1()
    else:
        print("Zadal jsi neplatnou hodnout.")
