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