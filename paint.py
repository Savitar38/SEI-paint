import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()

x = 0
y = 0

prepinac = ""
farba = "#000"

ikony = ["sprej.png", "stvorec.png", "kruh.png", "farba.png", "ciara.png", "stetec.png", "vymazat.png", "ulozit.png"]
tlacidla = ["sprej", "stvorec", "kruh", "farba", "ciara", "stetec", "vymazat", "ulozit"]

plocha = tk.Canvas(width=440, height=400, bg="white")
plocha.grid(row=1, column=0, columnspan=8)

def prepnut(volba):

    ## Voľba prepínača aby sme mohli vybrať správnu funkcionalitu ##
    print(volba)
    global prepinac
    if prepinac == volba:
        prepinac = ""
        return
    else:
        prepinac = volba

    ## Funkcionality, ktoré nekreslia, sa udejú tu ##

    if prepinac == "farba":
        global farba
        rgb, farba = colorchooser.askcolor(title ="Vyber farbu") # Output je v hexadecimálnej sústave
        prepinac = ""

    elif prepinac == "vymazat":
        plocha.delete("all")
        prepinac = ""

    elif prepinac == "ulozit":
        prepinac = ""



## VYTVÁRANIE TLAČIDIEL ##
ikony_subory = []
for i in range(8):
    img = tk.PhotoImage(file=f"./icons/{ikony[i]}")
    ikony_subory.append(img)

# kód pre testovanie s jednou ikonou
# 
# for i in range(8):
#     img = tk.PhotoImage(file=f"./icons/logo.png")
#     ikony_subory.append(img)


for i in range(8):
    b = tk.Button(image=ikony_subory[i], width=50, command= lambda i=i: prepnut(tlacidla[i]))
    b.grid(row=0, column=i)


def klik(e):

    ## Do globálnych premenných x a y sa uložia súradnice miesta kliku ##

    global x,y
    x=e.x 
    y=e.y


def hyb(e):
    global x,y
    global farba

    ## Do každej funkcie, ktorá niečo kreslí, máte 3 vstupy: originálne súradnice kliku, súradnice aktuálnej pozície stlačenej myše a farbu ##

    if prepinac == "sprej":
                for i in range(100):
            sx = rand.randint(-13, 13)
            sy = rand.randint(-13, 13)
            plocha.create_line(e.x+sx, e.y+sy, e.x+sx+1, e.y+sy, fill=farba)
        pass

    elif prepinac == "stvorec":
        plocha.delete("stvorec")
        plocha.create_rectangle(x, y, e.x, e.y, fill = farba, outline = farba, tag = "stvorec")

    elif prepinac == "kruh":
        pass

    elif prepinac == "ciara":
        pass

    elif prepinac == "stetec":
        plocha.create_oval(e.x-10, e.y-10, e.x+10, e.y+10, fill = farba, outline = farba)

def umiestnit(e):
    global x,y
    global farba

    ## Do každej funkcie, ktorá niečo kreslí, máte 3 vstupy: originálne súradnice kliku, súradnice aktuálnej pozície stlačenej myše a farbu ##

    if prepinac == "stvorec":
        plocha.create_rectangle(x, y, e.x, e.y, fill = farba)

    elif prepinac == "kruh":
        # kruh(x, y, e.x, e.y, farba)
        pass

    elif prepinac == "ciara":
        # ciara(x, y, e.x, e.y, farba)
        pass

plocha.bind("<Button-1>",klik)
plocha.bind("<B1-Motion>",hyb)
plocha.bind("<ButtonRelease-1>", umiestnit)


window.mainloop()
