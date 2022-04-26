from tkinter import *
import tkinter
from tkinter import font
from typing import Counter
from PIL import ImageTk, Image
import os
import PIL.Image as Image
import io
import base64
import pyodbc
import threading as th
import multiprocessing
import time
from playsound import playsound
from pygame import mixer


class mainWindow:
	window = Tk()
	


class Audioplayer:
	#Class
	print('Hello')

class Relative:
	def __init__(self, PersonID, LastName, FirstName, DateOfBirth, Relation, PersonImage, SOUND):
		self.PersonID = PersonID
		self.LastName = LastName
		self.FirstName = FirstName
		self.DateOfBirth = DateOfBirth
		self.Relation= Relation
		self.PersonImage = PersonImage
		self.SOUND = SOUND
		

	
class AzureApi:

	cwd = os.getcwd()
	
	def DownloadOnStartUp(self):
		server = 'st4prj4.database.windows.net'
		database = 'st4prj4'
		username = 'azureuser'
		password = '{Katrinebjerg123}'   
		driver= '{ODBC Driver 17 for SQL Server}'
		BrugerList=[]
		with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
			with conn.cursor() as cursor:
				query="""SELECT *, CAST(Image AS VARCHAR(MAX)) FROM dbo.Test_table"""
				m=cursor.execute(query)
				allRows = cursor.fetchall()
				for row in allRows:
					PersonID=row[0]
					LastName=str(row[1])
					FirstName=str(row[2])
					DateOfBirth=str(row[3])
					Relation=str(row[4])
					PersonImage=row[5]
					SOUND=row[6]
					if PersonImage !=None:
						if(os.path.exists('ImageFolder/Bruger'+str(PersonID)+'.png')):
							os.remove('ImageFolder/Bruger'+str(PersonID)+'.png')
						imageString = PersonImage
						imagePre= io.BytesIO(imageString)	
						img= Image.open(imagePre)
						imageNameString=str(PersonID)
						img.save('ImageFolder/Bruger'+imageNameString+'.png')
					if SOUND !=None:
						if(os.path.exists('AudioFolder/Bruger'+str(PersonID)+'.mp3')):
							os.remove('AudioFolder/Bruger'+str(PersonID)+'.mp3')
						audioString = SOUND
						audioPre= io.BytesIO(audioString)	
						with open ('AudioFolder/Bruger'+str(PersonID)+'.mp3','wb') as f:
							f.write(audioPre.getbuffer())
					#else:
					#Only use else statement for the update
						#ErrorWindow.openErrorWindow('AudioError')
					BrugerList.append(Relative(PersonID,LastName,FirstName,DateOfBirth,Relation,PersonImage,SOUND))
		return BrugerList
	def update_search():
		while(True):
			print("Tjekker db")
			server = 'st4prj4.database.windows.net'
			database = 'st4prj4'
			username = 'azureuser'
			password = '{Katrinebjerg123}'   
			driver= '{ODBC Driver 17 for SQL Server}'
			
			with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
				with conn.cursor() as cursor:
					query="""SELECT *, CAST(Image AS VARCHAR(MAX)) FROM dbo.Test_table"""
					m=cursor.execute(query)
					allRows = cursor.fetchall()
					counter=0
					changedRows=[]
					for row in allRows:
						RelativeObj=Relative(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),row[5],row[6])
						if(RelativeDTO.BrugerList[counter].PersonID==Relative(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),row[5],row[6])):
							RelativeDTO.BrugerList[counter].PersonID=row[0]
							changedRows.append(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),row[5],row[6])
					for row in changedRows:
						RelativeDTO.BrugerList[counter].PersonID=row[0]
						RelativeDTO.BrugerList[counter].LastName=str(row[1])
						RelativeDTO.BrugerList[counter].FirstName=str(row[2])
						RelativeDTO.BrugerList[counter].DateOfBirth=str(row[3])
						RelativeDTO.BrugerList[counter].Relation=str(row[4])
						RelativeDTO.BrugerList[counter].PersonImage=row[5]
						RelativeDTO.BrugerList[counter].SOUND=row[6]
						if RelativeDTO.BrugerList[counter].PersonImage !=None:
							if(os.path.exists('ImageFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.png')):
								os.remove('ImageFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.png')
							imageString = RelativeDTO.BrugerList[counter].PersonImage
							imagePre= io.BytesIO(imageString)	
							img= Image.open(imagePre)
							imageNameString=str(RelativeDTO.BrugerList[counter].PersonID)
							img.save('ImageFolder/Bruger'+imageNameString+'.png')
						if RelativeDTO.BrugerList[counter].SOUND !=None:
							if(os.path.exists('AudioFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.mp3')):
								os.remove('AudioFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.mp3')
							audioString = RelativeDTO.BrugerList[counter].SOUND
							audioString = row[6]
							audioPre= io.BytesIO(audioString)	
							with open ('AudioFolder/Bruger'+str(row[0])+'.mp3','wb') as f:
								f.write(audioPre.getbuffer())
						
						#else:
						#Only use else statement for the update
						#	ErrorWindow.openErrorWindow('Der var en fejl ved opdatering af data.')
						counter+=1
			time.sleep(600)
						
	
						
