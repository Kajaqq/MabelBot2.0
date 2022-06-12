# This Python file uses the following encoding: utf-8
import subprocess

import wikipedia
from fbchat import Client
from fbchat.models import *

import buleczki_lib
from d3s_lib import gitgud
# presety
from MabelPassy import MabelConfig
from MemeHandler import MemeHandler
from most_lib import czymostjestotwarty
from thicc_lib import thiccify

id_grupki = MabelConfig.id_grupki
banned_ids = MabelConfig.bannned_ids
linux_names = ["linuch", "linux", "linuks"]
love_react = ["linux to szrot", "linux ty kurwo jebana", "gnu/linux"]
mTable = []
wikipedia.set_lang("pl")
Mabel_login = MabelConfig.login
Mabel_password = MabelConfig.password


def goraca_aktualizacja(message_object, thread_id, thread_type):
    message_object.send(Message(text="Aktualizuję bota..."), thread_id, thread_type)
    subprocess.call(['chmod', '+x', 'hotfix.sh'])
    subprocess.call(['./hotfix.sh'])
    exit()


def wiki_search(term):
    if term == "AMD":
        wyszukiwanie = wikipedia.search("Kał")
        return wikipedia.summary(wyszukiwanie[0], 1)
    else:
        try:
            wyszukiwanie = wikipedia.search(term)
            return wikipedia.summary(wyszukiwanie[0], 3)
        except Exception as e:
            return f"Błąd: {e}"


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
        print(f"{author_id} napisał: {message_object.text}")  # output log
        if thread_type == ThreadType.GROUP and author_id not in banned_ids and author_id != self.uid and thread_id == id_grupki:

            msg = message_object.text.lower()

            if msg.startswith('/add'):
                msg1 = msg.split()
                if len(msg1) > 2:
                    if msg1[1] != '/':
                        if msg1[1] not in mTable:
                            f_content = ' '.join(msg[4:])
                            f_buffer = open("gownoposty.txt", "a")
                            f_buffer.write(f_content + '\n')
                            self.send(Message(text="Dodałem: {:s}".format(msg[1])), thread_id, thread_type)
                            f_buffer.close()
                            read_commands()
                        else:
                            self.send(Message(text="Komenda już istnieje"), thread_id, thread_type)
                    else:
                        self.send(Message(text="Nie możesz dać samego /"), thread_id, thread_type)
                else:
                    self.send(Message(text="Trzy lub więcej słowa potrzebne"), thread_id, thread_type)

            elif msg.startswith("/wiki"):
                self.send(Message(text=wiki_search(message_object.text[6:])), thread_id, thread_type)

            elif msg.startswith(tuple(mTable)):
                self.send(Message(text=sendShit(message_object.text)), thread_id, thread_type)

            elif msg == "/update":
                goraca_aktualizacja(self, thread_id, thread_type)

            elif msg.startswith("/git"):
                self.send(Message(text=gitgud(msg[5:])), thread_id, thread_type)

            elif msg == "/czymostjestotwarty":
                self.send(Message(text=czymostjestotwarty()), thread_id, thread_type)

            elif msg == "co":
                self.send(Message(text='jajco kurwa'), thread_id, thread_type)

            elif msg == "nk":
                self.send(Message(text='co, rąk ni mosz do roboty?'), thread_id, thread_type)

            elif msg == "arka gdynia":
                self.send(Message(text='KURWA ŚWINIA'), thread_id, thread_type)

            elif msg == "zagłębie sosnowiec":
                self.send(Message(text='KURWA BOMBOWIEC'), thread_id, thread_type)

            elif msg == "łódź bałuty":
                self.sendRemoteImage('http://www33.patrz.pl/u/f/29/39/76/293976.jpg',
                                     thread_id=thread_id, thread_type=thread_type)

            elif msg == "japierdole.png":
                self.sendRemoteImage('https://upload.wikimedia.org/wikipedia/commons/f/f3'
                                     '/Richard_Stallman_by_Anders_Brenna_01.jpg',
                                     message=Message(text='Stallman wlatuje'),
                                     thread_id=thread_id, thread_type=thread_type)

            elif msg == "/poilebuleczkiwbiedrze":
                self.send(Message(text=buleczki_lib.buleczki()), thread_id, thread_type)

            elif msg == "reload":
                self.removeUserFromGroup(author_id, id_grupki)
                self.addUsersToGroup(author_id, id_grupki)

            elif msg in love_react:
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.LOVE)

            elif msg == "/help":
                self.send(Message(text="Pomoc MabelBota 2.0\nBased on d3suu's MabelBot\nModified by Kajaqq"
                                       "\nco\n/wiki\njapierdole.png"
                                       "\nARKA GDYNIA\nZAGŁĘBIE SOSNOWIEC"
                                       "\n/poilebuleczkiwbiedrze"
                                       "\nlinux to szrot\n/update\n/git\n/czymostjestotwarty"),
                          thread_id, thread_type)

            elif "linuxp" in msg:
                self.send(Message(text="I'd just like to interject for a moment. What you’re referring to as Linux, "
                                       "is in fact, GNU/Linux, or as I’ve recently taken to calling it, "
                                       "GNU plus Linux. Linux is not an operating system unto itself, but rather "
                                       "another free component of a fully functioning GNU system made useful by the "
                                       "GNU corelibs, shell utilities and vital system components comprising a full "
                                       "OS as defined by POSIX. "
                                       "Many computer users run a modified version of the GNU system every day, "
                                       "without realizing it. Through a peculiar turn of events, the version of GNU "
                                       "which is widely used today is often called “Linux”, and many of its users "
                                       "are not aware that it is basically the GNU system, developed by the GNU "
                                       "Project. There really is a Linux, and these people are using it, "
                                       "but it is just a part of the system they use. "
                                       "Linux is the kernel: the program in the system that allocates the machine’s "
                                       "resources to the other programs that you run. The kernel is an essential "
                                       "part of an operating system, but useless by itself; it can only function in "
                                       "the context of a complete operating system. Linux is normally used in "
                                       "combination with the GNU operating system: the whole system is basically GNU "
                                       "with Linux added, or GNU/Linux. All the so-called “Linux” distributions are"
                                       "really distributions of GNU/Linux"), thread_id, thread_type)

            elif msg.startswith("/thiccify"):
                self.send(Message(text=thiccify(message_object.text[10:])), thread_id, thread_type)

            elif msg.startswith("/meme"):
                memeStuff = MemeHandler(msg[6:])
                self.sendRemoteImage(memeStuff[1], Message(text=memeStuff[0]), thread_id, thread_type)
        else:
            # Sends the data to the inherited onMessage, so that we can still see when a message is recieved
            super(MabelBot, self).onMessage(author_id=author_id, message_object=message_object,
                                            thread_id=id_grupki, thread_type=thread_type, **kwargs)
        # koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec

bot = MabelBot(Mabel_login, Mabel_password)
bot.send(Message(text='Jestem!'), thread_id=id_grupki, thread_type=ThreadType.GROUP)
bot.listen()
