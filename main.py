import pyperclip
import pyshorteners
from tkinter import *

myApp = Tk()
myApp.geometry("400x200")
myApp.title("URL Shortener | AYMEN DEV")
#myApp.resizable(False,False)
url = StringVar()
url_address = StringVar()

def urlshort():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get
    pyperclip.copy(url_short)

Label(myApp,text="My URL Shortener",font="poppins 25 bold").pack(pady=10)
Entry(myApp,textvariable=url).pack(pady=5)
Button(myApp,text="Generate Short URL", command=urlshort,fg="red").pack(pady=7)
Label(myApp,text="Your URL After Short ",font="poppins 25 bold").pack(pady=10)
Entry(myApp,textvariable=url_address).pack(pady=5)
Button(myApp,text="Copy Your URL", command=copyurl,fg="red").pack(pady=7)
myApp.mainloop()