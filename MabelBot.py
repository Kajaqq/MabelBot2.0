# This Python file uses the following encoding: utf-8
import threading

from fbchat import Client
from fbchat.models import *
import wikipedia
import clever
import buleczki_lib
import subprocess
from d3s_lib import gitgud
from most_lib import czymostjestotwarty
from luszownictwo import lurczak
from random import randint

# presety
from MabelPassy import MabelConfig

id_emilki = MabelConfig.idEmilki
id_kajaka = MabelConfig.idKajaka
id_grupki = MabelConfig.idGrupki
id_wujcika = MabelConfig.idWujcika
banned_ids = MabelConfig.bannned_ids
cleveruser = MabelConfig.cleveruser
cleverapi = MabelConfig.cleverkey
linux_names = ["linuch", "linux", "linuks"]
shit_searches = ['AMD', 'Asuka', 'fata morgana no yakata']
love_react = ["linux ty kurwo", "evangelion to szrot", "jojo je gunwo", "Asuka jest kurwa"]
mTable = []
wikipedia.set_lang("pl")
Mabel_login = MabelConfig.login
Mabel_password = MabelConfig.password


def goraca_aktualizacja(message_object, thread_id, thread_type):
    message_object.send(Message(text="Aktualizuję bota..."), thread_id, thread_type)
    subprocess.call(['chmod', '+x', 'hotfix.sh'])
    subprocess.call(['./hotfix.sh'])
    exit()


def wiki_kobietalekkichobyczajow(term):
    if term in shit_searches:
        wyszukiwanie = wikipedia.search(u"Kał")
        return wikipedia.summary(wyszukiwanie[0], 1)
    else:
        try:
            wyszukiwanie = wikipedia.search(term)
            return wikipedia.summary(wyszukiwanie[0], 3)
        except Exception as e:
            return "Błąd: %s" % e


def read_commands():
    del mTable[:]
    with open("gownoposty.txt") as file:
        for line in file:
            cmd = line.split()
            mTable.append(cmd[0])


read_commands()


def sendShit(msg):
    cmd_buff = msg.split()
    cmd = cmd_buff[0]
    index = mTable.index(cmd)
    m_buffer = open("gownoposty.txt", "r")
    with m_buffer as file:
        for i, line in enumerate(file):
            if i == index:
                cmd_buff = line.split()
                msg = ' '.join(cmd_buff[1:])
    m_buffer.close()
    return msg


class MabelBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        print("%s napisał: %s" % (author_id, message_object.text))  # output log
        cb = clever.Cleverbot(cleveruser, cleverapi)
        if thread_type == ThreadType.GROUP and thread_id in id_grupki and author_id != self.uid:
            msg = message_object.text.lower()
            global aipreset
            aipreset = ""
            if msg.startswith('/add'):
                msg1 = msg.split()
                if len(msg1) > 2:
                    if msg1[1] != '/':
                        if msg1[1] not in mTable:
                            f_content = ' '.join(msg[1:])
                            f_buffer = open("gownoposty.txt", "a")
                            f_buffer.write(f_content + '\n')
                            self.send(Message(text="No elo dodałem: {:s}".format(msg[1])), thread_id, thread_type)
                            f_buffer.close()
                            read_commands()
                        else:
                            self.send(Message(text="Komenda już istnieje"), thread_id, thread_type)
                    else:
                        self.send(Message(text="Nie możesz dać samego /"), thread_id, thread_type)
                else:
                    self.send(Message(text="Trzy lub więcej słowa potrzebne"), thread_id, thread_type)

            elif msg.startswith("/wiki"):
                self.send(Message(text=wiki_kobietalekkichobyczajow(message_object.text[6:])), thread_id, thread_type)

            elif msg.startswith("/echo"):
                self.send(Message(text=message_object.text[6:]), thread_id, thread_type)

            elif msg.startswith(tuple(mTable)):
                self.send(Message(text=sendShit(message_object.text)), thread_id, thread_type)

            elif msg == "/plucietotalne":
                self.sendLocalImage('plucie.gif', message=Message(text='Tfu!'),
                                    thread_id=thread_id, thread_type=thread_type)

            elif msg == "/update":
                goraca_aktualizacja(self, thread_id, thread_type)

            elif msg.startswith("/git"):
                self.send(Message(text=gitgud(msg[5:])), thread_id, thread_type)

            elif msg == "/czymostjestotwarty":
                self.send(Message(text=czymostjestotwarty()), thread_id, thread_type)

            elif msg == "/random":
                self.send(Message(text=randint(1, 100)), thread_id, thread_type)

            elif msg == "co":
                self.send(Message(text='jajco kurwa'), thread_id, thread_type)

            elif msg == "nk":
                self.send(Message(text='co, rąk ni mosz do roboty?'), thread_id, thread_type)

            elif msg == "arka gdynia":
                self.send(Message(text='KURWA ŚWINIA'), thread_id, thread_type)

            elif msg == u"zagłębie sosnowiec":
                self.send(Message(text='KURWA BOMBOWIEC'), thread_id, thread_type)

            elif msg == "łódź bałuty":
                self.sendRemoteImage('http://www33.patrz.pl/u/f/29/39/76/293976.jpg',
                                     thread_id=thread_id, thread_type=thread_type)
            elif msg == "2deep4u":
                self.sendRemoteImage('https://i.imgur.com/xulBcmn.png', thread_id, thread_type)

            elif msg == "Hawajska to szrot":
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.ANGRY)
                self.send(Message(
                    text="Możecie nalać polaczkowi Don Perignona, albo dobrej whisky 18 letniej. Polaczek wypije "
                         "duszkiem i powie, że cierpkie i jakieś mdłe. Dacie polakowi trufli to powie, że to jakiś "
                         "zgniły czosnek. Zaparzycie polaczkowi dobrego espresso z dobrej, ręcznej maszyny, "
                         "z świeżo mielonych ziaren bardzo dobrej jakości, powie że jakaś mała ta kawa i w ogóle "
                         "kwaśna i i dziwnie smakuje. Dlatego mnie nie dziwi, że 3/4 z was, biedaki szkaluje "
                         "HAWAJSKĄ. Nie dziwi mnie to, ponieważ wiem że jesteście tylko biednymi cebulakami i całe "
                         "życie schabowe z mięsa za 7,99/kg. Nie znacie życia, wasze kubki smakowe są wypalone od "
                         "podrobionych fajek i chujowej wódki. Nigdy nie mieliście okazji poznać smaków. Na widok "
                         "pizzy z miodem byście pewnie skakali i darli mordę jak te małpy w zoo. Kompozycja "
                         "słodko-słone, albo słodko-kwaśne to jedna z najlepszych rzeczy jakie można skonsumować. "
                         "Prawdziwa eksplozja dla wyrafinowanych smakoszy. "
                         "W cywilizowanej i rozwiniętej Japonii, kiedy córka przyprowadza i przedstawia swojego "
                         "wybranka rodzicom, ci wykonują test. Podają mu Hawajską. Kiedy chłopak pizzy nie zje, "
                         "albo powie że mu nie smakuje, to wiadomo że pochodzi z patologicznej rodziny. Test działa z "
                         "dokładnością 100% i nawet WHO i ONZ przyznali, że u rodzin w których dominuje alkoholizm, "
                         "narkomaństwo i kazirodztwo zawsze pojawia się niechęć do pizzy z ananasem. ")
                    , thread_type, thread_id)
                self.sendRemoteImage('https://i.imgur.com/xulBcmn.png', thread_id, thread_type)

            elif msg == "/poilebananywlidlu":
                self.send(Message(text='3,79 zł/kg'), thread_id, thread_type)

            elif msg == "/poilebuleczkiwbiedrze":
                self.send(Message(text=buleczki_lib.buleczki()), thread_id, thread_type)

            elif msg == "reload":
                self.removeUserFromGroup(author_id, id_grupki)
                self.addUsersToGroup(author_id, id_grupki)

            elif msg in love_react:
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.LOVE)

            elif author_id == id_wujcika and msg.startswith("kajak"):
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.ANGRY)

            elif msg == "/help":
                self.send(Message(text="Pomoc MabelBota 2.0\nBased on d3suu's MabelBot\nModified by Kajak2137"
                                       "\nco\n/wiki"
                                       "\nARKA GDYNIA\nZAGŁĘBIE SOSNOWIEC"
                                       "\n/poilebananywlidlu\n/poilebuleczkiwbiedrze"
                                       "\nlinux ty kurwo\n/echo"),
                          thread_id, thread_type)

            elif msg == "/kurczak":
                self.send(Message(text=lurczak()), thread_id, thread_type)
            else:
                # Sends the data to the inherited onMessage, so that we can still see when a message is recieved
                super(MabelBot, self).onMessage(author_id=author_id, message_object=message_object,
                                                thread_id=id_grupki, thread_type=thread_type, **kwargs)

        # koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend

    def on_people_added(self, user_ids):  # wywalka emilki
        if id_emilki in user_ids:
            self.removeUserFromGroup(id_emilki, id_grupki)
            self.send(Message(text='Threat neutralized'), thread_id=id_grupki, thread_type=ThreadType.GROUP)

    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):  # anty wywalka kajaka
        t = threading.Timer(1.0, self.addUsersToGroup, [removed_id, thread_id])
        t.start()


bot = MabelBot(Mabel_login, Mabel_password)
bot.listen()
