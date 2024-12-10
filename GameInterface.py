from tkinter import ttk
import customtkinter 
from customtkinter import *
from PIL import ImageTk, Image
from pygame import mixer


from HomePage import HomePage
from RulesPage import RulesPage
from PlayPage import PlayPage
from ProgressPage import ProgressPage
from DeckPage import DeckPage

#Encompasses the main frame/ menu of the game, and inherits from the customtkinter module#
class gameInterface(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Displays background image#
        imgBackground=Image.open('backgroundImage.jpg')
        resized=imgBackground.resize((2250,1500))
        backgroundImage=ImageTk.PhotoImage(resized)
        
        self.__imageBackground=customtkinter.CTkLabel(self, image=backgroundImage)
        self.__imageBackground.place(relx=0,rely=0,relheight=1,relwidth=1)

        #Displays logo#
        imgLogo=Image.open('HogwartsLogo.jpg')
        resized=imgLogo.resize((1050,800))
        backgroundLogo=ImageTk.PhotoImage(resized)

        #Creates frame#
        self.mainArea=customtkinter.CTkFrame(self, fg_color='#ebae3b')
        self.mainArea.place(relx=0.15, rely=0.1, relwidth=0.8, relheight=0.7)

        #Creates logo#
        self.__HogwartsLogo=customtkinter.CTkLabel(self.mainArea, image=backgroundLogo, text='')
        self.__HogwartsLogo.place(relx=0.2,rely=0.15,relheight=0.7,relwidth=0.59)
        
        
        self.currentPageNumber= 0
#       List of pages:
        self.pages=[HomePage(self.mainArea), PlayPage(self.mainArea), DeckPage(self.mainArea), 
                    RulesPage(self.mainArea), ProgressPage(self.mainArea)]
    
        for i in range(1,5):
            self.pages[i].place_forget()
      
        self.title("Harry Potter Top Trumps")

        self.geometry("2000x2000")

        self.loadPageWidgets()
        self.playMusic()
        self.mainloop()
    
    def loadPageWidgets(self):
        self.createSidebarMenu()
        

    #Creates the sidebar menu with the frames and buttons#
    def createSidebarMenu(self):
        self.__menu=customtkinter.CTkFrame(self, fg_color='#ebae3b')
        self.__menu.place(relx=0, rely=0, relwidth=0.1, relheight=1)

        rulesButton=customtkinter.CTkButton(self.__menu, text='Rules', fg_color='#d6931f', 
                                            font=('Berlin Sans FB Demi', 25),corner_radius= 20, 
                                            hover_color='#6d4814', command=lambda buttonPressed='Rules':
                                            ChangePage(buttonPressed))
        rulesButton.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

        playButton=customtkinter.CTkButton(self.__menu, text='Play', fg_color='#d6931f', 
                                           font=('Berlin Sans FB Demi', 25), corner_radius=20, 
                                           hover_color='#6d4814', command=lambda buttonPressed='Play':
                                           (buttonPressed))
        playButton.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        progressButton=customtkinter.CTkButton(self.__menu, text='Progress', fg_color='#d6931f', 
                                               font=('Berlin Sans FB Demi', 25), corner_radius=20,
                                                 hover_color='#6d4814', command=lambda buttonPressed=
                                                 'Progress':ChangePage(buttonPressed))
        progressButton.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        deckButton=customtkinter.CTkButton(self.__menu, text='Deck', fg_color='#d6931f', 
                                           font=('Berlin Sans FB Demi', 25), corner_radius=20, 
                                           hover_color='#6d4814', command=lambda buttonPressed='Deck':
                                           ChangePage(buttonPressed))
        deckButton.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)

        homeButton=customtkinter.CTkButton(self.__menu, text='Home', fg_color='#d6931f', 
                                           font=('Berlin Sans FB Demi', 25), corner_radius=20, 
                                           hover_color='#6d4814',command=lambda buttonPressed='Home':
                                           ChangePage(buttonPressed))
        homeButton.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)


        #Brings frame to the front of the others depending on the button chosen by the user#
        def ChangePage(buttonPressed):
            self.pages[self.currentPageNumber].place_forget()
            match buttonPressed:
                case 'Play':
                    self.currentPageNumber=1
                    self.pages[self.currentPageNumber].tkraise
                    self.pages[self.currentPageNumber].place(relx=0,rely=0,relwidth=1,relheight=1)
                
                case 'Rules':
                    self.currentPageNumber=3
                    self.pages[self.currentPageNumber].tkraise
                    self.pages[self.currentPageNumber].place(relx=0,rely=0,relwidth=1,relheight=1)
                
                case 'Progress':
                    self.currentPageNumber=4
                    self.pages[self.currentPageNumber].tkraise
                    self.pages[self.currentPageNumber].place(relx=0,rely=0,relwidth=1,relheight=1)
                
                case'Deck':
                    self.currentPageNumber=2
                    self.pages[self.currentPageNumber].tkraise
                    self.pages[self.currentPageNumber].place(relx=0,rely=0,relwidth=1,relheight=1)
                case 'Home':
                    self.currentPageNumber=0
                    self.pages[self.currentPageNumber].tkraise
                    self.pages[self.currentPageNumber].place(relx=0,rely=0,relwidth=1,relheight=1)
            
            #Disables the button of the page that the user is currently on#
            if self.currentPageNumber==0:
                homeButton.configure(state=customtkinter.DISABLED)
                playButton.configure(state='normal')
                rulesButton.configure(state='normal')
                progressButton.configure(state='normal')
                deckButton.configure(state='normal')
            
            if self.currentPageNumber==1:
                playButton.configure(state='disabled')
                homeButton.configure(state='normal')
                rulesButton.configure(state='normal')
                progressButton.configure(state='normal')
                deckButton.configure(state='normal')
            if self.currentPageNumber==2:
                deckButton.configure(state='disabled')
                playButton.configure(state='normal')
                homeButton.configure(state='normal')
                progressButton.configure(state='normal')
                rulesButton.configure(state='normal')
            
            if self.currentPageNumber==3:
                rulesButton.configure(state='disabled')
                playButton.configure(state='normal')
                progressButton.configure(state='normal')
                homeButton.configure(state='normal')
                deckButton.configure(state='normal')
            
            if self.currentPageNumber==4:
                progressButton.configure(state='disabled')
                playButton.configure(state='normal')
                rulesButton.configure(state='normal')
                deckButton.configure(state='normal')
                homeButton.configure(state='normal')

    #Plays music in the background- Hedwig's theme from Harry Potter#
    def playMusic(self):
        mixer.init()
        mixer.music.load('HedwigsTheme.mp3')
        mixer.music.play(loops=-1)
        
gameInterface()

