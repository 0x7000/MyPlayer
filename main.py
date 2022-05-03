#!/usr/bin/env python
# mpg123 lib on github
# https://github.com/20tab/mpg123-python
# icons tango icon theme
from mpg123 import Mpg123, Out123
import threading
import tkinter.ttk as ttk
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os
import time


def main():
    genislik = Pencere.winfo_screenwidth()
    yukseklik = Pencere.winfo_screenheight()
    px = 420  # pencere yüksekliği
    py = 680  # # pencere genişliği
    w = int((genislik / 2) - (px / 2))
    h = int((yukseklik / 2) - (py / 2))
    ekran = "{}x{}+{}+{}".format(px, py, w, h)
    Pencere.geometry(ekran)
    Pencere.mainloop()


def destroy_me():
    global SON
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    if msg:
        SON = True
        Pencere.destroy()
    else:
        pass


def loadmp3():
    konum = fd.askdirectory()
    print(konum)
    dosyalar = os.listdir(konum)
    for i in dosyalar:
        print(i)
    print(len(dosyalar))


def player():
    global SON
    while 1:
        if SON:
            break
        if STATUS[0] == "bekle":
            time.sleep(0.5)
            print("bekliyor...")
        if STATUS[0] == "play":
            dosya = Mpg123(str(STATUS[1]))
            out = Out123()
            for frame in dosya.iter_frames(out.start):
                if STATUS[0] == "stop":
                    STATUS[0] = "bekle"
                    break
                else:
                    out.play(frame)


def playconfig(stat, filename):
    STATUS[0] = stat
    STATUS[1] = filename


SON = False
PLAYER = threading.Thread(target=player)
STATUS = ["bekle", "none"]
PLAYER.start()

Pencere = Tk()
Pencere.title("MP3 Player")
Pencere.resizable(False, False)
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

Frm1 = tkinter.Frame(Pencere)
Frm1.place(relx=0.015, rely=0.011, relheight=0.25, relwidth=0.97)
Frm1.configure(relief="groove")
Frm1.configure(border=2)

Frm2 = tkinter.Frame(Pencere)
Frm2.place(relx=0.015, rely=0.27, relheight=0.72, relwidth=0.97)
Frm2.configure(relief="groove")
Frm2.configure(border=2)

TButton1 = ttk.Button(Frm1)
TButton1.place(relx=0.01, rely=0.70, height=48, width=48)
img01 = PhotoImage(file="icons/media-playback-start.png")
TButton1.configure(command=lambda: playconfig("play", "01.mp3"))
TButton1.configure(image=img01)

TButton2 = ttk.Button(Frm1)
TButton2.place(relx=0.14, rely=0.70, height=48, width=48)
img02 = PhotoImage(file="icons/media-playback-stop.png")
TButton2.configure(command=lambda: playconfig("stop", "none"))
TButton2.configure(image=img02)

TButton3 = ttk.Button(Frm1)
TButton3.place(relx=0.27, rely=0.70, height=48, width=48)
img03 = PhotoImage(file="icons/media-skip-forward.png")
TButton3.configure(image=img03)

TButton4 = ttk.Button(Frm1)
TButton4.place(relx=0.40, rely=0.70, height=48, width=48)
img04 = PhotoImage(file="icons/media-skip-backward.png")
TButton4.configure(image=img04)

TButton5 = ttk.Button(Frm1)
TButton5.place(relx=0.53, rely=0.70, height=48, width=48)
img05 = PhotoImage(file="icons/media-playback-pause.png")
TButton5.configure(image=img05)

TButton6 = ttk.Button(Frm1)
TButton6.configure(command=loadmp3)
TButton6.place(relx=0.87, rely=0.70, height=48, width=48)
img06 = PhotoImage(file="icons/media-eject.png")
TButton6.configure(image=img06)


TProgressbar1 = ttk.Progressbar(Frm1)
TProgressbar1.place(relx=0.011, rely=0.58, relwidth=0.978, relheight=0.0, height=16)
TProgressbar1.configure(length="560")

TLabel1 = ttk.Label(Frm1)
TLabel1.place(relx=0.01, rely=0.01, height=48, width=99)
TLabel1.configure(font="-family {Noto Sans} -size 28")
TLabel1.configure(relief="flat")
TLabel1.configure(text="00:00")

TLabel2 = ttk.Label(Frm1)
TLabel2.place(relx=0.01, rely=0.28, height=48, width=200)
TLabel2.configure(font="-family {Noto Sans} -size 16")
TLabel2.configure(relief="flat")
TLabel2.configure(text="ARTIST:")

TLabel3 = ttk.Label(Frm1)
TLabel3.place(relx=0.26, rely=0.01, height=28, width=280)
TLabel3.configure(font="-family {Noto Sans} -size 16")
TLabel3.configure(relief="flat")
TLabel3.configure(text="SONG NAME")

if __name__ == '__main__':
    main()
