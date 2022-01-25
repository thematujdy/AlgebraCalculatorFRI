import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import numpy as np
import os
import sys
from fractions import Fraction

version = "0.2"


# https://mega.nz/aff=2-GnMfDZGJo

# pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)


# float converter
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


# Error dialog
def error_dialog(msg):
    mb.showerror("Error", msg)


# combobox canvas
def make_combobox():
    canvas1.create_window(canvas_x + 70, canvas_y + 9, window=calculator_cb)


# okno
win = tk.Tk()
win.title("Algebra Calculator FRI Edition ver: " + version)
win.iconbitmap(resource_path('fri.ico'))
canvas1 = tk.Canvas(win, width=800, height=500)
canvas1.pack()
canvas_x = canvas1.winfo_width()
canvas_y = canvas1.winfo_height()
selected_calculator = tk.StringVar()
calculator_cb = ttk.Combobox(win, textvariable=selected_calculator)
calculator_cb['values'] = ('3x3 Matice', '4x4 Matice')
calculator_cb['state'] = 'readonly'
make_combobox()


# nakresli vybrane okno na canvas
def make_window(event):
    match calculator_cb.get():
        case '3x3 Matice':
            canvas1.delete("all")
            make_combobox()
            matice3X3()
            return
        case '4x4 Matice':
            canvas1.delete("all")
            make_combobox()
            return
        case _:
            canvas1.delete("all")
            make_combobox()
            return


calculator_cb.bind('<<ComboboxSelected>>', make_window)


