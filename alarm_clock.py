import datetime
import time
from logging import raiseExceptions

import pygame


def set_alarm_clock(alarm_clock):
    print(f"Alarm Clock set for {alarm_clock}")
    sound_file = "Scooter x Blasterjaxx x CERES - Heart Attack.mp3"
    is_rinning = True

    while is_rinning:
        curent_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(curent_time)

        if curent_time == alarm_clock:
            print("+++++++++++++++++++")
            print("WAKE UP")
            print(" ")
            print(" ")
            print("I LIKE IT LOUD")
            print("+++++++++++++++++++")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while (pygame.mixer.music.get_busy()):
                if input("IM WANKEN press q >>>").lower() == "q":
                    pygame.mixer.music.stop()
                    print(" ")

        time.sleep(1)


def alarm_clock(hour, minute, seconds):
    if (int(hour) >= 0 and int(hour) <= 23) and (int(minute) >= 0 and int(minute) <= 59) and (int(seconds) >= 0 and int(seconds) <= 59):
        alarm_time_setter = f"{str(hour)}:{str(minute)}:{str(seconds)}"


        return alarm_time_setter
    else:
        raise Exception("Invalid alarm clock")

    """
    
    elif hour is None:
        alarm_time_setter = f"{00}:{minute}:{seconds}"
        print(alarm_time_setter)

        return alarm_time_setter
    elif minute is None:
        alarm_time_setter = f"{hour}:{00}:{seconds}"
        print(alarm_time_setter)

        return alarm_time_setter
    elif seconds is None:
        alarm_time_setter = f"{hour}:{minute}:{00}"
        print(alarm_time_setter)
        return alarm_time_setter 
        
    """


if __name__ == '__main__':
    print("Alarm Clock SET")
    print("In  >> HH:MM:SS <<")
    while True:
        try:
            alarm_time = alarm_clock(input("HOURS:"), input("MINUTES:"), input("SECONDS:"))
            if alarm_time is not None:
                break

        except Exception:
            print("ERROR---->Wrong Input")
            print("TRY AGAIN")
            print("  ")
            continue

    set_alarm_clock(alarm_time)
