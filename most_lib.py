# coding=utf-8
from datetime import datetime
from bisect import bisect_left
import pytz

normalne = [4, 5, 6, 9, 10]
wakacyjne = [7, 8]
zamkniete = [11, 12, 1, 2, 3]
normalne_godziny_otwarcia = [1100, 1300, 1430, 1730]
wakacyjne_godziny_otwarcia = [830, 1130, 1300, 1430, 1730, 1900, 2120]
normalne_godziny_zamkniecia = [1030, 1200, 1330, 1600]
wakacyjne_godziny_zamkniecia = [800, 1030, 1200, 1330, 1430, 1830, 1900, 2120]


def czymostjestotwarty():
    tz = pytz.timezone('Europe/Warsaw')
    date_now = datetime.now(tz).month
    time_now = int(datetime.now(tz).strftime("%H%M"))
    if date_now in normalne:
        if 000 <= time_now <= 1030 or 1100 <= time_now <= 1200 or 1300 <= time_now <= 1330 or 1430 <= time_now <= 1600 or 1730 <= time_now <= 2359:
            return "Otwarty do %s" % closest(normalne_godziny_zamkniecia, time_now)
        else:
            return "Zamknięty do %s" % closest(normalne_godziny_otwarcia, time_now)
    elif date_now in wakacyjne:
        if 000 <= time_now <= 800 or 830 <= time_now <= 1030 or 1130 <= time_now <= 1200 or 1300 <= time_now <= 1330 or 1430 <= time_now <= 1600 or 1730 <= time_now <= 1830 or 1900 <= time_now <= 2030 or 2120 <= time_now <= 2359:
            return "Otwarty do %s" % closest(wakacyjne_godziny_zamkniecia, time_now)
        else:
            return "Zamknięty do %s" % closest(wakacyjne_godziny_otwarcia, time_now)
    elif date_now in zamkniete:
        return "Most otwarty tylko od kwietnia do października"
    else:
        return "Coś sie popsuło"


def closest(myList, myNumber):
    x = int(take_closest(myList, myNumber))
    y = str(x)
    if x <= 999:
        z = y[0] + ":" + y[1:]
        return z
    else:
        z = y[:2] + ":" + y[2:]
        return z


def take_closest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before
