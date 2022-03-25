class Time:
    def start():
        '''
        zjišťuje dobu kdy vlaky startují (ve stejný moment)
        '''
        global start_time_hours
        global start_time_mins
        global start_time_full_mins
        print("V kolik hodin vyjedou vlaky? (formát Hod:Min)")
        start_time_str = str(input())
        start_time_list = start_time_str.split(":", )
        start_time_hours = start_time_list[0]
        start_time_hours = int(start_time_hours)
        start_time_mins = start_time_list[1]
        start_time_mins = int(start_time_mins)
        start_time_full_mins = start_time_hours * 60
        start_time_full_mins = start_time_full_mins + start_time_mins

    def different_start():
        '''
        přidá rozdíl ve startu mezi vlaky
        '''
        global difference_full_mins
        # Rozdíl v Intu - pouze v minutách
        global difference_full_STR
        # Rozdíl ve stringu (formá HHh MMmin)
        # první vlak (start time)
        global first_start_time_full_mins
        print("V kolik hodin vyjede první vlak? (formát Hod:Min)")
        first_start_time_str = str(input())
        first_start_time_list = first_start_time_str.split(":", )
        first_start_time_hours = first_start_time_list[0]
        first_start_time_hours = int(first_start_time_hours)
        first_start_time_mins = first_start_time_list[1]
        first_start_time_mins = int(first_start_time_mins)
        first_start_time_full_mins = first_start_time_hours * 60
        x = first_start_time_full_mins
        y = first_start_time_mins
        first_start_time_full_mins = x + y
        # druhý vlak (start time)
        print("V kolik hodin vyjede první vlak? (formát Hod:Min)")
        second_start_time_str = str(input())
        second_start_time_list = second_start_time_str.split(":", )
        second_start_time_hours = second_start_time_list[0]
        second_start_time_hours = int(second_start_time_hours)
        second_start_time_mins = second_start_time_list[1]
        second_start_time_mins = int(second_start_time_mins)
        second_start_time_full_mins = second_start_time_hours * 60
        x = second_start_time_full_mins
        y = second_start_time_mins
        second_start_time_full_mins = x + y
        # rozdíl mezi vlaky
        z1 = first_start_time_full_mins
        z2 = second_start_time_full_mins
        if z1 > z2:
            difference_full_mins = z1 - z2
            difference_hours = difference_full_mins // 60
            difference_mins = difference_full_mins % 60
            difference_full_STR = f"{difference_hours}h {difference_mins}min "
        if z2 > z1:
            difference_full_mins = z2 - z1
            difference_hours = difference_full_mins // 60
            difference_mins = difference_full_mins % 60
            difference_full_STR = f"{difference_hours}h {difference_mins}min "

    def longer_train(first_train_secs_full, second_train_secs_full):
        '''
        zjistí který vlak má delší trasu a který ji má kratší
        '''
        global longer_train_secs
        global shorther_train_secs
        if first_train_secs_full > second_train_secs_full:
            longer_train_secs = first_train_secs_full
            shorther_train_secs = second_train_secs_full
        elif first_train_secs_full < second_train_secs_full:
            longer_train_secs = second_train_secs_full
            shorther_train_secs = first_train_secs_full
        elif first_train_secs_full == second_train_secs_full:
            longer_train_secs = first_train_secs_full
            shorther_train_secs = second_train_secs_full

    def encounter_interval():
        '''
        zjistí po jaké době se vlaky budou setkávat
        '''
        global encounter_interval_secs
        # v sekundách zapsaný interval setkání
        encounter_interval_secs = longer_train_secs // shorther_train_secs

    def number_of_encounters():
        '''
        zjistí kolikrát se vlaky setkají
        '''
        global encounters_secs
        global encounters_min
        global encounters_time
        global encounters
        lenght_of_ride_full_secs = lenght_of_ride_full_mins * 60
        encounters = lenght_of_ride_full_secs / encounter_interval_secs
        # setkají se každých {encounters} sekund
        encounters_min = encounters // 60
        encounters_secs = encounters % 60
        encounters_time = f"{encounters_min}min {encounters_secs}s "

    def end():
        '''
        zjišťuje dobu kdy vlaky končí
        '''
        global end_time_hours  # hodiny konce
        global end_time_mins  # minuty konce
        global end_time_full_mins
        # v minutách zapsaný kompletní konec vlaků
        print("V kolik hodin dojedou vlaky? (formát Hod:Min)")
        end_time_str = str(input())
        end_time_list = end_time_str.split(":", )
        end_time_hours = end_time_list[0]
        end_time_hours = int(end_time_hours)
        end_time_mins = end_time_list[1]
        end_time_mins = int(end_time_mins)
        end_time_full_mins = end_time_hours * 60
        end_time_full_mins = end_time_full_mins + end_time_mins

    def lenght_of_ride():
        '''
        počítá dobu kterou budou vlaky jezdit
        '''
        global time_of_ride_full
        # ve stringu zapsaná  doba kdy vlaky budou jezdit
        global lenght_of_ride_full_mins
        # v intu zapsaná doba kdy vlaky budou jezdit, XXX bude sloužit k
        # výpočtu setkání! XXX
        lenght_of_ride_full_mins = start_time_full_mins - end_time_full_mins
        lenght_of_ride_hours = lenght_of_ride_full_mins // 60
        lenght_of_ride_mins = lenght_of_ride_full_mins % 60
        time_of_ride_full = f"{lenght_of_ride_hours}h {lenght_of_ride_mins}min"

    def times_of_encounter():
        '''
        Spočítá časy kdy se vlaky setkají
        '''
        # import time_of_ride_full_mins
        # import first_start_time_full_mins
        # import encounters_interval_secs
        global time_string
        lenght_of_ride_full_secs = lenght_of_ride_full_mins * 60
        time_of_all_encounters_secs = []
        encounters1 = encounters
        encounters1 = int(encounters1)
        while (encounters != 0):
            time = lenght_of_ride_full_secs - encounters
            time_mins = time // 60
            time_secs = time % 60
            time_string = f"{time_mins}min. a {time_secs}sec. "
            time_of_all_encounters_secs.append(time_string)
        print(f"Vlaky se setkají v těchto časech: {time_string}.")


