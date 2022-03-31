from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os


class mainWindow:
	window = Tk()


class Pictures:

	cwd = os.getcwd()
	cwd+="\ImageFolder"
	#Indlæser billeder til menuer
	Bruger1Billede=Image.open(cwd+"\Bruger1.png")
	Bruger1resized=Bruger1Billede.resize((100,100),Image.ANTIALIAS)
	newBruger1Billede = ImageTk.PhotoImage(Bruger1resized)

	#Indlæser billeder til lyd
	MuteBillede = Image.open(cwd+"\Mute.jpg")
	MuteBilledeResize=MuteBillede.resize((40,40),Image.ANTIALIAS)
	newMuteBilledeResize = ImageTk.PhotoImage(MuteBilledeResize)

	Lyd1Billede = Image.open(cwd+"\Lyd1.jpg")
	NewLyd1BilledeResize=Lyd1Billede.resize((40,40),Image.ANTIALIAS)
	newLyd1BilledeResize = ImageTk.PhotoImage(NewLyd1BilledeResize)

	Lyd2Billede = Image.open(cwd+"\Lyd2.jpg")
	NewLyd2BilledeResize=Lyd2Billede.resize((40,40),Image.ANTIALIAS)
	newLyd2BilledeResize = ImageTk.PhotoImage(NewLyd2BilledeResize)

	Lyd3Billede = Image.open(cwd+"\Lyd3.jpg")
	NewLyd3BilledeResize=Lyd3Billede.resize((40,40),Image.ANTIALIAS)
	newLyd3BilledeResize = ImageTk.PhotoImage(NewLyd3BilledeResize)


class OpenNewWindow:

	def openNewWindow():
		
		newWindow=Toplevel(mainWindow.window)
		newWindow.title("new window")
		newWindow.geometry("200x200")
		Label(newWindow,text="New window")


class TetsGUI:

	mainWindow.window.title("Erindringsdevice")
	mainWindow.window.geometry('700x500')
	

	Bruger1 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede, command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger1.pack()
	Bruger1.place(x=100,y=50)

	Bruger2 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger2.pack()
	Bruger2.place(x=250,y=50)
	
	Bruger3 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger3.pack()
	Bruger3.place(x=400,y=50)

	Bruger4 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger4.pack()
	Bruger4.place(x=550,y=50)

	Bruger5 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger5.pack()
	Bruger5.place(x=100,y=200)

	Bruger6 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger6.pack()
	Bruger6.place(x=250,y=200)
	
	Bruger7 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger7.pack()
	Bruger7.place(x=400,y=200)

	Bruger8 = Button(mainWindow.window, height ='100', width='100', bg = 'blue', fg='white', image=newBruger1Billede,command=lambda: OpenNewWindow.openNewWindow(newBruger1Billede))
	Bruger8.pack()
	Bruger8.place(x=550,y=200)

	
	#Knapper til menu  -  lyd
	Mute = Button(mainWindow.window, height ='40', width='40', bg = 'blue', fg='white', image=Pictures.newMuteBilledeResize)
	Mute.pack()
	Mute.place(x=100,y=350)

	Lyd1 = Button(mainWindow.window, height ='40', width='40', bg = 'blue', fg='white', image=Pictures.newLyd1BilledeResize)
	Lyd1.pack()
	Lyd1.place(x=150,y=350)

	Lyd2 = Button(mainWindow.window, height ='40', width='40', bg = 'blue', fg='white', image=Pictures.newLyd2BilledeResize)
	Lyd2.pack()
	Lyd2.place(x=200,y=350)

	Lyd3 = Button(mainWindow.window, height ='40', width='40', bg = 'blue', fg='white', image=Pictures.newLyd3BilledeResize)
	Lyd3.pack()
	Lyd3.place(x=250,y=350)

	mainWindow.window.mainloop()




