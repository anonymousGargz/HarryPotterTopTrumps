from tkinter import ttk
import customtkinter 
from customtkinter import *
from PIL import ImageTk, Image

#Displays the HomePage, inherits from the gameInterface frame mainArea#
class HomePage(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color='#ebae3b')

        #Opens and resizes the Hufflepuff logo#
        imgHufflepuff=ImageTk.PhotoImage(Image.open('hufflepuffLogoUpdated.jpg'))
        imgHufflepuff=Image.open('hufflepuffLogoUpdated.jpg')
        resized=imgHufflepuff.resize((400,600))
        hufflepuffImage=ImageTk.PhotoImage(resized)

        #Opens and resizes the Gryffindor logo#
        imgGryffindor=ImageTk.PhotoImage(Image.open('gryffindorLogoUpdated.jpg'))
        imgGryffindor=Image.open('gryffindorLogoUpdated.jpg')
        resized=imgGryffindor.resize((400,300))
        gryffindorImage=ImageTk.PhotoImage(resized)

        #Opens and resizes the Ravenclaw logo#
        imgRavenclaw=ImageTk.PhotoImage(Image.open('ravenclawLogoUpdated.jpg'))
        imgRavenclaw=Image.open('ravenclawLogoUpdated.jpg')
        resized=imgRavenclaw.resize((400,300))
        ravenclawImage=ImageTk.PhotoImage(resized)

        #Opens and resizes the Slytherin logo#
        imgSlytherin=ImageTk.PhotoImage(Image.open('slytherinLogoUpdated.jpg'))
        imgSlytherin=Image.open('slytherinLogoUpdated.jpg')
        resized=imgSlytherin.resize((400,300))
        slytherinImage=ImageTk.PhotoImage(resized)

        #Creates the title and logo widgets#
        self.__title=customtkinter.CTkLabel(self, text='HARRY POTTER TOP TRUMPS', 
                                            font=('Berlin Sans FB Demi',40))
        self.__hufflepuffLogo=customtkinter.CTkLabel(self, fg_color='#e8af17', 
                                                     image= hufflepuffImage, corner_radius=50)
        self.__gryffindorLogo=customtkinter.CTkLabel(self, fg_color='#670001',
                                                     image= gryffindorImage, corner_radius=20)
        self.__ravenclawLogo=customtkinter.CTkLabel(self, fg_color='#3aa6cc', 
                                                    image= ravenclawImage, corner_radius=20)
        self.__slytherinLogo=customtkinter.CTkLabel(self, fg_color='#172a14', 
                                                    image= slytherinImage, corner_radius=20)

        #Places all the widgets that have been created#
        self.__title.place(relx=0.3, rely=0.1, relwidth=0.5, relheight=0.1)
        self.__hufflepuffLogo.place(relx=0.30, rely=0.5, relwidth=0.15, relheight=0.2)
        self.__gryffindorLogo.place(relx=0.05, rely=0.5, relwidth=0.15, relheight=0.2)
        self.__ravenclawLogo.place(relx=0.55, rely=0.5, relwidth=0.15, relheight=0.2)
        self.__slytherinLogo.place(relx=0.80, rely=0.5, relwidth=0.15, relheight=0.2)

        