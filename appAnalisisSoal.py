from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class siswa:
    jumlah = 0
    def __init__(self, name, answer, value, fixanswer, Class):
        self.nama = name
        self.jawaban = answer
        self.hasil = value
        self.jawabanTerjemah = fixanswer
        self.kelas = Class


udin = siswa('udin',0,0,0,'XA')
samsuri = siswa('samsuri',0,0,0,'XA')
sarmin = siswa('sarmin',0,0,0,'XB')
joni = siswa('joni',0,0,0,'XB')

root = tk.Tk()
root.geometry("1000x1000")
root.configure(bg="grey")

#variable text +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
global inputJwbSiswa1
global inputJwbSiswa2
global inputJwbSiswa3
global inputJwbSiswa4
global inputKunci

kunciJawaban = tk.StringVar()
JawabanSiswa1 = tk.StringVar()
JawabanSiswa2 = tk.StringVar()
JawabanSiswa3 = tk.StringVar()
JawabanSiswa4 = tk.StringVar()

udin.jawaban = JawabanSiswa1.get()
samsuri.jawaban = JawabanSiswa2.get()
sarmin.jawaban = JawabanSiswa3.get()
joni.jawaban = JawabanSiswa4.get()

keyA = tk.StringVar()
keyB = tk.StringVar()
keyC = tk.StringVar()
keyD = tk.StringVar()
keyE = tk.StringVar()

# base function +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def pindahFrame(event):
    selected = combo.get()
    if selected == 'XA':
        xA()
    elif selected == 'XB':
        xB()
    else:
        print("pilih pilihan dengan benar")


def terjemah(y):
    udin.jawaban = JawabanSiswa1.get()
    samsuri.jawaban = JawabanSiswa2.get()
    sarmin.jawaban = JawabanSiswa3.get()
    joni.jawaban = JawabanSiswa4.get()

    a = len(y.jawaban)
    keyFormat = [keyA.get(), keyB.get(), keyC.get(), keyD.get(), keyE.get()]
    listjawaban = [y.jawaban[0], y.jawaban[1], y.jawaban[2]]
    for i in range(a):
        if (listjawaban[i] == keyFormat[0]):
            listjawaban[i] = 'a'
        elif (listjawaban[i] == keyFormat[1]):
            listjawaban[i] = 'b'
        elif (listjawaban[i] == keyFormat[2]):
            listjawaban[i] = 'c'
        elif( listjawaban[i] == keyFormat[3]):
            listjawaban[i] = 'd'
        elif (listjawaban[i] == keyFormat[4]):
            listjawaban[i] = 'e'
        else:
            listjawaban[i] = 'x'
    y.jawabanTerjemah = listjawaban
    
def fungsiKoreksi(x):
    udin.jawaban = JawabanSiswa1.get()
    samsuri.jawaban = JawabanSiswa2.get()
    sarmin.jawaban = JawabanSiswa3.get()
    joni.jawaban = JawabanSiswa4.get()
    n= len(x.jawabanTerjemah)
    kj = kunciJawaban.get()
    for i in range (n):
        if(x.jawabanTerjemah[i] == kj[i]):
            x.hasil+=1
            
        else:
            x.hasil +=0
       
def submit1():

    udin.jawaban = JawabanSiswa1.get()
    terjemah(udin)
    fungsiKoreksi(udin)

    textHasil1 = ttk.Label(frameXA, text="Hasil Udin :")
    textHasil1.pack(padx=100,pady=5,fill="x", expand=True)
    hasilSiswa1 = ttk.Label(frameXA, text=udin.hasil)
    hasilSiswa1.pack(padx=100,pady=5,fill="x", expand=True)

def submit2():

    samsuri.jawaban = JawabanSiswa2.get()
    terjemah(samsuri)
    fungsiKoreksi(samsuri)

    textHasil2 = ttk.Label(frameXA, text="Hasil Samsuri :")
    textHasil2.pack(padx=100,pady=5,fill="x", expand=True)
    hasilSiswa2 = ttk.Label(frameXA, text=samsuri.hasil)
    hasilSiswa2.pack(padx=100,pady=5,fill="x", expand=True)

def submit3():

    sarmin.jawaban = JawabanSiswa3.get()
    terjemah(sarmin)
    fungsiKoreksi(sarmin)

    textHasil3 = ttk.Label(frameXB, text="Hasil Sarmin :")
    textHasil3.pack(padx=100,pady=5,fill="x", expand=True)
    hasilSiswa3 = ttk.Label(frameXB, text=sarmin.hasil)
    hasilSiswa3.pack(padx=100,pady=5,fill="x", expand=True)

def submit4():

    joni.jawaban = JawabanSiswa4.get()
    terjemah(joni)
    fungsiKoreksi(joni)

    textHasil4 = ttk.Label(frameXB, text="Hasil Joni :")
    textHasil4.pack(padx=100,pady=5,fill="x", expand=True)
    hasilSiswa4 = ttk.Label(frameXB, text=joni.hasil)
    hasilSiswa4.pack(padx=100,pady=5,fill="x", expand=True)