# okno na počítanie 3x3 matíc
class matice3X3:
    def __init__(self):
        # prvá matica 3x3
        self.entry1 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 100, canvas_y + 100, window=self.entry1)
        self.entry2 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 150, canvas_y + 100, window=self.entry2)
        self.entry3 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 200, canvas_y + 100, window=self.entry3)
        self.entry4 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 100, canvas_y + 150, window=self.entry4)
        self.entry5 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 150, canvas_y + 150, window=self.entry5)
        self.entry6 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 200, canvas_y + 150, window=self.entry6)
        self.entry7 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 100, canvas_y + 200, window=self.entry7)
        self.entry8 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 150, canvas_y + 200, window=self.entry8)
        self.entry9 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 200, canvas_y + 200, window=self.entry9)

        # druha matica 3x3
        self.entry10 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 350, canvas_y + 100, window=self.entry10)
        self.entry11 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 400, canvas_y + 100, window=self.entry11)
        self.entry12 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 450, canvas_y + 100, window=self.entry12)
        self.entry13 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 350, canvas_y + 150, window=self.entry13)
        self.entry14 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 400, canvas_y + 150, window=self.entry14)
        self.entry15 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 450, canvas_y + 150, window=self.entry15)
        self.entry16 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 350, canvas_y + 200, window=self.entry16)
        self.entry17 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 400, canvas_y + 200, window=self.entry17)
        self.entry18 = tk.Entry(win, width=4)
        canvas1.create_window(canvas_x + 450, canvas_y + 200, window=self.entry18)

        # label výsledku
        self.var1 = tk.StringVar()
        self.output1 = tk.Label(win, textvariable=self.var1)
        canvas1.create_window(canvas_x + 600, canvas_y + 100, window=self.output1)
        self.var2 = tk.StringVar()
        self.output2 = tk.Label(win, textvariable=self.var2)
        canvas1.create_window(canvas_x + 650, canvas_y + 100, window=self.output2)
        self.var3 = tk.StringVar()
        self.output3 = tk.Label(win, textvariable=self.var3)
        canvas1.create_window(canvas_x + 700, canvas_y + 100, window=self.output3)
        self.var4 = tk.StringVar()
        self.output4 = tk.Label(win, textvariable=self.var4)
        canvas1.create_window(canvas_x + 600, canvas_y + 150, window=self.output4)
        self.var5 = tk.StringVar()
        self.output5 = tk.Label(win, textvariable=self.var5)
        canvas1.create_window(canvas_x + 650, canvas_y + 150, window=self.output5)
        self.var6 = tk.StringVar()
        self.output6 = tk.Label(win, textvariable=self.var6)
        canvas1.create_window(canvas_x + 700, canvas_y + 150, window=self.output6)
        self.var7 = tk.StringVar()
        self.output7 = tk.Label(win, textvariable=self.var7)
        canvas1.create_window(canvas_x + 600, canvas_y + 200, window=self.output7)
        self.var8 = tk.StringVar()
        self.output8 = tk.Label(win, textvariable=self.var8)
        canvas1.create_window(canvas_x + 650, canvas_y + 200, window=self.output8)
        self.var9 = tk.StringVar()
        self.output9 = tk.Label(win, textvariable=self.var9)
        canvas1.create_window(canvas_x + 700, canvas_y + 200, window=self.output9)

        # uloží matice
        def daj_matice():
            # deklaracia prvej matice
            try:
                try:
                    a1 = convert_to_float(self.entry1.get())
                except:
                    a1 = 0

                try:
                    a2 = convert_to_float(self.entry2.get())
                except:
                    a2 = 0

                try:
                    a3 = convert_to_float(self.entry3.get())
                except:
                    a3 = 0

                try:
                    a4 = convert_to_float(self.entry4.get())
                except:
                    a4 = 0

                try:
                    a5 = convert_to_float(self.entry5.get())
                except:
                    a5 = 0

                try:
                    a6 = convert_to_float(self.entry6.get())
                except:
                    a6 = 0

                try:
                    a7 = convert_to_float(self.entry7.get())
                except:
                    a7 = 0

                try:
                    a8 = convert_to_float(self.entry8.get())
                except:
                    a8 = 0

                try:
                    a9 = convert_to_float(self.entry9.get())
                except:
                    a9 = 0

                self.arr1 = np.array([[a1, a2, a3],
                                      [a4, a5, a6],
                                      [a7, a8, a9]])

            except:
                error_dialog("Chyba pri deklarovaní prvej matice.")
                return

            # deklaracia druhej matice
            try:
                try:
                    b1 = convert_to_float(self.entry10.get())
                except:
                    b1 = 0

                try:
                    b2 = convert_to_float(self.entry11.get())
                except:
                    b2 = 0

                try:
                    b3 = convert_to_float(self.entry12.get())
                except:
                    b3 = 0

                try:
                    b4 = convert_to_float(self.entry13.get())
                except:
                    b4 = 0

                try:
                    b5 = convert_to_float(self.entry14.get())
                except:
                    b5 = 0

                try:
                    b6 = convert_to_float(self.entry15.get())
                except:
                    b6 = 0

                try:
                    b7 = convert_to_float(self.entry16.get())
                except:
                    b7 = 0

                try:
                    b8 = convert_to_float(self.entry17.get())
                except:
                    b8 = 0

                try:
                    b9 = convert_to_float(self.entry18.get())
                except:
                    b9 = 0
                self.arr2 = np.array([[b1, b2, b3],
                                      [b4, b5, b6],
                                      [b7, b8, b9]])

            except:
                error_dialog("Chyba pri deklarovaní druhej matice.")
                return

        # napise vysledok
        def vysledok(arr):
            self.var1.set(Fraction(arr[0, 0]).limit_denominator())
            self.var2.set(Fraction(arr[0, 1]).limit_denominator())
            self.var3.set(Fraction(arr[0, 2]).limit_denominator())
            self.var4.set(Fraction(arr[1, 0]).limit_denominator())
            self.var5.set(Fraction(arr[1, 1]).limit_denominator())
            self.var6.set(Fraction(arr[1, 2]).limit_denominator())
            self.var7.set(Fraction(arr[2, 0]).limit_denominator())
            self.var8.set(Fraction(arr[2, 1]).limit_denominator())
            self.var9.set(Fraction(arr[2, 2]).limit_denominator())
            print(arr)

        # pripočítanie 3x3 matíc
        def pripocitaj():
            daj_matice()
            try:
                arr = np.add(self.arr1, self.arr2)
                vysledok(arr)

            except:
                error_dialog("Chyba pri pripočítavaní matíc.")
                return

        # odpočítanie 3x3 matíc
        def odpocitaj():
            daj_matice()
            try:
                arr = np.subtract(self.arr1, self.arr2)
                vysledok(arr)

            except:
                error_dialog("Chyba pri odpočítavaní matíc.")
                return

        # násobenie 3x3 matíc
        def nasob():
            daj_matice()
            try:
                arr = np.multiply(self.arr1, self.arr2)
                vysledok(arr)

            except:
                error_dialog("Chyba pri násobení matíc.")
                return

        # delenie 3x3 matíc
        def delenie():
            daj_matice()
            try:
                arr = np.divide(self.arr1, self.arr2)
                vysledok(arr)

            except:
                error_dialog("Chyba pri delení matíc.")
                return

        # transponovanie
        def transponuj_prvu():
            daj_matice()
            try:
                self.var1.set(Fraction(self.arr1[0, 0]).limit_denominator())
                self.var2.set(Fraction(self.arr1[1, 0]).limit_denominator())
                self.var3.set(Fraction(self.arr1[2, 0]).limit_denominator())
                self.var4.set(Fraction(self.arr1[0, 1]).limit_denominator())
                self.var5.set(Fraction(self.arr1[1, 1]).limit_denominator())
                self.var6.set(Fraction(self.arr1[2, 1]).limit_denominator())
                self.var7.set(Fraction(self.arr1[0, 2]).limit_denominator())
                self.var8.set(Fraction(self.arr1[1, 2]).limit_denominator())
                self.var9.set(Fraction(self.arr1[2, 2]).limit_denominator())
            except:
                error_dialog("Chyba pri transponovaní.")

        def transponuj_druhu():
            daj_matice()
            try:
                self.var1.set(Fraction(self.arr2[0, 0]).limit_denominator())
                self.var2.set(Fraction(self.arr2[1, 0]).limit_denominator())
                self.var3.set(Fraction(self.arr2[2, 0]).limit_denominator())
                self.var4.set(Fraction(self.arr2[0, 1]).limit_denominator())
                self.var5.set(Fraction(self.arr2[1, 1]).limit_denominator())
                self.var6.set(Fraction(self.arr2[2, 1]).limit_denominator())
                self.var7.set(Fraction(self.arr2[0, 2]).limit_denominator())
                self.var8.set(Fraction(self.arr2[1, 2]).limit_denominator())
                self.var9.set(Fraction(self.arr2[2, 2]).limit_denominator())
            except:
                error_dialog("Chyba pri transponovaní.")

        # trojuholnikovy tvar matice
        def daj_trojuholnik_prvej():
            daj_matice()
            try:
                # 1. krok
                x1 = self.arr1[0, 0] * ((0 - self.arr1[1, 0]) / self.arr1[0, 0])
                x2 = self.arr1[0, 1] * ((0 - self.arr1[1, 0]) / self.arr1[0, 0])
                x3 = self.arr1[0, 2] * ((0 - self.arr1[1, 0]) / self.arr1[0, 0])
                v1 = self.arr1[1, 0] + x1
                v2 = self.arr1[1, 1] + x2
                v3 = self.arr1[1, 2] + x3
                m_arr1 = np.array([[Fraction(self.arr1[0, 0]).limit_denominator(),
                                    Fraction(self.arr1[0, 1]).limit_denominator(),
                                    Fraction(self.arr1[0, 2]).limit_denominator()],
                                   [Fraction(v1).limit_denominator(),
                                    Fraction(v2).limit_denominator(),
                                    Fraction(v3).limit_denominator()],
                                   [Fraction(self.arr1[2, 0]).limit_denominator(),
                                    Fraction(self.arr1[2, 1]).limit_denominator(),
                                    Fraction(self.arr1[2, 2]).limit_denominator()]])
                # 2. krok
                x1 = self.arr1[0, 0] * ((0 - self.arr1[2, 0]) / self.arr1[0, 0])
                x2 = self.arr1[0, 1] * ((0 - self.arr1[2, 0]) / self.arr1[0, 0])
                x3 = self.arr1[0, 2] * ((0 - self.arr1[2, 0]) / self.arr1[0, 0])
                v1 = self.arr1[2, 0] + x1
                v2 = self.arr1[2, 1] + x2
                v3 = self.arr1[2, 2] + x3
                m_arr2 = np.array([[Fraction(m_arr1[0, 0]).limit_denominator(),
                                    Fraction(m_arr1[0, 1]).limit_denominator(),
                                    Fraction(m_arr1[0, 2]).limit_denominator()],
                                   [Fraction(m_arr1[1, 0]).limit_denominator(),
                                    Fraction(m_arr1[1, 1]).limit_denominator(),
                                    Fraction(m_arr1[1, 2]).limit_denominator()],
                                   [Fraction(v1).limit_denominator(),
                                    Fraction(v2).limit_denominator(),
                                    Fraction(v3).limit_denominator()]])
                # 3. krok
                x1 = m_arr2[1, 0] * ((0 - m_arr2[2, 1]) / m_arr2[1, 1])
                x2 = m_arr2[1, 1] * ((0 - m_arr2[2, 1]) / m_arr2[1, 1])
                x3 = m_arr2[1, 2] * ((0 - m_arr2[2, 1]) / m_arr2[1, 1])
                v1 = m_arr2[2, 0] + x1
                v2 = m_arr2[2, 1] + x2
                v3 = m_arr2[2, 2] + x3
                m_arr3 = np.array([[Fraction(m_arr2[0, 0]).limit_denominator(),
                                    Fraction(m_arr2[0, 1]).limit_denominator(),
                                    Fraction(m_arr2[0, 2]).limit_denominator()],
                                   [Fraction(m_arr2[1, 0]).limit_denominator(),
                                    Fraction(m_arr2[1, 1]).limit_denominator(),
                                    Fraction(m_arr2[1, 2]).limit_denominator()],
                                   [Fraction(v1).limit_denominator(),
                                    Fraction(v2).limit_denominator(),
                                    Fraction(v3).limit_denominator()]])
                vysledok(m_arr3)
            except:
                error_dialog("Chyba pri počítaní hodnosti matice.")

        # hodnost matice
        def daj_hodnost_prvej():
            daj_trojuholnik_prvej()

        # tlačidlá
        self.button_add = tk.Button(win, text="Spočítať", command=pripocitaj)
        canvas1.create_window(canvas_x + 525, canvas_y + 250, window=self.button_add)
        self.button_sub = tk.Button(win, text="Odpočítať", command=odpocitaj)
        canvas1.create_window(canvas_x + 530, canvas_y + 275, window=self.button_sub)
        self.button_mul = tk.Button(win, text="Násobiť", command=nasob)
        canvas1.create_window(canvas_x + 524, canvas_y + 300, window=self.button_mul)
        self.button_div = tk.Button(win, text="Deliť", command=delenie)
        canvas1.create_window(canvas_x + 516, canvas_y + 325, window=self.button_div)
        self.button_tr1 = tk.Button(win, text="Transponovať", command=transponuj_prvu)
        canvas1.create_window(canvas_x + 175, canvas_y + 250, window=self.button_tr1)
        self.button_tr2 = tk.Button(win, text="Transponovať", command=transponuj_druhu)
        canvas1.create_window(canvas_x + 425, canvas_y + 250, window=self.button_tr2)
        self.button_hod1 = tk.Button(win, text="Hodnosť", command=daj_hodnost_prvej)
        canvas1.create_window(canvas_x + 188, canvas_y + 276, window=self.button_hod1)

    def __del__(self):
        return


win.mainloop()
