# This Python file uses the following encoding: utf-8
from fbchat import Client
from fbchat.models import *
import wikipedia
import re

# presety
id_emilki = "100011357566074"
id_kajaka = ["100002151786860"]
id_grupki = "943760085727075"
linux_names = ["gnu/linux" ,"linux"]
loop = False
wikipedia.set_lang("pl")
Potezny_login = ''
Potezny_password = ''


def wikikurwa(term):
    if term == "AMD":
        wyszukiwanie = wikipedia.search("Kał")
        return wikipedia.summary(wyszukiwanie[0], 1)
    else:
        try:
            wyszukiwanie = wikipedia.search(term)
            return wikipedia.summary(wyszukiwanie[0], 3)
        except Exception as e:
            return "Błąd: %s" % (e)


class MabelBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        print("%s napisal: %s" % (author_id, message_object.text))  # output log
        if thread_type == ThreadType.GROUP and author_id != self.uid:
            if "/wiki" in message_object.text:
                self.send(Message(text=wikikurwa(message_object.text[6:])), thread_id, thread_type)
            elif message_object.text == "co":
                self.send(Message(text='jajco kurwa'), thread_id, thread_type)
            elif message_object.text == "nk":
             self.send(Message(text='co, rąk ni mosz do roboty?'), thread_id, thread_type)
            elif message_object.text == "ARKA GDYNIA":
                self.send(Message(text='KURWA ŚWINIA'), thread_id, thread_type)
            elif message_object.text == "ZAGLEBIE SOSNOWIEC":
                self.send(Message(text='KURWA BOMBOWIEC'), thread_id, thread_type)
            elif message_object.text == "japierdole.png":
                self.sendRemoteImage('https://upload.wikimedia.org/wikipedia/commons/f/f3'
                                 '/Richard_Stallman_by_Anders_Brenna_01.jpg',
                                 message=Message(text='Stallman wlatuje'),
                                 thread_id=thread_id, thread_type=thread_type)
            elif message_object.text == "/poilebananywlidlu":
                self.send(Message(text='3,79 zł/kg'), thread_id, thread_type)
            elif message_object.text == "/poilebuleczkiwbiedrze":
                self.send(Message(text='0,49 zł/szt.'), thread_id, thread_type)
            elif message_object.text == "reload":
                self.removeUserFromGroup(author_id, id_grupki)
                self.addUsersToGroup(author_id, id_grupki)
            elif message_object.text == "linux to szrot" or message_object.text == "GNU/Linux":
                self.reactToMessage(message_id=message_object.uid, reaction=MessageReaction.LOVE)
            elif message_object.text == u" ":
                self.send(Message(text='Gratuluje worka'), thread_id, thread_type)
            elif message_object.text == "/help":
                self.send(Message(text="Pomoc MabelBota 2.0\nBased on d3suu's MabelBot\nModified by Kajak2137"
                                       "\nco\n/wikipedia\njapierdole.png\n/makeamdgreatagain"
                                       "\nARKA GDYNIA\nZAGLEBIE SOSNOWIEC"
                                       "\n/poilebananywlidlu\n/poilebuleczkiwbiedrze"
                                       "\nlinux to szrot\nKtóry POTIS najlepszy?"),
                        thread_id, thread_type)
            elif "który potis najlepszy" in message_object.text.lower():
                self.send(Message(text='Ten za pobraniem'), thread_id, thread_type)
            elif re.compile('|'.join(linux_names), re.IGNORECASE).search(message_object.text) and message_object.text != "linux to szrot":
                self.send(Message (text="I'd just like to interject for a moment. What you’re referring to as Linux, "
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
            elif "linux" in message_object.text.lower():
                self.send(Message(text='GNU/Linux*'), thread_id, thread_type)
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
