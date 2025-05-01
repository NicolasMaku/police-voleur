from tkinter import *

window = Tk()
window.title("Police")
window.geometry("500x500")
canvas = Canvas(window, width=500, height=250,bg="white")
canvas.pack(padx=5, pady=5)
# from left,from top deb,from left
canvas.create_line(110, 10, 110, 200)
canvas.create_line(10, 110, 210, 110, fill="green")
canvas.create_oval(10, 10, 210, 200)

window.mainloop()