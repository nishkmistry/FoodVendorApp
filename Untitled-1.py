from tkinter import *
root = Tk()

#variable is stored in the root object
root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)

def clicked1():
    root.counter += 1
    L1['text'] = 'Button clicked: ' + str(root.counter)
        
b = Button(root, text="Click Me", command=clicked)
b.pack()

L = Label(root, text="No clicks yet.")
L.pack()

b1 = Button(root, text="Click Me", command=clicked1)
b1.pack()

L1 = Label(root, text="No clicks yet.")
L1.pack()

root.mainloop()