class Pictures:
	#Can be used to add a picture
	#picture = Image.open(r'C:\Users\anton\OneDrive\Pictures\Bruger2.png')  
	#picture = picture.save("ImageFolder\Bruger2.png") 
	cwd = os.getcwd()
	cwdUser=cwd+"\ImageFolder"
	cwdSound=cwd+"\SoundImageFolder"
	#Indlæser billeder til menuer
	if(os.path.exists(cwdUser+"\Bruger1.png")):
		Bruger1Billede=Image.open(cwdUser+"\Bruger1.png")
		Bruger1resized=Bruger1Billede.resize((150,150),Image.ANTIALIAS)
		newBruger1Billede = ImageTk.PhotoImage(Bruger1resized)
	if(os.path.exists(cwdUser+"\Bruger2.png")):
		Bruger2Billede=Image.open(cwdUser+"\Bruger2.png")
		Bruger2resized=Bruger2Billede.resize((150,150),Image.ANTIALIAS)
		newBruger2Billede = ImageTk.PhotoImage(Bruger2resized)
	if(os.path.exists(cwdUser+"\Bruger3.png")):
		Bruger3Billede=Image.open(cwdUser+"\Bruger3.png")
		Bruger3resized=Bruger3Billede.resize((150,150),Image.ANTIALIAS)
		newBruger3Billede = ImageTk.PhotoImage(Bruger3resized)
	if(os.path.exists(cwdUser+"\Bruger4.png")):
		Bruger4Billede=Image.open(cwdUser+"\Bruger4.png")
		Bruger4resized=Bruger4Billede.resize((150,150),Image.ANTIALIAS)
		newBruger4Billede = ImageTk.PhotoImage(Bruger4resized)
	if(os.path.exists(cwdUser+"\Bruger5.png")):
		Bruger5Billede=Image.open(cwdUser+"\Bruger5.png")
		Bruger5resized=Bruger5Billede.resize((150,150),Image.ANTIALIAS)
		newBruger5Billede = ImageTk.PhotoImage(Bruger5resized)
	if(os.path.exists(cwdUser+"\Bruger6.png")):
		Bruger6Billede=Image.open(cwdUser+"\Bruger6.png")
		Bruger6resized=Bruger6Billede.resize((150,150),Image.ANTIALIAS)
		newBruger6Billede = ImageTk.PhotoImage(Bruger6resized)
	if(os.path.exists(cwdUser+"\Bruger7.png")):
		Bruger7Billede=Image.open(cwdUser+'\Bruger7.png')
		Bruger7resized=Bruger7Billede.resize((150,150),Image.ANTIALIAS)
		newBruger7Billede = ImageTk.PhotoImage(Bruger7resized)
	if(os.path.exists(cwdUser+'\Bruger8.png')):
		Bruger8Billede=Image.open(cwdUser+'\Bruger8.png')
		Bruger8resized=Bruger8Billede.resize((150,150),Image.ANTIALIAS)
		newBruger8Billede = ImageTk.PhotoImage(Bruger8resized)

	#Indlæser billeder til lyd
	MuteBillede = Image.open(cwdSound+"\Mute.JPG")
	MuteBilledeResize=MuteBillede.resize((60,60),Image.ANTIALIAS)
	newMuteBilledeResize = ImageTk.PhotoImage(MuteBilledeResize)

	Lyd1Billede = Image.open(cwdSound+"\Lyd1.JPG")
	NewLyd1BilledeResize=Lyd1Billede.resize((60,60),Image.ANTIALIAS)
	newLyd1BilledeResize = ImageTk.PhotoImage(NewLyd1BilledeResize)

	Lyd2Billede = Image.open(cwdSound+"\Lyd2.JPG")
	NewLyd2BilledeResize=Lyd2Billede.resize((60,60),Image.ANTIALIAS)
	newLyd2BilledeResize = ImageTk.PhotoImage(NewLyd2BilledeResize)

	Lyd3Billede = Image.open(cwdSound+"\Lyd3.JPG")
	NewLyd3BilledeResize=Lyd3Billede.resize((60,60),Image.ANTIALIAS)
	newLyd3BilledeResize = ImageTk.PhotoImage(NewLyd3BilledeResize)

	PlaybuttonBillede = Image.open(cwdSound+"\Pauseplay.png")
	NewPlaybuttonBillede=PlaybuttonBillede.resize((180,180),Image.ANTIALIAS)
	NewPlaybuttonBillede = ImageTk.PhotoImage(NewPlaybuttonBillede)
				


