import tkinter as tk
from tkinter import colorchooser
import random
from PIL import Image
from tkinter.filedialog import asksaveasfile

window = tk.Tk()
window.title("Paint")

x = 0
y = 0

prepinac = ""
pred_prepinac = ""
farba = "#000"

# PRÍPRAVA PRE ZOBRAZENIE IKON, VYTVORÍME SI DVA LISTY -- JEDEN SO SVETLÝMI A DRUHÝ S TMAVÝMI (STLAČENÝMI) IKONAMY
ikony = ["sprej.png", "stvorec.png", "kruh.png", "farba.png", "ciara.png", "stetec.png", "vymazat.png", "ulozit.png"]
tlacidla = ["sprej", "stvorec", "kruh", "farba", "ciara", "stetec", "vymazat", "ulozit"]
ikony.sort()
tlacidla.sort()

ikony_subory = []
ikony_tmave = []
for i in range(8):
    img = tk.PhotoImage(file=f"./icons/{ikony[i]}")
    ikony_subory.append(img)

for i in range(8):
    img = tk.PhotoImage(file=f"./icons_dark/{ikony[i]}")
    ikony_tmave.append(img)


# VYTVORÍME CANVAS KDE BUDEME KRESLIŤ
plocha = tk.Canvas(width=440, height=400, bg="white")
plocha.grid(row=1, column=0, columnspan=8)

# JEDNODUCHÁ FUNKCIA, KTORÁ ZISTÍ, AKÁ IKONA BOLA STLAČENÁ A PODÁ TÚTO INFORMÁCIU ĎALŠEJ FUNKCII 
def zmen_ikonu(prepinac):
    ikona = f"{prepinac}.png"
    index = ikony.index(ikona)
    zobrazit_tlacidla(index)

# HLAVNÁ FUNKCIA NA PREPÍNANIE FUNKCIÍ
def prepnut(volba):

    ## Voľba prepínača aby sme mohli vybrať správnu funkcionalitu ##
    global prepinac
    global pred_prepinac
    pred_prepinac = prepinac
    if prepinac == volba:
        zobrazit_tlacidla()
        prepinac = ""
        return
    else:
        prepinac = volba

    ## Funkcionality, ktoré nekreslia, sa udejú tu ##

    if prepinac == "farba":
        global farba
        pred_farba = farba
        rgb, farba = colorchooser.askcolor(title ="Vyber farbu") # Output je v hexadecimálnej sústave
        if farba == None:
            farba = pred_farba
        prepinac = pred_prepinac

    elif prepinac == "vymazat":
        plocha.delete("all")
        prepinac = pred_prepinac

    elif prepinac == "ulozit":
        plocha.postscript(file="kresba.eps")
        img = Image.open("kresba.eps")
        file = asksaveasfile(defaultextension = ".png")
        img.save(file.name)
        prepinac = ""
        zobrazit_tlacidla()

    # O ostatné funkcionality, ktoré sú dynamické, sa postaráme nižšie, tu len zmeníme ikonu na aktívnu
    else:
        zmen_ikonu(prepinac)



## VYTVÁRANIE A RENDEROVANIE TLAČIDIEL, AK JE INPUT NEŠPECIFIKOVANÝ, VŠETKY IKONY BUDÚ BIELE##
def zobrazit_tlacidla(volba=10):
    for i in range(8):
        if i == volba:
            b = tk.Button(image=ikony_tmave[i], width=50, command= lambda i=i: prepnut(tlacidla[i]))
            b.grid(row=0, column=i)
        else:
            b = tk.Button(image=ikony_subory[i], width=50, command= lambda i=i: prepnut(tlacidla[i]))
            b.grid(row=0, column=i)

# PRVOTNÉ RENDEROVANIE TLAČIDIEL
zobrazit_tlacidla()

# PO KLIKNUTÍ ZAPÍŠEME SÚRADNICE PÔVODNÉHO KLIKU
def klik(e):

    ## Do globálnych premenných x a y sa uložia súradnice miesta kliku ##

    global x,y
    x=e.x 
    y=e.y

# DYNAMICKY REAGUJEME NA SÚRADNICE MYŠI A PRIEBEŽNE RENDERUJEME TVAR PODĽA VÝBERU PREPÍNAČA
def hyb(e):
    global x,y
    global farba

    ## Do každej funkcie, ktorá niečo kreslí, máte 3 vstupy: originálne súradnice kliku, súradnice aktuálnej pozície stlačenej myše a farbu ##

    if prepinac == "sprej":
        for i in range(100):
            sx = random.randint(-13, 13)
            sy = random.randint(-13, 13)
            plocha.create_line(e.x+sx, e.y+sy, e.x+sx+1, e.y+sy, fill=farba)

    elif prepinac == "stvorec":
        plocha.delete("stvorec")
        plocha.create_rectangle(x, y, e.x, e.y, fill = farba, outline = farba, tag = "stvorec")

    elif prepinac == "kruh":
        plocha.delete("kruh")
        plocha.create_oval(x, y, e.x, e.y, fill = farba, outline = farba, tag = "kruh")

    elif prepinac == "ciara":
        plocha.delete("ciara")
        plocha.create_line(x, y, e.x, e.y, fill = farba, tag = "ciara", width=1)

    elif prepinac == "stetec":
        plocha.create_oval(e.x-10, e.y-10, e.x+10, e.y+10, fill = farba, outline = farba)

# GEOMETRICKÉ TVARY RENDERUJEME AŽ PO UVOLNENÍ TLAČIDLA MYŠI, ČO SI VYŽADUJE SAMOSTATNÚ FUNKCIU
def umiestnit(e):
    global x,y
    global farba

    if prepinac == "stvorec":
        plocha.create_rectangle(x, y, e.x, e.y, fill = farba, outline = farba)

    elif prepinac == "kruh":
        plocha.create_oval(x, y, e.x, e.y, fill = farba, outline = farba)

    elif prepinac == "ciara":
        plocha.create_line(x, y, e.x, e.y, fill = farba, width=1)

# AKCIE MYŠI PREPOJÍME S JEDNOTLIVÝMI FUNKCIAMI
plocha.bind("<Button-1>",klik)
plocha.bind("<B1-Motion>",hyb)
plocha.bind("<ButtonRelease-1>", umiestnit)


window.mainloop()