# UI Domain ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# UI Domain +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# UI Domain ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# UI Domain +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    global mainFrame
    mainFrame = ttk.Frame(root)
    mainFrame.pack(padx=100,pady=10,fill="x", expand=True)
    text1 = ttk.Label(mainFrame, text="Pilih kelas yang akan dikoreksi : ")
    text1.pack(padx=100,pady=40,fill="x", expand=True)

    # UI kunci jawaban +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    lebelKunci = ttk.Label(mainFrame, text='Kunci Jawaban:')
    lebelKunci.pack(padx=100,pady=10,fill="x", expand=True)
    inputKunci = ttk.Entry(mainFrame, textvariable=kunciJawaban)
    inputKunci.pack(padx=100,pady=5,fill="x", expand=True)

    
    #UI combobox +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    global combo
    combo = ttk.Combobox(mainFrame, values=['XA','XB'])
    combo.place(x=100, y=65)
    combo.bind('<<ComboboxSelected>>', pindahFrame)

    #UI jawaban key +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    key1 = ttk.Label(mainFrame, text='A =')
    key1.pack(padx=100,pady=5,fill="x", expand=True)
    key1 = ttk.Entry(mainFrame, textvariable=keyA)
    key1.pack(padx=100,pady=5,fill="x", expand=True)

    key2 = ttk.Label(mainFrame, text='B =')
    key2.pack(padx=100,pady=5,fill="x", expand=True)
    key2 = ttk.Entry(mainFrame, textvariable=keyB)
    key2.pack(padx=100,pady=5,fill="x", expand=True)

    key3 = ttk.Label(mainFrame, text='C =')
    key3.pack(padx=100,pady=5,fill="x", expand=True)
    key3 = ttk.Entry(mainFrame, textvariable=keyC)
    key3.pack(padx=100,pady=5,fill="x", expand=True)

    key4 = ttk.Label(mainFrame, text='D =')
    key4.pack(padx=100,pady=5,fill="x", expand=True)
    key4 = ttk.Entry(mainFrame, textvariable=keyD)
    key4.pack(padx=100,pady=5,fill="x", expand=True)

    key5 = ttk.Label(mainFrame, text='E =')
    key5.pack(padx=100,pady=5,fill="x", expand=True)
    key5 = ttk.Entry(mainFrame, textvariable=keyE)
    key5.pack(padx=100,pady=5,fill="x", expand=True)

#UI jawaban siswa +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def xA():
    def pindahFokus(event):
    
        fokusSaatIni2 = frameXA.focus_get()
    
        if fokusSaatIni2 == inputJwbSiswa1:
            inputJwbSiswa2.focus_set()
            submit1()
        elif fokusSaatIni2 == inputJwbSiswa2:
            inputJwbSiswa1.focus_set()
            submit2()
        else:
            pesanSelesai = ttk.Label(mainFrame, text="Semua siswa berhasil terkoreksi")
            pesanSelesai.pack(padx=100,pady=5,fill="x", expand=True)

    global frameXA
    frameXA = ttk.Frame(root)
    frameXA.pack(padx=100,pady=5,fill="x", expand=True)

    lebelJwbSiswa1 = ttk.Label(frameXA, text='Udin:')
    lebelJwbSiswa1.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa1 = ttk.Entry(frameXA, textvariable=JawabanSiswa1)
    inputJwbSiswa1.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa1.bind('<Return>', pindahFokus)

    lebelJwbSiswa2 = ttk.Label(frameXA, text='Samsuri:')
    lebelJwbSiswa2.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa2 = ttk.Entry(frameXA, textvariable=JawabanSiswa2)
    inputJwbSiswa2.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa2.bind('<Return>', pindahFokus)

def xB():
    def pindahFokus(event):

        fokusSaatIni3 = frameXB.focus_get()

        if fokusSaatIni3 == inputJwbSiswa3:
            inputJwbSiswa4.focus_set()
            submit3()
        elif fokusSaatIni3== inputJwbSiswa4:
            inputJwbSiswa3.focus_set()
            submit4()
        else:
            pesanSelesai = ttk.Label(mainFrame, text="Semua siswa berhasil terkoreksi")
            pesanSelesai.pack(padx=100,pady=5,fill="x", expand=True)


    global frameXB
    frameXB = ttk.Frame(root)
    frameXB.pack(padx=100,pady=5,fill="x", expand=True)
    
    lebelJwbSiswa3 = ttk.Label(frameXB, text='Sarmin:')
    lebelJwbSiswa3.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa3 = ttk.Entry(frameXB, textvariable=JawabanSiswa3)
    inputJwbSiswa3.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa3.bind('<Return>', pindahFokus)

    lebelJwbSiswa4 = ttk.Label(frameXB, text='Joni:')
    lebelJwbSiswa4.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa4 = ttk.Entry(frameXB, textvariable=JawabanSiswa4)
    inputJwbSiswa4.pack(padx=100,pady=5,fill="x", expand=True)
    inputJwbSiswa4.bind('<Return>', pindahFokus)

# tombol submit ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
main()
root.mainloop()