class ErrorWindow:
	def openErrorWindow(ErrorType):
		errorWindow=Toplevel(mainWindow.window)
		errorWindow.title("Error Window")
		errorWindow.geometry("800x480")
		errorWindow.attributes('-topmost', True)
		#On RPI set the below condition
		#errorrWindow.attributes('-fullscreen',True)
		Label(errorWindow,text="Error Window")
		if(ErrorType=='AudioError'):
			errorLabel=Label(errorWindow,text='There was error getting the audio',font=("Cambria",20))
			errorLabel.place(x=350,y=50)
			CloseWindow = Button(errorWindow, height ='2', width='20',bg='white', text='Godkend', command=errorWindow.destroy)
			CloseWindow.pack()
			CloseWindow.place(x=350,y=250)

class OpenNewWindow:
	isPlaying=False
	def openNewWindow(showImage, _id):
		cwd = os.getcwd()
		ID=_id-1
		relativeObj=RelativeDTO.BrugerList[ID]
		newWindow=Toplevel(mainWindow.window)
		newWindow.title("new window")
		newWindow.geometry("800x480")
		newWindow.attributes('-topmost', True)
		#On RPI set the below condition
		#newWindow.attributes('-fullscreen',True)
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
		NameLabel = Label(newWindow,text="Jeg er "+relativeObj.FirstName+" " +relativeObj.LastName, font=("Cambria",15), wraplength=280)
		NameLabel.place(x=500, y=10)
		BirthdayLabel = Label(newWindow,text="Jeg blev født " + relativeObj.DateOfBirth, font=("Cambria",15))
		BirthdayLabel.place(x=500, y=75)
		RelationLabel= Label(newWindow, text="Jeg er din " + relativeObj.Relation, font=("Cambria",15))
		RelationLabel.place(x=500,y=140)
		PlayLabel= Label(newWindow, text="Tryk her for at høre mere om mig", font=("Cambria",15))
		PlayLabel.place(x=500,y=205)

		PlaySound = Button(newWindow, height ='125', width='125', bg = 'white', fg='white', image=Pictures.NewPlaybuttonBillede, command=lambda: OpenNewWindow.StopOrPlay(_id,OpenNewWindow.isPlaying,cwd))
		PlaySound.pack()
		PlaySound.place(x=600,y=250)
		CloseWindow = Button(newWindow, height ='3', width='30',bg='white', text='Luk vinduet', command=newWindow.destroy)
		CloseWindow.pack()
		CloseWindow.place(x=560,y=400)
		Mute = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newMuteBilledeResize)
		Mute.pack()
		Mute.place(x=70,y=410)
		Lyd1 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd1BilledeResize)
		Lyd1.pack()
		Lyd1.place(x=170,y=410)

		Lyd2 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd2BilledeResize)
		Lyd2.pack()
		Lyd2.place(x=270,y=410)

		Lyd3 = Button(newWindow, height ='60', width='60', bg = 'blue', fg='white', image=Pictures.newLyd3BilledeResize)
		Lyd3.pack()
		Lyd3.place(x=370,y=410)
		#this can be used to remove a picture
		#cwd = os.getcwd()
		#cwd+="\ImageFolder\Bruger2.png"
		#os.remove(cwd)
	def StopOrPlay(_id,isPlaying,cwd):
		mixer.init()
		if mixer.music.get_busy() == False:
			OpenNewWindow.isPlaying=False
		else:
			OpenNewWindow.isPlaying=True
		if(OpenNewWindow.isPlaying==False):
			if(os.path.exists(cwd+'\AudioFolder\Bruger'+str(_id)+'.mp3')):
				mixer.music.load(cwd+'\AudioFolder\Bruger'+str(_id)+'.mp3') #Loading Music File
				mixer.music.play() #Playing Music with Pygame
				OpenNewWindow.isPlaying=True
		elif(OpenNewWindow.isPlaying==True):
			mixer.music.stop()
			mixer.music.unload()
			OpenNewWindow.isPlaying=False

		

