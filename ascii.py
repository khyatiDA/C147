from tkinter import *
window = Tk()

window.title("ENSCRIPTION WITH ASCII CODE")
window.geometry("600x600")

word = Entry(window)
word.place(relx = 0.5 , rely =0.4  , anchor = CENTER)

label1 = Label(window , text = "Nmae in Ascii")
label1.place(relx = 0.5 , rely = 0.6  , anchor = CENTER )

label2 = Label(window , text = "Encrypted Name")
label2.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

def asciiConvert():
    input = str(word.get())

    for letter in input:
        label1["text"]+=str(ord(letter))+""
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"]+=str(chr(encrypted))+""

btn = Button(window , text = "Display the Ascii code and encrypted value" , command = asciiConvert)  
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)  


window.mainloop()


