class Time:
    def train1():  # zjišťuje dobu cesty prvního vlaku
        global first_train_mins
        global first_train_secs
        print("Zadej délku trasy prvního vlaku (na celé minuty): ")
        first_train_mins = int(input())
        print("Zadej délku trasy prvního vlaku (na celé sekundy): ")
        first_train_secs = int(input())

    def train2():  # zjišťuje dobu cesty druhého vlaku
        global second_train_mins
        global second_train_secs
        print("Zadej délku trasy druhého vlaku (na celé minuty): ")
        second_train_mins = int(input())
        print("Zadej délku trasy druhého vlaku (na celé sekundy): ")
        second_train_secs = int(input())

    def start():  # zjišťuje dobu kdy vlaky startují (ve stejný moment)
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

    def different_start():  # přidá rozdíl ve startu mezi vlaky
        global first_start_time_hours
        global first_start_time_mins
        global first_start_time_full_mins
        # první vlak (start time)
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
            # TODO nějak vytvořit rozdíl mezi vlaky

    def end():  # zjišťuje dobu kdy vlaky končí
        global end_time_hours
        global end_time_mins
        global end_time_full_mins
        print("V kolik hodin vyjedou vlaky? (formát Hod:Min)")
        end_time_str = str(input())
        end_time_list = end_time_str.split(":", )
        end_time_hours = end_time_list[0]
        end_time_hours = int(end_time_hours)
        end_time_mins = end_time_list[1]
        end_time_mins = int(end_time_mins)
        end_time_full_mins = end_time_hours * 60
        end_time_full_mins = end_time_full_mins + end_time_mins

    def lenght_of_ride():  # počítá dobu kterou budou vlaky jezdit
        global time_of_ride_full
        lenght_of_ride_full_mins = start_time_full_mins - end_time_full_mins
        lenght_of_ride_hours = lenght_of_ride_full_mins // 60
        lenght_of_ride_mins = lenght_of_ride_full_mins % 60
        time_of_ride_full = f"{lenght_of_ride_hours}h {lenght_of_ride_mins}min"

# TODO rozdílné časy (line 64)

# TODO setkání vlaků

# TODO počet setkání

# TODO časy setkání