print("Ze všeho nejdřív zjistíme délku tratě jednotlivých vlaků. ")
choice1 = ["1" "ano" "jo" "a" "j"]
choice2 = ["0" "ne" "n"]
print("Zadej délku trasy prvního vlaku (na celé minuty): ")
first_train_mins = int(input())
print("Zadej délku trasy prvního vlaku (na celé sekundy): ")
first_train_secs = int(input())
first_train_secs_full = first_train_mins * 60
first_train_secs_full = first_train_secs_full + first_train_secs

print("Zadej délku trasy druhého vlaku (na celé minuty): ")
second_train_mins = int(input())
print("Zadej délku trasy druhého vlaku (na celé sekundy): ")
second_train_secs = int(input())
second_train_secs_full = second_train_mins * 60
second_train_secs_full = second_train_secs_full + second_train_secs

if first_train_mins and second_train_mins != 0:
    choice = str(input("vyráží vlaky ve stejný moment?\n"))
    if any(choice in s for s in choice1):
        print("V kolik hodin vyjedou vlaky? (formát Hod:Min)")
        start_time_str = str(input())
        start_time_list = start_time_str.split(":", )
        start_time_hours = start_time_list[0]
        start_time_hours = int(start_time_hours)
        start_time_mins = start_time_list[1]
        start_time_mins = int(start_time_mins)
        start_time_full_mins = start_time_hours * 60
        start_time_full_mins = start_time_full_mins + start_time_mins

        print("V kolik hodin dojedou vlaky? (formát Hod:Min)")
        end_time_str = str(input())
        end_time_list = end_time_str.split(":", )
        end_time_hours = end_time_list[0]
        end_time_hours = int(end_time_hours)
        end_time_mins = end_time_list[1]
        end_time_mins = int(end_time_mins)
        end_time_full_mins = end_time_hours * 60
        end_time_full_mins = end_time_full_mins + end_time_mins

        Time.longer_train(first_train_secs_full, second_train_secs_full)
        Time.encounter_interval()
        Time.lenght_of_ride()
        Time.number_of_encounters()
        Time.times_of_encounter()
    elif any(choice in s for s in choice2):
        print("V kolik hodin vyjede první vlak? (formát Hod:Min)")
        first_start_time_str = str(input())
        first_start_time_list = first_start_time_str.split(":", )
        first_start_time_hours = first_start_time_list[0]
        first_start_time_hours = int(first_start_time_hours)
        first_start_time_mins = first_start_time_list[1]
        first_start_time_mins = int(first_start_time_mins)
        first_start_time_full_mins = first_start_time_hours * 60
        x = first_start_time_full_mins
        y = first_start_time_mins
        first_start_time_full_mins = x + y
        # druhý vlak (start time)
        print("V kolik hodin vyjede první vlak? (formát Hod:Min)")
        second_start_time_str = str(input())
        second_start_time_list = second_start_time_str.split(":", )
        second_start_time_hours = second_start_time_list[0]
        second_start_time_hours = int(second_start_time_hours)
        second_start_time_mins = second_start_time_list[1]
        second_start_time_mins = int(second_start_time_mins)
        second_start_time_full_mins = second_start_time_hours * 60
        x = second_start_time_full_mins
        y = second_start_time_mins
        second_start_time_full_mins = x + y
        # rozdíl mezi vlaky
        z1 = first_start_time_full_mins
        z2 = second_start_time_full_mins
        if z1 > z2:
            difference_full_mins = z1 - z2
            difference_hours = difference_full_mins // 60
            difference_mins = difference_full_mins % 60
            difference_full_STR = f"{difference_hours}h {difference_mins}min "
        if z2 > z1:
            difference_full_mins = z2 - z1
            difference_hours = difference_full_mins // 60
            difference_mins = difference_full_mins % 60
            difference_full_STR = f"{difference_hours}h {difference_mins}min "

        print("V kolik hodin dojedou vlaky? (formát Hod:Min)")
        end_time_str = str(input())
        end_time_list = end_time_str.split(":", )
        end_time_hours = end_time_list[0]
        end_time_hours = int(end_time_hours)
        end_time_mins = end_time_list[1]
        end_time_mins = int(end_time_mins)
        end_time_full_mins = end_time_hours * 60
        end_time_full_mins = end_time_full_mins + end_time_mins

        Time.longer_train(first_train_secs_full, second_train_secs_full)
        Time.encounter_interval()
        Time.number_of_encounters()
        Time.lenght_of_ride()
        Time.times_of_encounter()
else:
    print("MÁŠ TAM CHYBU")
