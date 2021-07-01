from tkinter import * 
counter = 0
def add (event=None):
	global counter
	counter  += 1
	messagetoadd = f"{counter} {e1.get()}"
	lis.insert(END,messagetoadd)
	e1.delete(0,END)

def edit(event):
	slot = lis.get(ACTIVE).split()
	e1.insert(END,slot[1])
	lis.delete(ACTIVE)

root = Tk()
width = 500
height = 500
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw / 2)- (width /2)
y = (sh / 2)- (height /2)
root.geometry("%dx%d+%d+%d"%(width,height,x,y))

lbl = Label(root,text = "Add to the list")

frame = Frame(root, width = 500, height =320,)
sc = Scrollbar(frame,orient = "vertical")
sc.pack(side = "right",fill = "y")
e1 = Entry(root)
e1.bind('<Return>',add)
lbl1 = Label(root , text = "To Do List",font = ("Arial",17))
lis = Listbox(frame,width = 78,height = 20,yscrollcommand = sc.set)
sc.config(command = lis.yview)
lis.bind('<Double-1>',edit)

btn = Button(root,text = "add to the list",command = add)


frame.place(x =1 ,y=160)
lbl.place(x = 20 ,y = 50)
lbl1.place(x = 190 ,y = 120)
e1.place(x = 120 , y=50)
lis.pack()
btn.place(x = 290 , y=50)

root.mainloop()