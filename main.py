#!/usr/bin/env python
# mpg123 lib on github
# https://github.com/20tab/mpg123-python
# mit licanse

from mpg123 import Mpg123, Out123
from tkinter import *
from tkinter import messagebox
from time import sleep
import threading


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 420  # pencere yüksekliği
    py = 180  # # pencere genişliği
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def baslat():
    global STOP
    STOP = False
    say = threading.Thread(target=sayac)
    say.start()
    play = threading.Thread(target=player, args=("test.mp3",))
    play.start()


def durdur():
    global STOP
    STOP = True


def sayac():
    saniye = 0
    dakika = 0
    while 1:
        global STOP
        if STOP:
            saniye = 0
            dakika = 0
            Sure_label.config(text=str("{0:0=2d}".format(dakika)) + ":" + str("{0:0=2d}".format(saniye)))
            Play_label2.config(text="?")
            break
        else:
            Sure_label.config(text=str("{0:0=2d}".format(dakika)) + ":" + str("{0:0=2d}".format(saniye)))
            saniye += 1
            if saniye == 59:
                dakika += 1
                saniye = 0
        sleep(1)


def player(dosya):
    Play_label2.config(text=dosya)
    mp3 = Mpg123(dosya)
    out = Out123()
    for frame in mp3.iter_frames(out.start):
        global STOP
        if STOP:
            break
        else:
            out.play(frame)
    STOP = True


def destroy_me():
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    # print(msg)  # msg true ise yes değilse no
    if msg:
        global STOP
        STOP = True
        Pencere.destroy()
        # .destroy pencereyi ve bekleyen işlemleri sonlandırıcak,
        # sonlandırmadan evvel bekleyen işlemlerin kapanmasını veya bitmesini beklemekte fayda var
    else:
        pass


Pencere = Tk()
Pencere.title("Player")
Pencere.resizable(False, False)
# Pencere kapatılırken, destroy_me adlı fonksiyonu çağır.
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

Sure_label = Label(Pencere, text="00:00", font=("terminus", 28))
Sure_label.place(x=10, y=10)

Play_label = Label(Pencere, text="Now Playing.")
Play_label.place(x=10, y=50)

Play_label2 = Label(Pencere, text="?")
Play_label2.place(x=100, y=50)

play_button = Button(Pencere, text="Play", command=baslat)
play_button.place(x=150, y=14)

stop_button = Button(Pencere, text="Stop", command=durdur)
stop_button.place(x=205, y=14)

stop_button = Button(Pencere, text="Next")
stop_button.place(x=265, y=14)

STOP = False

if __name__ == '__main__':
    main()
