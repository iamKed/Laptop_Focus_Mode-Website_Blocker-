from tkinter import *

root = Tk()

def submit():
    print(f"Starting Time: {S_time.get()}  Ending Time:  {E_time.get()}")
    if S_Entry and E_Entry:
        with open("Records.txt", "a") as file:
            file.write(f"Starting Time: {S_time.get()}  Ending Time:  {E_time.get()} Website List: { Websites_Input.get()}\n")
            
        print("Your Time is submitted succesfully !")
    # print("(To Submit More Websites Type Websites Again!)")
    next_msg=Label(root,text='✅(To Submit More Websites Type Websites Again and Hit the SUBMIT button again!)')
    next_msg.grid(row=7,column=3)
    this_b = Label(root, text=f'"{Websites_Input.get()}" will be Hibernated till {E_time.get()}:00 ')
    this_b.grid(row=6,column=3)
    this_b.after(5000, this_b.destroy)
    W_Entry.delete(0,END)


root.geometry("644x344")
Label(root, text="Welcome to Focus Mode!", font="comicsansms 19 bold", pady=15).grid(row=0, column=3)
Starting_Time = Label(root, text="Starting Time")
Ending_Time = Label(root, text="Ending Time")
Websites = Label(root, text="Websites to be Blocked:")
Notice = Label(root, text="(Please Enter the time in 24 Hours Only!)\n(Please Provide One website a line!)")
Notice.grid(row=1, column=3)
Starting_Time.grid(row=2, column=2)
Ending_Time.grid(row=3, column=2)
Websites.grid(row=4, column=2)
S_time = StringVar()
E_time = StringVar()
Websites_Input = StringVar()
S_Entry = Entry(root, textvariable=S_time)
E_Entry = Entry(root, textvariable=E_time)
W_Entry = Entry(root, textvariable=Websites_Input)
S_Entry.grid(row=2, column=3)
E_Entry.grid(row=3, column=3)
W_Entry.grid(row=4, column=3)
Button(text="Submit", command=submit).grid(row=8, column=3)
root.mainloop()
