from tkinter import *
window=Tk()
window.title("gui-new application")
window.geometry("500x500+500+500")
window.configure(bg="black")

frame=Frame(window,bg="white",borderwidth=1)
frame.pack()
s1 = Scale(from_=0, to=200, orient="horizontal", length=500, tickinterval=10)
s1.pack(padx=200,pady=200)
mainloop()
