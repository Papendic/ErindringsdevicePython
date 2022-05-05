from tkinter import *
import tkinter
from tkinter import font
#from typing import Counter
from PIL import ImageTk, Image
import os
import mysql.connector
import PIL.Image as Image
import io
import pyodbc
import threading as th
import time
from pygame import mixer

class Root:
	root = Tk()
	
class AudioPlayer:
	mixer.init()
	cwd=os.getcwd()
	def StopOrPlay(_id,isPlaying):
		if mixer.music.get_busy() == False:
			RelativeWindow.isPlaying=False
		else:
			RelativeWindow.isPlaying=True
		if(RelativeWindow.isPlaying==False):
			if(os.path.exists(AudioPlayer.cwd+'\AudioFolder\Bruger'+str(_id)+'.mp3')):
				mixer.music.load(AudioPlayer.cwd+'\AudioFolder\Bruger'+str(_id)+'.mp3') #Loading Music File
				mixer.music.play() #Playing Music with Pygame
				RelativeWindow.isPlaying=True
		elif(RelativeWindow.isPlaying==True):
			mixer.music.stop()
			mixer.music.unload()
			RelativeWindow.isPlaying=False
	def Stop():
		mixer.music.stop()
		mixer.music.unload()
		RelativeWindow.isPlaying=False

	def MuteVolume():
		mixer.music.set_volume(0.0)
		if(len(RelativeWindow.ButtonList)!=0):
			RelativeWindow.ConfigColor(0)
		MainWindow.ConfigColor(0)
	def LowVolume():
		mixer.music.set_volume(0.33)
		if(len(RelativeWindow.ButtonList)!=0):
			RelativeWindow.ConfigColor(1)
		MainWindow.ConfigColor(1)
	def MediumVolume():
		mixer.music.set_volume(0.66)
		if(len(RelativeWindow.ButtonList)!=0):
			RelativeWindow.ConfigColor(2)
		MainWindow.ConfigColor(2)
	def MaxVolume():
		mixer.music.set_volume(1.0)
		if(len(RelativeWindow.ButtonList)!=0):
			RelativeWindow.ConfigColor(3)
		MainWindow.ConfigColor(3)

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
		BrugerList=[]
		conn=mysql.connector.connect(host='34.88.203.155',user='UserAnton',password='RelativeDatabase',database='RelativeDatabase')
		#with pyodbc.connect('SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
		#with conn.cursor() as cursor:
		mycursor=conn.cursor()
		query="""SELECT * FROM RelativeDatabase"""
		m=mycursor.execute(query)
		allRows = mycursor.fetchall()
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
			conn=mysql.connector.connect(host='34.88.203.155',user='relativedatabase',password='RelativeDatabase',database='RelativeDatabase')
			with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
				with conn.cursor() as cursor:
					query="""SELECT *, CAST(Image AS VARCHAR(MAX)) FROM dbo.Test_table"""
					m=cursor.execute(query)
					allRows = cursor.fetchall()
					counter=0
					changedRows=[]
					for row in allRows:
						RelativeObj=Relative(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),row[5],row[6])
						if(RelativeDTO.BrugerList[counter].PersonID==row[0]):
							RelativeDTO.BrugerList[counter].PersonID=row[0]
							changedRows.append(Relative(row[0],str(row[1]),str(row[2]),str(row[3]),str(row[4]),row[5],row[6]))
					for relative in changedRows:
						RelativeDTO.BrugerList[counter].PersonID= relative.PersonID
						RelativeDTO.BrugerList[counter].LastName=str(relative.LastName)
						RelativeDTO.BrugerList[counter].FirstName=str(relative.FirstName)
						RelativeDTO.BrugerList[counter].DateOfBirth=str(relative.DateOfBirth)
						RelativeDTO.BrugerList[counter].Relation=str(relative.Relation)
						RelativeDTO.BrugerList[counter].PersonImage=relative.PersonImage
						RelativeDTO.BrugerList[counter].SOUND=relative.SOUND
						if(RelativeDTO.BrugerList[counter].PersonID==1):
							MainWindow.MainLabelList[0].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==2):
							MainWindow.MainLabelList[1].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==3):
							MainWindow.MainLabelList[2].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==4):
							MainWindow.MainLabelList[3].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==5):
							MainWindow.MainLabelList[4].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==6):
							MainWindow.MainLabelList[5].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==7):
							MainWindow.MainLabelList[6].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						elif (RelativeDTO.BrugerList[counter].PersonID==8):
							MainWindow.MainLabelList[7].config(text=RelativeDTO.BrugerList[counter].FirstName.title()+" " +RelativeDTO.BrugerList[counter].LastName.title())
						if RelativeDTO.BrugerList[counter].PersonImage !=None:
							if(os.path.exists('ImageFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.png')):
								os.remove('ImageFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.png')
							imageString = RelativeDTO.BrugerList[counter].PersonImage
							imagePre= io.BytesIO(imageString)	
							img= Image.open(imagePre)
							imageNameString=str(RelativeDTO.BrugerList[counter].PersonID)
							img.save('ImageFolder/Bruger'+imageNameString+'.png')
							Pictures.updatePicture(RelativeDTO.BrugerList[counter].PersonID)
						if RelativeDTO.BrugerList[counter].SOUND !=None:
							if(os.path.exists('AudioFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.mp3')):
								os.remove('AudioFolder/Bruger'+str(RelativeDTO.BrugerList[counter].PersonID)+'.mp3')
							audioString = RelativeDTO.BrugerList[counter].SOUND
							audioPre= io.BytesIO(audioString)	
							with open ('AudioFolder/Bruger'+str(row[0])+'.mp3','wb') as f:
								f.write(audioPre.getbuffer())
						#else:
						#Only use else statement for the update
						#	ErrorWindow.openErrorWindow('Der var en fejl ved opdatering af data.')
						counter+=1
			time.sleep(10)
												
