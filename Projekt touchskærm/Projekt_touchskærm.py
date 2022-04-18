from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os
import PIL.Image as Image
import io
import base64
import pyodbc


class mainWindow:
	window = Tk()

class Audioplayer:
	#Class
	print('Hello')

class Pictures:
	#Can be used to add a picture
	#picture = Image.open(r'C:\Users\anton\OneDrive\Pictures\Bruger2.png')  
	#picture = picture.save("ImageFolder\Bruger2.png") 
	cwd = os.getcwd()
	cwd+="\ImageFolder"
	#Indlæser billeder til menuer
	Bruger1Billede=Image.open(cwd+"\Bruger1.png")
	Bruger1resized=Bruger1Billede.resize((150,150),Image.ANTIALIAS)
	newBruger1Billede = ImageTk.PhotoImage(Bruger1resized)

	Bruger2Billede=Image.open(cwd+"\Bruger2.png")
	Bruger2resized=Bruger2Billede.resize((150,150),Image.ANTIALIAS)
	newBruger2Billede = ImageTk.PhotoImage(Bruger2resized)

	Bruger3Billede=Image.open(cwd+"\Bruger3.png")
	Bruger3resized=Bruger3Billede.resize((150,150),Image.ANTIALIAS)
	newBruger3Billede = ImageTk.PhotoImage(Bruger3resized)

	Bruger4Billede=Image.open(cwd+"\Bruger4.png")
	Bruger4resized=Bruger4Billede.resize((150,150),Image.ANTIALIAS)
	newBruger4Billede = ImageTk.PhotoImage(Bruger4resized)

	Bruger5Billede=Image.open(cwd+"\Bruger5.png")
	Bruger5resized=Bruger5Billede.resize((150,150),Image.ANTIALIAS)
	newBruger5Billede = ImageTk.PhotoImage(Bruger5resized)

	Bruger6Billede=Image.open(cwd+"\Bruger6.png")
	Bruger6resized=Bruger6Billede.resize((150,150),Image.ANTIALIAS)
	newBruger6Billede = ImageTk.PhotoImage(Bruger6resized)

	Bruger7Billede=Image.open(cwd+"\Bruger7.png")
	Bruger7resized=Bruger7Billede.resize((150,150),Image.ANTIALIAS)
	newBruger7Billede = ImageTk.PhotoImage(Bruger7resized)

	Bruger8Billede=Image.open(cwd+"\Bruger8.png")
	Bruger8resized=Bruger8Billede.resize((150,150),Image.ANTIALIAS)
	newBruger8Billede = ImageTk.PhotoImage(Bruger8resized)

	#Indlæser billeder til lyd
	MuteBillede = Image.open(cwd+"\Mute.JPG")
	MuteBilledeResize=MuteBillede.resize((60,60),Image.ANTIALIAS)
	newMuteBilledeResize = ImageTk.PhotoImage(MuteBilledeResize)

	Lyd1Billede = Image.open(cwd+"\Lyd1.JPG")
	NewLyd1BilledeResize=Lyd1Billede.resize((60,60),Image.ANTIALIAS)
	newLyd1BilledeResize = ImageTk.PhotoImage(NewLyd1BilledeResize)

	Lyd2Billede = Image.open(cwd+"\Lyd2.JPG")
	NewLyd2BilledeResize=Lyd2Billede.resize((60,60),Image.ANTIALIAS)
	newLyd2BilledeResize = ImageTk.PhotoImage(NewLyd2BilledeResize)

	Lyd3Billede = Image.open(cwd+"\Lyd3.JPG")
	NewLyd3BilledeResize=Lyd3Billede.resize((60,60),Image.ANTIALIAS)
	newLyd3BilledeResize = ImageTk.PhotoImage(NewLyd3BilledeResize)

	PlaybuttonBillede = Image.open(cwd+"\Pauseplay.png")
	NewPlaybuttonBillede=PlaybuttonBillede.resize((80,80),Image.ANTIALIAS)
	NewPlaybuttonBillede = ImageTk.PhotoImage(NewPlaybuttonBillede)
	
class AzureApi:
	cwd = os.getcwd()
	def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
		with open(filename, 'wb') as file:
			 file.write(data)

	def OpenDataBaseTest(self, id):
		server = 'st4prj4.database.windows.net'
		database = 'st4prj4'
		username = 'azureuser'
		password = '{Katrinebjerg123}'   
		driver= '{ODBC Driver 17 for SQL Server}'
		with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
			with conn.cursor() as cursor:
				query="""SELECT *, CAST(Image AS VARCHAR(MAX)) FROM dbo.Test_table WHERE PersonID = ?"""
				tuple1=(str(id))
				m=cursor.execute(query,tuple1)
				row = cursor.fetchone()
				while row:
					print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
					row = cursor.fetchone()
					if str(row[3])!='None':
					    imageString = str(row[3])
					if str(row[3])!='None':
						integers = []
						for x in m:
						    print(x)
						while imageString:
							value = int(text[:2], 16)
							integers.append(value)
							text = text[2:]
						data = bytearray(integers)    
						with open('output.jpg', 'wb') as fh:
							print(fh.write(data))
						image= Image.open('output.jpg')
						image.show()
						#imagePre= imageString[2:]
						#imagePre= base64.b64encode(imageString)
						#print(imagePre)
						#with open('Bruger2.png','wb') as File:
						#	File.write(imagePre)
	def OpenDataBaseTest(self, id):
		server = 'st4prj4.database.windows.net'
		database = 'st4prj4'
		username = 'azureuser'
		password = '{Katrinebjerg123}'   
		driver= '{ODBC Driver 17 for SQL Server}'
		with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
			with conn.cursor() as cursor:
				query="""SELECT *, CAST(Image AS VARCHAR(MAX)) FROM dbo.Test_table WHERE PersonID = ?"""
				tuple1=(str(id))
				m=cursor.execute(query,tuple1)
				row = cursor.fetchone()
				while row:
					row = cursor.fetchone()
					if str(row[4])!='None':
					    audioString = str(row[4])
					if str(row[4])!='None':
						#Code that makes fetches and converts to correct byte format
						print('Hello')
					else:
						ErrorWindow.openErrorWindow('AudioError')
						
						
