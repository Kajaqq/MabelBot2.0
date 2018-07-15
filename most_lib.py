# coding=utf-8
from datetime import datetime
from bisect import bisect_left
import pytz

normalne = [4, 5, 6, 9, 10]
wakacyjne = [7, 8]
zamkniete = [11, 12, 1, 2, 3]
normalne_godziny_zamkniecia = [1030, 1200, 1330, 1600]
wakacyjne_godziny_zamkniecia = [8000, 1030, 1200, 1330, 1430, 1830, 1900, 2120]


def czymostjestotwarty():
    tz = pytz.timezone('Europe/Warsaw')
    date_now = datetime.now(tz).month
    time_now = int(datetime.now(tz).strftime("%H%M"))
    if date_now in normalne:
        if 0000 <= time_now <= 1030 or 1100 <= time_now <= 1200 or 1300 <= time_now <= 1330 or 1430 <= time_now <= 1600 or 1730 <= time_now <= 2359:
            return str("Otwarty do %s" % takeClosest(normalne_godziny_zamkniecia, time_now))
        else:
            return "Zamknięty"
    elif date_now in wakacyjne:
        if 0000 <= time_now <= 8000 or 8030 <= time_now <= 1030 or 1130 <= time_now <= 1200 or 1300 <= time_now <= 1330 or 1430 <= time_now <= 1600 or 1730 <= time_now <= 1830 or 1900 <= time_now <= 2030 or 2120 <= time_now <= 2359:
            return str("Otwarty do %s" % takeClosest(wakacyjne_godziny_zamkniecia, time_now))
        else:
            return "Zamknięty"
    elif date_now in zamkniete:
        return "Most otwarty tylko od kwietnia do października"
    else:
        return "Coś sie popsuło"


def takeClosest(myList, myNumber):
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

