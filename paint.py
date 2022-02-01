import tkinter as tk

window = tk.Tk()

img = tk.PhotoImage(file="./logo.png")

plocha = tk.Canvas(width=440, height=400, bg="red")
plocha.grid(row=1, column=0, columnspan=8)

def disp(num):
    plocha.delete("all")
    # plocha.create_text(50, 10, text=e1.get())
    plocha.create_text(50, 10, text=f"Jou Jou {num}")

for i in range(8):
    b = tk.Button(image=img, command=disp(i), width=50)
    b.grid(row=0, column=i)

# e1 = tk.Entry()
# e1.pack()

window.mainloop()