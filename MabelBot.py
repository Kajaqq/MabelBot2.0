# This Python file uses the following encoding: utf-8
from fbchat import Client
from fbchat.models import *
import wikipedia
import re
import buleczki_lib
import subprocess

# presety
id_emilki = "100011357566074"
id_kajaka = ["100002151786860"]
id_grupki = "943760085727075"
linux_names = ["linuch", "linux", "linuks"]
love_react = ["linux to szrot", "GNU/Linux"]
mTable = []
wikipedia.set_lang("pl")
Potezny_login = ''
Potezny_password = ''

def goraca_aktualizacja(message_object, thread_id, thread_type):
    message_object.send(Message(text="Aktualizuje bota..."), thread_id, thread_type)
    subprocess.call(['./hotfix.sh'])
    exit()

def wikikurwa(term):
    term = term.decode('utf-8')
    if term == "AMD":
        wyszukiwanie = wikipedia.search(u"Kał")
        return wikipedia.summary(wyszukiwanie[0], 1)
    else:
        try:
            wyszukiwanie = wikipedia.search(term)
            return wikipedia.summary(wyszukiwanie[0], 3)
        except Exception as e:
            return "Błąd: %s" % (e)


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
        print("%s napisal: %s" % (author_id, message_object.text))  # output log
        if thread_type == ThreadType.GROUP and author_id != self.uid:

            msg = message_object.text.lower().decode('utf8')

            if msg.startswith('/add'):
                msg1 = msg.split()
                if len(msg1) > 2:
                    if msg1[1] != '/':
                        if msg1[1] not in mTable:
                            f_content = ' '.join(msg[1:])
                            f_buffer = open("gownoposty.txt", "a")
                            f_buffer.write(f_content + '\n')
                            self.send(Message(text="Added command: {:s}".format(msg[1])), thread_id, thread_type)
                            f_buffer.close()
                            read_commands()
                        else:
                            self.send(Message(text="Command already exists!"), thread_id, thread_type)
                    else:
                        self.send(Message(text="It can't be only /"), thread_id, thread_type)
                else:
                    self.send(Message(text="Three or more words needed!"), thread_id, thread_type)

            if msg[:4] == "/wiki":
                self.send(Message(text=wikikurwa(message_object.text[6:])), thread_id, thread_type)

            if msg.startswith(tuple(mTable)):
                self.send(Message(text=sendShit(message_object.text)), thread_id, thread_type)

            if msg == "/plucietotalne":
                self.sendLocalImage('plucie.gif', message=Message(text='Tfu!'),
                                    thread_id=thread_id, thread_type=thread_type)
                
            elif msg == "/update":
                goraca_aktualizacja(self, thread_id, thread_type)

            elif msg == "co":
                self.send(Message(text='jajco kurwa'), thread_id, thread_type)

            elif msg == "nk":
                self.send(Message(text='co, rąk ni mosz do roboty?'), thread_id, thread_type)

            elif msg == "arka gdynia":
                self.send(Message(text='KURWA ŚWINIA'), thread_id, thread_type)

            elif msg == "zaglebie sosnowiec":
                self.send(Message(text='KURWA BOMBOWIEC'), thread_id, thread_type)

            elif msg == "japierdole.png":
                self.sendRemoteImage('https://upload.wikimedia.org/wikipedia/commons/f/f3'
                                     '/Richard_Stallman_by_Anders_Brenna_01.jpg',
                                     message=Message(text='Stallman wlatuje'),
                                     thread_id=thread_id, thread_type=thread_type)

            elif msg == "/poilebananywlidlu":
                self.send(Message(text='3,79 zł/kg'), thread_id, thread_type)

            elif msg == "/poilebuleczkiwbiedrze":
                self.send(Message(text=buleczki_lib.buleczki()), thread_id, thread_type)

            elif msg == "reload":
                self.removeUserFromGroup(author_id, id_grupki)
                self.addUsersToGroup(author_id, id_grupki)

            elif msg == "linux to szrot" or msg == "GNU/Linux":
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.LOVE)

            elif msg == " ":
                self.send(Message(text='Gratuluje worka'), thread_id, thread_type)

            elif msg == "/help":
                self.send(Message(text="Pomoc MabelBota 2.0\nBased on d3suu's MabelBot\nModified by Kajak2137"
                                       "\nco\n/wiki\njapierdole.png\n/makeamdgreatagain"
                                       "\nARKA GDYNIA\nZAGLEBIE SOSNOWIEC"
                                       "\n/poilebananywlidlu\n/poilebuleczkiwbiedrze"
                                       "\nlinux to szrot\nKtóry POTIS najlepszy?"),
                          thread_id, thread_type)

            elif u"który potis najlepszy" in msg:
                self.send(Message(text='Ten za pobraniem'), thread_id, thread_type)

            elif re.compile('|'.join(linux_names), re.IGNORECASE).search(
                    msg) and msg != "linux to szrot" and "gnu" not in msg:
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

        else:
            # Sends the data to the inherited onMessage, so that we can still see when a message is recieved
            super(MabelBot, self).onMessage(author_id=author_id, message_object=message_object,
                                            thread_id=id_grupki, thread_type=thread_type, **kwargs)
        # koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend koniec komend

    def on_people_added(self, user_ids):  # wywalka emilki
        if id_emilki in user_ids:
            self.removeUserFromGroup(id_emilki, id_grupki)
            self.send(Message(text='Threat neutralized'), thread_id=id_grupki, thread_type=ThreadType.GROUP)

    def on_person_removed(self, user_id):  # anty wywalka kajaka
        if id_kajaka in user_id:
            self.addUsersToGroup(id_kajaka, id_grupki)
        else:
            self.addUsersToGroup(id_emilki, id_grupki)


bot = MabelBot(Potezny_login, Potezny_password)
bot.listen()