class RelativeDTO:
	def __init__(self,BrugerList):
		self.BrugerList=BrugerList
	apiService= AzureApi()
	BrugerList=apiService.DownloadOnStartUp()
	x = th.Timer(30,AzureApi.update_search)
	x.start()
	
	

class TestGUI:
	mainWindow.window.title("Erindringsdevice")
	mainWindow.window.geometry('800x480')
	#On RPI set the below condition
	#mainWindow.window.attributes('-fullscreen',True)
	relativeObj=RelativeDTO.BrugerList
	isPlaying=False
	if(relativeObj[0].PersonImage!=None):
		global Bruger1
		Bruger1 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger1Billede, command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger1Billede,1))
		Bruger1.pack()
		Bruger1.place(x=40,y=10)
		global Name1Label
		Name1Label = Label(mainWindow.window,text=relativeObj[0].FirstName+" " +relativeObj[0].LastName, font=("Cambria",10), wraplength=280)
		Name1Label.place(x=40, y=170)
	if(relativeObj[1].PersonImage!=None):
		global Bruger2
		Bruger2 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger2Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger2Billede,2))
		Bruger2.pack()
		Bruger2.place(x=230,y=10)
		global Name2Label
		Name2Label = Label(mainWindow.window,text=relativeObj[1].FirstName+" " +relativeObj[1].LastName, font=("Cambria",10), wraplength=280)
		Name2Label.place(x=230, y=170)
	if(relativeObj[2].PersonImage!=None):
		global Bruger3
		Bruger3 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger3Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger3Billede,3))
		Bruger3.pack()
		Bruger3.place(x=420,y=10)
		global Name3Label
		Name3Label = Label(mainWindow.window,text=relativeObj[2].FirstName+" " +relativeObj[2].LastName, font=("Cambria",10), wraplength=280)
		Name3Label.place(x=420, y=170)
	if(relativeObj[3].PersonImage!=None):
		global Bruger4
		Bruger4 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger4Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger4Billede,4))
		Bruger4.pack()
		Bruger4.place(x=610,y=10)
		global Name4Label
		Name4Label = Label(mainWindow.window,text=relativeObj[3].FirstName+" " +relativeObj[3].LastName, font=("Cambria",10), wraplength=280)
		Name4Label.place(x=610, y=170)
	if(relativeObj[4].PersonImage!=None):
		global Bruger5
		Bruger5 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger5Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger5Billede,5))
		Bruger5.pack()
		Bruger5.place(x=40,y=200)
		global Name5Label
		Name5Label = Label(mainWindow.window,text=relativeObj[4].FirstName+" " +relativeObj[4].LastName, font=("Cambria",10), wraplength=280)
		Name5Label.place(x=40, y=360)
	if(relativeObj[5].PersonImage!=None):
		global Bruger6
		Bruger6 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger6Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger6Billede,6))
		Bruger6.pack()
		Bruger6.place(x=230,y=200)
		global Name6Label
		Name6Label = Label(mainWindow.window,text=relativeObj[5].FirstName+" " +relativeObj[5].LastName, font=("Cambria",10), wraplength=280)
		Name6Label.place(x=230, y=360)
	if(relativeObj[6].PersonImage!=None):
		global Bruger7
		Bruger7 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger7Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger7Billede,7))
		Bruger7.pack()
		Bruger7.place(x=420,y=200)
		global Name7Label
		Name7Label = Label(mainWindow.window,text=relativeObj[6].FirstName+" " +relativeObj[6].LastName, font=("Cambria",10), wraplength=280)
		Name7Label.place(x=420, y=360)	
	if(relativeObj[7].PersonImage!=None):
		global Bruger8
		Bruger8 = Button(mainWindow.window, height ='150', width='150', bg = 'blue', fg='white', image=Pictures.newBruger8Billede,command=lambda: OpenNewWindow.openNewWindow(Pictures.newBruger8Billede,8))
		Bruger8.pack()
		Bruger8.place(x=610,y=200)
		global Name8Label
		Name8Label = Label(mainWindow.window,text=relativeObj[7].FirstName+" " +relativeObj[7].LastName, font=("Cambria",10), wraplength=280)
		Name8Label.place(x=610, y=360)

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

	CloseWindow = Button(mainWindow.window, height ='2', width='20',bg='white', text='Luk vinduet', command=mainWindow.window.destroy)
	CloseWindow.pack()
	CloseWindow.place(x=530,y=420)
	
	mainWindow.window.mainloop()
