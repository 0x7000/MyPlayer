#!/usr/bin/env python
# mpg123 lib on github
# https://github.com/20tab/mpg123-python
# icons tango icon theme

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


if __name__ == '__main__':
    main()
