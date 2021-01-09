import tkinter as t

tk = t.Tk()
w = t.Button()
c = t.Canvas(tk, bg = "#000000", bd = 3)
x = 20
y = 20

img = t.PhotoImage(file = "Logo.png")
c.create_image(x, y, image = img)
coord = 10, 50, 240, 210

def clearboard():
    c.delete("all");


def key(event):
    global y
    global x
    pr = event.char
    if(pr is "w"):
        y -= 5
    if(pr is "s"):
        y += 5
    if(pr is "a"):
        x -= 5
    if(pr is "d"):
        x += 5
    c.delete("all");
    c.create_image(x, y, image = img)



w = t.Button(tk, command = clearboard, activebackground = "#000000", activeforeground = "#FFFFFF", bd = 3, fg = "#000000", bg = "#FFFFFF", text = "Clear", relief="groove")


c.focus_set()
c.bind("<Key>", key)

w.pack()
c.pack()
tk.mainloop()