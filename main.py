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
import time
import eyed3


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


def destroy_me():
    global SON
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    if msg:
        STATUS[0] = "stop"
        SON = True
        Pencere.destroy()
    else:
        pass


def loadmp3():
    STATUS[0] = "stop"
    global FILENAME
    FILENAME = fd.askopenfilename()
    if FILENAME:
        playconfig("play", FILENAME)
        print(FILENAME)
    else:
        pass


def tagreader(filename):
    audiofile = eyed3.load(filename)
    artist = audiofile.tag.artist
    song = audiofile.tag.title
    TLabel1.configure(text=song)
    TLabel2.configure(text=artist)


def player():
    global SON
    while 1:
        if SON:
            break
        if STATUS[0] == "bekle":
            time.sleep(0.5)
            # print("bekliyor...")
            pass
        if STATUS[0] == "play":
            tagreader(STATUS[1])
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
FILENAME = ""
PLAYER.start()

Pencere = Tk()
Pencere.title("MP3 Player")
Pencere.resizable(False, False)
Pencere.protocol('WM_DELETE_WINDOW', destroy_me)

Frm1 = tkinter.Frame(Pencere)
Frm1.place(relx=0.015, rely=0.011, relheight=0.95, relwidth=0.97)
Frm1.configure(relief="groove")
Frm1.configure(border=2)


TButton1 = ttk.Button(Frm1)
TButton1.place(relx=0.01, rely=0.70, height=48, width=48)
img01 = PhotoImage(file="icons/media-playback-start.png")
TButton1.configure(command=lambda: playconfig("play", FILENAME))
TButton1.configure(image=img01)

TButton2 = ttk.Button(Frm1)
TButton2.place(relx=0.14, rely=0.70, height=48, width=48)
img02 = PhotoImage(file="icons/media-playback-stop.png")
TButton2.configure(command=lambda: playconfig("stop", "none"))
TButton2.configure(image=img02)

TButton3 = ttk.Button(Frm1)
TButton3.configure(command=loadmp3)
TButton3.place(relx=0.87, rely=0.70, height=48, width=48)
img03 = PhotoImage(file="icons/media-eject.png")
TButton3.configure(image=img03)

TLabel1 = ttk.Label(Frm1)
TLabel1.place(relx=0.01, rely=0.3, height=48, width=380)
TLabel1.configure(font="-family {Noto Sans} -size 14")
TLabel1.configure(relief="flat")
TLabel1.configure(text="ARTIST:")

TLabel2 = ttk.Label(Frm1)
TLabel2.place(relx=0.01, rely=0.1, height=32, width=380)
TLabel2.configure(font="-family {Noto Sans} -size 14")
TLabel2.configure(relief="flat")
TLabel2.configure(text="SONG NAME")

if __name__ == '__main__':
    main()