class ErrorWindow:
	def openErrorWindow(ErrorType):
		errorWindow=Toplevel(mainWindow.window)
		errorWindow.title("Error Window")
		errorWindow.geometry("400x200")
		Label(errorWindow,text="Error Window")
		if(ErrorType=='AudioError'):
			errorLabel=Label(errorWindow,text='There was error getting the audio')
			errorLabel.place(x=150,y=50)
			CloseWindow = Button(mainWindow.window, height ='2', width='20',bg='white', text='Close Window', command=mainWindow.window.destroy)
			CloseWindow.pack()
			CloseWindow.place(x=150,y=150)

class OpenNewWindow:
	def openNewWindow(showImage):
		newWindow=Toplevel(mainWindow.window)
		newWindow.title("new window")
		newWindow.geometry("800x480")
		Label(newWindow,text="New window") 
		if showImage==Pictures.newBruger1Billede:
			preSizeImage=Pictures.Bruger1Billede
		elif showImage==Pictures.newBruger2Billede:
			preSizeImage=Pictures.Bruger2Billede
		elif showImage==Pictures.newBruger3Billede:
			preSizeImage=Pictures.Bruger3Billede
		elif showImage==Pictures.newBruger4Billede:
			preSizeImage=Pictures.Bruger4Billede
		elif showImage==Pictures.newBruger5Billede:
			preSizeImage=Pictures.Bruger5Billede
		elif showImage==Pictures.newBruger6Billede:
			preSizeImage=Pictures.Bruger6Billede
		elif showImage==Pictures.newBruger7Billede:
			preSizeImage=Pictures.Bruger7Billede
		elif showImage==Pictures.newBruger8Billede:
			preSizeImage=Pictures.Bruger8Billede
		resizedImage = preSizeImage.resize((500,400), Image.ANTIALIAS)
		photoImg=ImageTk.PhotoImage(resizedImage)
		img = Label(newWindow,image=photoImg)
		img.image = photoImg
		img.place(x=0, y=0)
		PlaySound = Button(newWindow, height ='75', width='75', bg = 'white', fg='white', image=Pictures.NewPlaybuttonBillede)
		PlaySound.pack()
		PlaySound.place(x=550,y=50)
		CloseWindow = Button(newWindow, height ='2', width='20',bg='white', text='Close Window', command=newWindow.destroy)
		CloseWindow.pack()
		CloseWindow.place(x=530,y=250)
		Mute = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newMuteBilledeResize)
		Mute.pack()
		Mute.place(x=100,y=400)
		Lyd1 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd1BilledeResize)
		Lyd1.pack()
		Lyd1.place(x=200,y=400)

		Lyd2 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd2BilledeResize)
		Lyd2.pack()
		Lyd2.place(x=300,y=400)

		Lyd3 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd3BilledeResize)
		Lyd3.pack()
		Lyd3.place(x=400,y=400)
		#this can be used to remove a picture
		#cwd = os.getcwd()
		#cwd+="\ImageFolder\Bruger2.png"
		#os.remove(cwd)
		


class TestGUI:
	mainWindow.window.title("Erindringsdevice")
	mainWindow.window.geometry('800x480')
	apiService= AzureApi()
	apiService.OpenDataBaseTest(5)
	Bruger1 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger1Billede, command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger1Billede))
	Bruger1.pack()
	Bruger1.place(x=40,y=30)

	Bruger2 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger2Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger2Billede))
	Bruger2.pack()
	Bruger2.place(x=230,y=30)
	
	Bruger3 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger3Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger3Billede))
	Bruger3.pack()
	Bruger3.place(x=420,y=30)

	Bruger4 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger4Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger4Billede))
	Bruger4.pack()
	Bruger4.place(x=610,y=30)

	Bruger5 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger5Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger5Billede))
	Bruger5.pack()
	Bruger5.place(x=40,y=200)

	Bruger6 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger6Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger6Billede))
	Bruger6.pack()
	Bruger6.place(x=230,y=200)
	
	Bruger7 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger7Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger7Billede))
	Bruger7.pack()
	Bruger7.place(x=420,y=200)

	Bruger8 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger8Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger8Billede))
	Bruger8.pack()
	Bruger8.place(x=610,y=200)

	#Knapper til menu  -  lyd
	Mute = Button(mainWindow.window, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newMuteBilledeResize)
	Mute.pack()
	Mute.place(x=100,y=400)

	Lyd1 = Button(mainWindow.window, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd1BilledeResize)
	Lyd1.pack()
	Lyd1.place(x=200,y=400)

	Lyd2 = Button(mainWindow.window, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd2BilledeResize)
	Lyd2.pack()
	Lyd2.place(x=300,y=400)

	Lyd3 = Button(mainWindow.window, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd3BilledeResize)
	Lyd3.pack()
	Lyd3.place(x=400,y=400)

	CloseWindow = Button(mainWindow.window, height ='2', width='20',bg='white', text='Close Window', command=mainWindow.window.destroy)
	CloseWindow.pack()
	CloseWindow.place(x=530,y=420)

	mainWindow.window.mainloop()
