#!/usr/bin/env python
# mpg123 lib on github
# https://github.com/20tab/mpg123-python
# icons tango icon theme

import tkinter.ttk as ttk
import tkinter
from tkinter import *
from tkinter import messagebox


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
    msg = messagebox.askyesno("Çıkış", "Çıkmak İstiyor musunuz?")
    if msg:
        Pencere.destroy()
    else:
        pass


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
TButton1.place(relx=0.01, rely=0.71, height=44, width=44)
TButton1.configure(text="Play")

TButton2 = ttk.Button(Frm1)
TButton2.place(relx=0.13, rely=0.71, height=44, width=44)
TButton2.configure(text="Stop")

TButton3 = ttk.Button(Frm1)
TButton3.place(relx=0.25, rely=0.71, height=44, width=44)
TButton3.configure(text="Next")

TButton4 = ttk.Button(Frm1)
TButton4.place(relx=0.37, rely=0.71, height=44, width=44)
TButton4.configure(text="Prev")

TButton5 = ttk.Button(Frm1)
TButton5.place(relx=0.49, rely=0.71, height=44, width=44)
TButton5.configure(text="Pause")

TButton6 = ttk.Button(Frm1)
TButton6.place(relx=0.88, rely=0.71, height=44, width=44)
TButton6.configure(text="Load")

TProgressbar1 = ttk.Progressbar(Frm1)
TProgressbar1.place(relx=0.013, rely=0.55, relwidth=0.978, relheight=0.0, height=16)
TProgressbar1.configure(length="560")


if __name__ == '__main__':
    main()
