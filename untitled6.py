from tkinter import *
import random
root=Tk()
root.title('gift')
root.geometry('400x400')

label1=Label(root,text='Gift items: bottle, pen, pencil, crayons, backpack, book')
label2=Label(root)

def giftpicker():
    n=random.sample(range(1,6),1)
    label2['text'] = "Your gift is gift number " + str(n) +"!"

button=Button(root,text='Generate gift',command=giftpicker)
button.place(relx=0.5,rely=0.5,anchor=CENTER)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)
label2.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()
    