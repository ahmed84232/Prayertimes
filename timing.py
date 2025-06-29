from datetime import datetime


def current_time():

    time = datetime.now().time().strftime("%I:%M %p")
    time = time.split(":")
    time1 = time[0]
    time2 = time[1].split(" ")
    daytime = time2[1]
    time2 = time2[0]
    return int(time1), int(time2), daytime


def current_time_12():
    time = datetime.now().time().strftime("%I:%M %p")
    time = time.split(":")
    time1 = str(int(time[0]))
    time2 = time[1]
    time = time1 + ":" + time2
    return time


def prayer_time_formatter(prayer_time):

    time = prayer_time
    time = time.split(":")
    time1 = time[0]
    time2 = time[1].split(" ")
    daytime = time2[1]
    time2 = time2[0]
    return int(time1), int(time2), daytime


def remaining_time_for_prayer(prayer_time):

    # Declaring time variables
    current_time1, current_time2, current_daytime = current_time()
    prayer_time1, prayer_time2, prayer_daytime = prayer_time_formatter(prayer_time)
    if current_time1 == 12:
        current_time1 = 0
    else:
        pass

    if current_daytime == prayer_daytime:

        remaining_time1 = prayer_time1 - current_time1

        remaining_time2 = 0

        if current_time1 < prayer_time2:
            remaining_time_min = prayer_time2
        else:
            remaining_time_min = current_time2

        remaining_time2 = prayer_time2 - current_time2
        remaining_time = f"{str(remaining_time1)}:{str(abs(remaining_time2))}"

    else:

        remaining_time1 = 12 - current_time1 + prayer_time1

        if current_time1 < prayer_time2:
            remaining_time_min = prayer_time2
        else:
            remaining_time_min = current_time2

        remaining_time2 = prayer_time2 - current_time2
        remaining_time = f"{str(remaining_time1)}:{str(abs(remaining_time2))}"


    return remaining_time

