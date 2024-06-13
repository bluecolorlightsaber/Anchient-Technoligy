import tkinter

def do_nothing():
    moregarbage = tkinter.Toplevel()
    toplevelgarbagelabel = tkinter.Label(moregarbage, text="serously, this is garbage, it does nothing. download the real thing")
    toplevelgarbagelabel2 = tkinter.Label(moregarbage, text="Succesfully deleted comments")
    toplevelgarbagelabel2.pack()
    toplevelgarbagelabel.pack()
    moregarbage.mainloop()
garbage = tkinter.Tk()

label = tkinter.Label(garbage, text="this is garbage, enter the ID of the user you want to delete comments")
entry = tkinter.Entry(garbage)
button = tkinter.Button(garbage, text="ok", command=do_nothing)

label.pack()

entry.pack()
button.pack()

garbage.mainloop()

