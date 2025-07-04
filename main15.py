import math
from tkinter import *

#Input Value
def input(value):
    current = scvalue.get()
    if value == "π":
         value = str(math.pi)
    elif value == "e":
         value = str(math.e)
    elif value == "^":
         value = "**"
    elif value == "√":
         value = "sqrt("
    elif value == "sin":
         value = "sin("
    elif value == "cos":
         value = "cos("
    elif value == "tan":
         value = "tan("
    elif value == "log":
         value="log10("
    scvalue.set(current + value)
    screen.update()

#Handling Input Event
def handle(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = scvalue.get()
            safe_dict = math.__dict__.copy()
            safe_dict["radians"] =math.radians
            safe_dict["log10"] = math.log10
            safe_dict["sqrt"] = math.sqrt
            result = eval(expression, {"__builtins__": None}, safe_dict)
        except Exception as e:
            print(e)
            result = "error"
        scvalue.set(result)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text== "⌫":
        current = scvalue.get()
        if current:
            scvalue.set(current[:-1])
        screen.update()


root = Tk()
root.geometry("420x800")
root.minsize(420,800)
root.maxsize(600,800)
root.title("Calculator By Sanskar")
root.config(bg="white")

#Entry Widget
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 80", bg="#1e1e1e", fg="white", insertbackground="white")
screen.pack(fill="x")

#Creating Circular Button
def create_circle_button(parent, text, bg="orange"):
    canvas = Canvas(parent, width=95, height=90, bg="white", highlightthickness=0)
    canvas.pack(side="left", padx=5, pady=5,fill="x")
    circle = canvas.create_oval(8, 8, 80, 80, fill=bg, outline=bg)
    label = canvas.create_text(45, 45, text=text, font="lucida 20 bold", fill="black")
    canvas.tag_bind(circle, "<Button-1>", lambda e, t=text: input(t))
    canvas.tag_bind(label, "<Button-1>", lambda e, t=text: input(t))

rows = [
    ["sin", "cos", "tan", "log"],
    ["√", "e", "^", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "π", ")"],
]


for row in rows:
    f = Frame(root, bg="white")
    f.pack()
    for item in row:
        display = item
        if item == "√":
            display = "sqrt("
        create_circle_button(f, display)


f=Frame(root,padx=5,pady=10, bg="white")
f.pack()

#Buttons
b = Button(f, text="C", padx=20, pady=20, font="lucida 20 bold")
b.pack(side="right",padx=8)
b.bind("<Button-1>", handle)

b = Button(f, text="⌫", padx=20, pady=20, font="lucida 20 bold")
b.pack(side="right",padx=8)
b.bind("<Button-1>", handle)

b = Button(f, text="=", padx=20, pady=20, font="lucida 20 bold")
b.pack(side="right", padx=8)
b.bind("<Button-1>", handle)

root.mainloop()