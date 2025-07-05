from tkinter import *

root = Tk()
root.title("SANSKAR TRAVELS")
root.geometry("535x380")
root.configure(bg="snow")


def getvals():
    print("From Submitted!")
    print(f"Name: {namevalue.get()}")
    print(f"Phone: {phonevalue.get()}")
    print(f"Gender: {gendervalue.get()}")
    print(f"Emergency Contact: {emergencyvalue.get()}")
    print(f"Payment Mode: {paymentmodevalue.get()}")
    print(f"Prebook Meal: {'Yes' if foodservicevalue.get() else 'No'}")


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

#Heading
label = Label(root,text="✈ WELCOME ✈",font="Georgia 29 bold",pady=10,bg="snow",fg="black").grid(row=0,column=0,columnspan=3,sticky="n",pady=20)

#Text for our form
NAME =Label(root,text="NAME",font="Consolas 15 bold",pady=2,anchor="e",bg="snow",fg="black")
PHONE =Label(root,text="PHONE",font="Helvetica 15 bold",pady=2,bg="snow",fg="black")
GENDER =Label(root,text="GENDER",font="Helvetica 15 bold",pady=2,bg="snow",fg="black")
EMERGENCY =Label(root,text="EMERGENCY CONTACT",font="helvetica 15 bold",pady=2,bg="snow",fg="black")
PAYMENTMODE =Label(root,text="PAYMENT MODE",font="Helvetica 15 bold",pady=2,bg="snow",fg="black")

#Pack text for form
NAME.grid(row=1,column=0, sticky="n")
PHONE.grid(row=2,column=0, sticky="n")
GENDER.grid(row=3,column=0, sticky="n")
EMERGENCY.grid(row=4,column=0, sticky="n")
PAYMENTMODE.grid(row=5,column=0, sticky="n")

#Tkinter variable for storing entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

#Entries for form
entry_width=10
nameentry=Entry(root,textvariable=namevalue,bg="gray61",width=30,highlightthickness=0)
phoneentry=Entry(root,textvariable=phonevalue,bg="gray61",width=30,highlightthickness=0)
genderentry=Entry(root,textvariable=gendervalue,bg="gray61",width=30,highlightthickness=0)
emergencyentry=Entry(root,textvariable=emergencyvalue,bg="gray61",width=30,highlightthickness=0)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue,bg="gray61",width=30,highlightthickness=0)

#Packing for entries
nameentry.grid(row=1,column=1,pady=3,sticky="w")
phoneentry.grid(row=2,column=1,pady=3,sticky="w")
genderentry.grid(row=3,column=1,pady=3,sticky="w")
emergencyentry.grid(row=4,column=1,pady=3,sticky="w")
paymentmodeentry.grid(row=5,column=1,pady=3,sticky="w")

#Checkbox & packing
Checkbutton(text="Prebook your meal? 🍽",font="helvetic 12 bold",variable=foodservicevalue,bg="snow",fg="black").grid(row=6,column=1,sticky="w")

Button( text="Submit Now", font=("Helvetica", 13, "bold"),
                    command=getvals, padx=15, pady=6,
                    bg="snow", fg="black", activebackground="snow",
                    relief="flat", bd=0, cursor="hand2").grid(row=7, column=1, pady=15, sticky="w")

root.mainloop()