class Pictures:
	#Can be used to add a picture
	#picture = Image.open(r'C:\Users\anton\OneDrive\Pictures\Bruger2.png')  
	#picture = picture.save("ImageFolder\Bruger2.png") 
	cwd = os.getcwd()
	cwdUser=cwd+"\ImageFolder"
	cwdSound=cwd+"\SoundImageFolder"
	Bruger1Billede=[]
	Bruger2Billede=[]
	Bruger3Billede=[]
	Bruger4Billede=[]
	Bruger5Billede=[]
	Bruger6Billede=[]
	Bruger7Billede=[]
	Bruger8Billede=[]
	newBruger1Billede=[]
	newBruger2Billede=[]
	newBruger3Billede=[]
	newBruger4Billede=[]
	newBruger5Billede=[]
	newBruger6Billede=[]
	newBruger7Billede=[]
	newBruger8Billede=[]
	def setPictures():
		#Indlæser billeder til menuer
		if(os.path.exists(Pictures.cwdUser+"\Bruger1.png")):
			Pictures.Bruger1Billede=Image.open(Pictures.cwdUser+"\Bruger1.png")
			Bruger1resized=Pictures.Bruger1Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger1Billede = ImageTk.PhotoImage(Bruger1resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger2.png")):
			Pictures.Bruger2Billede=Image.open(Pictures.cwdUser+"\Bruger2.png")
			Bruger2resized=Pictures.Bruger2Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger2Billede = ImageTk.PhotoImage(Bruger2resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger3.png")):
			Pictures.Bruger3Billede=Image.open(Pictures.cwdUser+"\Bruger3.png")
			Bruger3resized=Pictures.Bruger3Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger3Billede = ImageTk.PhotoImage(Bruger3resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger4.png")):
			Pictures.Bruger4Billede=Image.open(Pictures.cwdUser+"\Bruger4.png")
			Bruger4resized=Pictures.Bruger4Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger4Billede = ImageTk.PhotoImage(Bruger4resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger5.png")):
			Pictures.Bruger5Billede=Image.open(Pictures.cwdUser+"\Bruger5.png")
			Bruger5resized=Pictures.Bruger5Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger5Billede = ImageTk.PhotoImage(Bruger5resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger6.png")):
			Pictures.Bruger6Billede=Image.open(Pictures.cwdUser+"\Bruger6.png")
			Bruger6resized=Pictures.Bruger6Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger6Billede = ImageTk.PhotoImage(Bruger6resized)
		if(os.path.exists(Pictures.cwdUser+"\Bruger7.png")):
			Pictures.Bruger7Billede=Image.open(Pictures.cwdUser+'\Bruger7.png')
			Bruger7resized=Pictures.Bruger7Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger7Billede = ImageTk.PhotoImage(Bruger7resized)
		if(os.path.exists(Pictures.cwdUser+'\Bruger8.png')):
			Pictures.Bruger8Billede=Image.open(Pictures.cwdUser+'\Bruger8.png')
			Bruger8resized=Pictures.Bruger8Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger8Billede = ImageTk.PhotoImage(Bruger8resized)
	def updatePicture(ID):
		if(os.path.exists(Pictures.cwdUser+"\Bruger1.png") and ID==1):
			Pictures.Bruger1Billede=Image.open(Pictures.cwdUser+"\Bruger1.png")
			Bruger1resized=Pictures.Bruger1Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger1Billede = ImageTk.PhotoImage(Bruger1resized)
			MainWindow.MainBrugerList[0].config(image=Pictures.newBruger1Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger2.png")and ID==2):
			Pictures.Bruger2Billede=Image.open(Pictures.cwdUser+"\Bruger2.png")
			Bruger2resized=Pictures.Bruger2Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger2Billede = ImageTk.PhotoImage(Bruger2resized)
			MainWindow.MainBrugerList[1].config(image=Pictures.newBruger2Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger3.png")and ID==3):
			Pictures.Bruger3Billede=Image.open(Pictures.cwdUser+"\Bruger3.png")
			Bruger3resized=Pictures.Bruger3Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger3Billede = ImageTk.PhotoImage(Bruger3resized)
			MainWindow.MainBrugerList[2].config(image=Pictures.newBruger3Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger4.png")and ID==4):
			Pictures.Bruger4Billede=Image.open(Pictures.cwdUser+"\Bruger4.png")
			Bruger4resized=Pictures.Bruger4Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger4Billede = ImageTk.PhotoImage(Bruger4resized)
			MainWindow.MainBrugerList[3].config(image=Pictures.newBruger4Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger5.png")and ID==5):
			Pictures.Bruger5Billede=Image.open(Pictures.cwdUser+"\Bruger5.png")
			Bruger5resized=Pictures.Bruger5Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger5Billede = ImageTk.PhotoImage(Bruger5resized)
			MainWindow.MainBrugerList[4].config(image=Pictures.newBruger5Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger6.png")and ID==6):
			Pictures.Bruger6Billede=Image.open(Pictures.cwdUser+"\Bruger6.png")
			Bruger6resized=Pictures.Bruger6Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger6Billede = ImageTk.PhotoImage(Bruger6resized)
			MainWindow.MainBrugerList[5].config(image=Pictures.newBruger6Billede)
		elif(os.path.exists(Pictures.cwdUser+"\Bruger7.png")and ID==7):
			Pictures.Bruger7Billede=Image.open(Pictures.cwdUser+'\Bruger7.png')
			Bruger7resized=Pictures.Bruger7Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger7Billede = ImageTk.PhotoImage(Bruger7resized)
			MainWindow.MainBrugerList[6].config(image=Pictures.newBruger7Billede)
		elif(os.path.exists(Pictures.cwdUser+'\Bruger8.png')and ID==8):
			Pictures.Bruger8Billede=Image.open(Pictures.cwdUser+'\Bruger8.png')
			Bruger8resized=Pictures.Bruger8Billede.resize((150,150),Image.ANTIALIAS)
			Pictures.newBruger8Billede = ImageTk.PhotoImage(Bruger8resized)
			MainWindow.MainBrugerList[7].config(image=Pictures.newBruger8Billede)
	
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
	NewPlaybuttonBillede=PlaybuttonBillede.resize((135,135),Image.ANTIALIAS)
	NewPlaybuttonBillede = ImageTk.PhotoImage(NewPlaybuttonBillede)
	
	StopbuttonBillede = Image.open(cwdSound+"\StopButton.png")
	NewStopbuttonBillede=StopbuttonBillede.resize((135,135),Image.ANTIALIAS)
	NewStopbuttonBillede = ImageTk.PhotoImage(NewStopbuttonBillede)
				
class ErrorWindow:
	def openErrorWindow(ErrorType):
		errorWindow=Toplevel(Root.window)
		errorWindow.title("Error Window")
		errorWindow.geometry("800x480")
		errorWindow.attributes('-topmost', True)
		#On RPI set the below condition
		#errorrWindow.attributes('-fullscreen',True)
		Label(errorWindow,text="Error Window")
		if(ErrorType=='AudioError'):
			errorLabel=Label(errorWindow,text='There was error getting the audio',font=("Cambria",20))
			errorLabel.place(x=350,y=50)
			CloseWindow = Button(errorWindow, height ='2', width='20',bg='white', text='Godkend', command=errorWindow.closeErrorWindow)
			CloseWindow.pack()
			CloseWindow.place(x=350,y=250)
	def closeErrorWindow():
		AudioPlayer.Stop()
		ErrorWindow.destroy()		

class RelativeWindow:
	isPlaying=False
	ButtonList=[]
	def openRelativeWindow(_id):
		cwd = os.getcwd()
		ID=_id-1
		relativeObj=RelativeDTO.BrugerList[ID]
		newWindow=Toplevel(Root.root)
		newWindow.title("new window")
		newWindow.geometry("800x480")
		newWindow.attributes('-topmost', True)
		#On RPI set the below condition
		#newWindow.attributes('-fullscreen',True)
		Label(newWindow,text="New window") 
		if _id==1:
			preSizeImage=Pictures.Bruger1Billede
		elif _id==2:
			preSizeImage=Pictures.Bruger2Billede
		elif _id==3:
			preSizeImage=Pictures.Bruger3Billede
		elif _id==4:
			preSizeImage=Pictures.Bruger4Billede
		elif _id==5:
			preSizeImage=Pictures.Bruger5Billede
		elif _id==6:
			preSizeImage=Pictures.Bruger6Billede
		elif _id==7:
			preSizeImage=Pictures.Bruger7Billede
		elif _id==8:
			preSizeImage=Pictures.Bruger8Billede
		resizedImage = preSizeImage.resize((500,400), Image.ANTIALIAS)
		photoImg=ImageTk.PhotoImage(resizedImage)
		img = Label(newWindow,image=photoImg, bg='LightPink1',border=3)
		img.image = photoImg
		img.place(x=0, y=0)
		NameLabel = Label(newWindow,text="Jeg er "+relativeObj.FirstName.title()+" " +relativeObj.LastName.title(), font=("Cambria",13), wraplength=280)
		NameLabel.place(x=515, y=10)
		BirthdayLabel = Label(newWindow,text="Jeg blev født " + relativeObj.DateOfBirth, font=("Cambria",13))
		BirthdayLabel.place(x=515, y=75)
		RelationLabel= Label(newWindow, text="Jeg er din " + relativeObj.Relation.lower(), font=("Cambria",13))
		RelationLabel.place(x=515,y=140)
		PlayLabel= Label(newWindow, text="Tryk her for at høre mere om mig", font=("Cambria",13))
		PlayLabel.place(x=515,y=205)
		PlaySound = Button(newWindow, height ='140', width='140', bg = 'LightPink1', fg='white', image=Pictures.NewPlaybuttonBillede, command=lambda: AudioPlayer.StopOrPlay(_id,RelativeWindow.isPlaying,cwd))
		PlaySound.pack()
		PlaySound.place(x=590,y=250)

		CloseWindow = Button(newWindow, height ='1', width='13',bg='LightPink1', text='Luk vinduet', command=lambda: RelativeWindow.closeRelativeWindow(newWindow),font=("Cambria",25))
		CloseWindow.pack()
		CloseWindow.place(x=530,y=400)

		Mute = Button(newWindow, height ='64', width='64', bg = MainWindow.MainAudioList[0].cget('bg'), fg='white', image=Pictures.newMuteBilledeResize, command=lambda: AudioPlayer.MuteVolume())
		Mute.pack()
		Mute.place(x=70,y=407)
		RelativeWindow.ButtonList.append(Mute)

		Lyd1 = Button(newWindow, height ='64', width='64', bg = MainWindow.MainAudioList[1].cget('bg'), fg='white', image=Pictures.newLyd1BilledeResize, command=lambda: AudioPlayer.LowVolume())
		Lyd1.pack()
		Lyd1.place(x=170,y=407)
		RelativeWindow.ButtonList.append(Lyd1)

		Lyd2 = Button(newWindow, height ='64', width='64', bg = MainWindow.MainAudioList[2].cget('bg'), fg='white', image=Pictures.newLyd2BilledeResize, command=lambda: AudioPlayer.MediumVolume())
		Lyd2.pack()
		Lyd2.place(x=270,y=407)
		RelativeWindow.ButtonList.append(Lyd2)

		Lyd3 = Button(newWindow, height ='64', width='64', bg = MainWindow.MainAudioList[3].cget('bg'), fg='white', image=Pictures.newLyd3BilledeResize, command=lambda: AudioPlayer.MaxVolume())
		Lyd3.pack()
		Lyd3.place(x=370,y=407)
		RelativeWindow.ButtonList.append(Lyd3)
		AudioPlayer.StopOrPlay(RelativeWindow._id,RelativeWindow.isPlaying)

	def closeRelativeWindow(newWindow):
		RelativeWindow.ButtonList=[]
		AudioPlayer.Stop()
		newWindow.destroy()
		#this can be used to remove a picture
		#cwd = os.getcwd()
		#cwd+="\ImageFolder\Bruger2.png"
		#os.remove(cwd)
	def ConfigColor(ButtonId):
		if(len(RelativeWindow.ButtonList)!=0):
			for button in RelativeWindow.ButtonList:
				button.config(bg='red')
			RelativeWindow.ButtonList[ButtonId].config(bg='green')

class RelativeDTO:
	def __init__(self,BrugerList):
		self.BrugerList=BrugerList
	apiService= AzureApi()
	BrugerList=apiService.DownloadOnStartUp()
	x = th.Timer(5,AzureApi.update_search)
	x.start()
	
class MainWindow:
	MainWindow=Toplevel(Root.root)
	MainWindow.title("Erindringsdevice")
	MainWindow.geometry('800x480')
	#MainWindow.overrideredirect(1)
	MainAudioList=[]
	MainBrugerList=[]
	MainLabelList=[]
	#On RPI set the below condition
	#MainWindow.attributes('-fullscreen',True)
	relativeObj=RelativeDTO.BrugerList
	Pictures.setPictures()
	isPlaying=False
	if(relativeObj[0].PersonImage!=None):
		Bruger1Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger1Billede, command=lambda: RelativeWindow.openRelativeWindow(1))
		Bruger1Button.pack()
		Bruger1Button.place(x=40,y=10)
		MainBrugerList.append(Bruger1Button)
		Bruger1Label = Label(MainWindow,text=relativeObj[0].FirstName.title()+" " +relativeObj[0].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger1Label.place(x=40, y=170)
		MainLabelList.append(Bruger1Label)
	if(relativeObj[1].PersonImage!=None):
		Bruger2Button = Button(MainWindow,height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger2Billede,command=lambda: RelativeWindow.openRelativeWindow(2))
		Bruger2Button.pack()
		Bruger2Button.place(x=230,y=10)
		MainBrugerList.append(Bruger2Button)
		Bruger2Label = Label(MainWindow,text=relativeObj[1].FirstName.title()+" " +relativeObj[1].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger2Label.place(x=230, y=170)
		MainLabelList.append(Bruger2Label)
	if(relativeObj[2].PersonImage!=None):
		Bruger3Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger3Billede,command=lambda: RelativeWindow.openRelativeWindow(3))
		Bruger3Button.pack()
		Bruger3Button.place(x=420,y=10)
		MainBrugerList.append(Bruger3Button)
		Bruger3Label = Label(MainWindow,text=relativeObj[2].FirstName.title()+" " +relativeObj[2].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger3Label.pack()
		Bruger3Label.place(x=420, y=170)
		MainLabelList.append(Bruger3Label)
	if(relativeObj[3].PersonImage!=None):
		Bruger4Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger4Billede,command=lambda: RelativeWindow.openRelativeWindow(4))
		Bruger4Button.pack()
		Bruger4Button.place(x=610,y=10)
		MainBrugerList.append(Bruger4Button)
		Bruger4Label = Label(MainWindow,text=relativeObj[3].FirstName.title()+" " +relativeObj[3].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger4Label.place(x=610, y=170)
		MainLabelList.append(Bruger4Label)
	if(relativeObj[4].PersonImage!=None):
		Bruger5Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger5Billede,command=lambda: RelativeWindow.openRelativeWindow(5))
		Bruger5Button.pack()
		Bruger5Button.place(x=40,y=200)
		MainBrugerList.append(Bruger5Button)
		Bruger5Label = Label(MainWindow,text=relativeObj[4].FirstName.title() + " " +relativeObj[4].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger5Label.place(x=40, y=360)
		MainLabelList.append(Bruger5Label)
	if(relativeObj[5].PersonImage!=None):
		Bruger6Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger6Billede,command=lambda: RelativeWindow.openRelativeWindow(6))
		Bruger6Button.pack()
		Bruger6Button.place(x=230,y=200)
		MainBrugerList.append(Bruger6Button)
		Bruger6Label = Label(MainWindow,text=relativeObj[5].FirstName.title() + " " +relativeObj[5].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger6Label.place(x=230, y=360)
		MainLabelList.append(Bruger6Label)
	if(relativeObj[6].PersonImage!=None):
		Bruger7Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger7Billede,command=lambda: RelativeWindow.openRelativeWindow(7))
		Bruger7Button.pack()
		Bruger7Button.place(x=420,y=200)
		MainBrugerList.append(Bruger7Button)
		Bruger7Label = Label(MainWindow,text=relativeObj[6].FirstName.title()+" " +relativeObj[6].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger7Label.place(x=420, y=360)	
		MainLabelList.append(Bruger7Label)
	if(relativeObj[7].PersonImage!=None):
		Bruger8Button = Button(MainWindow, height ='154', width='154', bg = 'LightPink1', fg='white', image=Pictures.newBruger8Billede,command=lambda: RelativeWindow.openRelativeWindow(8))
		Bruger8Button.pack()
		Bruger8Button.place(x=610,y=200)
		MainBrugerList.append(Bruger8Button)
		Bruger8Label = Label(MainWindow,text=relativeObj[7].FirstName.title()+" " +relativeObj[7].LastName.title(), font=("Cambria",10), wraplength=280)
		Bruger8Label.place(x=610, y=360)
		MainLabelList.append(Bruger8Label)

	#Knapper til menu  -  lyd
	Mute = Button(MainWindow, height ='64', width='64', bg = 'red', fg='white', image=Pictures.newMuteBilledeResize, command=lambda: AudioPlayer.MuteVolume())
	Mute.pack()
	Mute.place(x=100,y=400)
	MainAudioList.append(Mute)

	Lyd1 = Button(MainWindow, height ='64', width='64', bg = 'red', fg='white', image=Pictures.newLyd1BilledeResize, command=lambda: AudioPlayer.LowVolume())
	Lyd1.pack()
	Lyd1.place(x=200,y=400)
	MainAudioList.append(Lyd1)

	Lyd2 = Button(MainWindow, height ='64', width='64', bg = 'red', fg='white', image=Pictures.newLyd2BilledeResize, command=lambda: AudioPlayer.MediumVolume())
	Lyd2.pack()
	Lyd2.place(x=300,y=400)
	MainAudioList.append(Lyd2)

	Lyd3 = Button(MainWindow, height ='64', width='64', bg = 'green', fg='white', image=Pictures.newLyd3BilledeResize, command=lambda: AudioPlayer.MaxVolume())
	Lyd3.pack()
	Lyd3.place(x=400,y=400)
	MainAudioList.append(Lyd3)

	CloseWindow = Button(MainWindow, height ='2', width='20',bg='LightPink1', text='Luk vinduet', font=("Cambria",15), command=Root.root.destroy)
	CloseWindow.pack()
	CloseWindow.place(x=530,y=400)

	def ConfigColor(ButtonId):
		for button in MainWindow.MainAudioList:
		    button.config(bg='red')
		MainWindow.MainAudioList[ButtonId].config(bg='green')

class Initiate:
	Root.root.attributes('-topmost',False)
	Root.root.update()
	Root.root.withdraw()
	Root.root.mainloop()
