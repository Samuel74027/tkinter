from tkinter import *

app = Tk()
app.title('GUI Example 2')
app.geometry("200x500") 
app.configure(background='white')


toggle = False
text = StringVar()
text.set('Original text')
toggleLabel = Label(textvariable = text)
toggleLabel.config(bg = 'blue')
toggleLabel.pack(side = 'bottom')

def toggle():
    global toggle
    if toggle == True:
        text.set('Changed text')
        toggleLabel.config(bg = 'red')
        toggle = False
    elif toggle == False:
        text.set('Original text')
        toggleLabel.config(bg = 'green')
        toggle = True
        

button1 = Button(text='Click Here', command = toggle)
button1.pack(side = 'top')



app.mainloop()