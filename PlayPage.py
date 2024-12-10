import customtkinter 
from customtkinter import *
from PIL import ImageTk, Image

from PlayPageElements import Player1Timer
from PlayPageElements import GetPlayer1Values
from PlayPageElements import GetPlayer2Values
from PlayPageElements import PauseTimer
from PlayPageElements import CreateNewObjects


#Displays the elements on the PlayPage, inherits from the gameInterface frame mainArea#
class PlayPage(customtkinter.CTkFrame):
    def __init__(self,parent):
            super().__init__(parent, fg_color='#670001')

            #Displays the background image#
            imgBackground=Image.open('GryffindorRoom.png')
            resized=imgBackground.resize((2250,1500))
            backgroundImage=ImageTk.PhotoImage(resized)
        
            self.__imageBackground=customtkinter.CTkLabel(self, image=backgroundImage)
            self.__imageBackground.place(relx=0,rely=0,relheight=1,relwidth=1)

            #opens the BackOfCard image#
            BackOfCard=Image.open('BACKOFCARD.jpg')
            imgBackOfCard=ImageTk.PhotoImage(BackOfCard, master=self)

            
            self.__KillTimerPlayer1=False
            self.__KillTimerPlayer2=False

            self.__PauseTimerPlayer1=False
            self.__PauseTimerPlayer2=False
            
            
            self.__countdownTimerIconPlayer1=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                                    corner_radius=20, text='', 
                                                                    font=('Berlin Sans FB Demi', 20))
            self.__countdownTimerIconPlayer2=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                                    corner_radius=20, text='', 
                                                                    font=('Berlin Sans FB Demi', 20))

            #Card display for Player 1- displays all the widgets#
            self.__BackOfCards1Player1=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards1Player1.place(relx=0.085, rely=0.125,relwidth=0.3,relheight=0.8)

            self.__BackOfCards2Player1=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards2Player1.place(relx=0.075, rely=0.135,relwidth=0.3,relheight=0.8)

            self.__BackOfCards3Player1=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards3Player1.place(relx=0.097, rely=0.1,relwidth=0.3,relheight=0.8)
            
            self.Player1Card=customtkinter.CTkLabel(self,fg_color='#fae6e6',corner_radius=20, text='')
            self.Player1Card.place(relx=0.1, rely=0.15,relwidth=0.25,relheight=0.7)

            self.NameLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b', 
                                                         text='', font=('Berlin Sans FB Demi', 20))
            self.NameLabelPlayer1.place(in_=self.Player1Card, relx=0.0,rely=0.0, relheight=0.1,
                                        relwidth=1)

            self.__SkillLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b', 
                                                            text='SpellSkill:',text_color='white',
                                                            font=('Berlin Sans FB Demi', 20), 
                                                            corner_radius=20)
            self.__SkillLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.15, relheight=0.1,
                                           relwidth=0.5)

            self.__SpellSkillPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                             corner_radius=20, text='', 
                                                             font=('Berlin Sans FB Demi', 20),
                                                             command=lambda valueChosen=
                                                             'SpellSkillPlayer1': 
                                                             GetPlayer1Values.__GetValueChosenByPlayer1__
                                                             (self,valueChosen))
            self.__SpellSkillPlayer1.place(in_=self.Player1Card,relx=0.65,rely=0.15, relheight=0.1,
                                           relwidth=0.2)

            self.__BraverySkillLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b',
                                                                    text='BraverySkill:',
                                                                    text_color='white' ,
                                                                    font=('Berlin Sans FB Demi', 20), 
                                                                    corner_radius=20)
            self.__BraverySkillLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.3, 
                                                  relheight=0.1,relwidth=0.5)

            self.__BraverySkillPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                               corner_radius=20, text='', 
                                                               font=('Berlin Sans FB Demi', 20),
                                                               command=lambda 
                                                               valueChosen='BraverySkillPlayer1': 
                                                               GetPlayer1Values.__GetValueChosenByPlayer1__
                                                               (self,valueChosen))
            self.__BraverySkillPlayer1.place(in_=self.Player1Card,relx=0.65,rely=0.30, relheight=0.1,
                                             relwidth=0.2)

            self.__BroomSkillLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b', 
                                                                 text='BroomSkill:',text_color='white' ,
                                                                 font=('Berlin Sans FB Demi', 20), 
                                                                 corner_radius=20)
            self.__BroomSkillLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.45, 
                                                relheight=0.1,relwidth=0.5)
            
            self.__BroomSkillPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                             corner_radius=20, text='', 
                                                             font=('Berlin Sans FB Demi', 20), command=
                                                             lambda valueChosen='BroomSkillPlayer1': 
                                                             GetPlayer1Values.__GetValueChosenByPlayer1__
                                                             (self,valueChosen))
            self.__BroomSkillPlayer1.place(in_=self.Player1Card, relx=0.65,rely=0.45, relheight=0.1,
                                           relwidth=0.2)

            self.KindnessSkillLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b',
                                                                   text='Kindness:',text_color='white', 
                                                                   font=('Berlin Sans FB Demi', 20), 
                                                                   corner_radius=20)
            self.KindnessSkillLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.6, 
                                                 relheight=0.1,relwidth=0.5)

            self.__KindnessSkillPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                                corner_radius=20, text='',
                                                                font=('Berlin Sans FB Demi', 20), 
                                                                command=lambda valueChosen=
                                                                'KindnessSkillPlayer1': 
                                                                GetPlayer1Values.__GetValueChosenByPlayer1__
                                                                (self,valueChosen))
            self.__KindnessSkillPlayer1.place(in_=self.Player1Card, relx=0.65,rely=0.60, relheight=0.1,
                                              relwidth=0.2)

            self.__StrengthSkillLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b',
                                                                     text='StrengthSkill:',text_color=
                                                                     'white', 
                                                                     font=('Berlin Sans FB Demi', 20), 
                                                                     corner_radius=20)
            self.__StrengthSkillLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.75, 
                                                   relheight=0.1,relwidth=0.5)
            
            self.__StrengthSkillPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                                corner_radius=20, text='',
                                                                font=('Berlin Sans FB Demi', 20), 
                                                                command=lambda valueChosen=
                                                                'StrengthSkillPlayer1': 
                                                                GetPlayer1Values.__GetValueChosenByPlayer1__
                                                                (self,valueChosen))
            self.__StrengthSkillPlayer1.place(in_=self.Player1Card, relx=0.65,rely=0.75, relheight=0.1,
                                              relwidth=0.2)

            self.__TopTrumpsRatingLabelPlayer1=customtkinter.CTkLabel(self.Player1Card, fg_color='#8f0e1b',
                                                                       text='TopTrumpsRating:',text_color=
                                                                       'white', 
                                                                       font=('Berlin Sans FB Demi', 20), 
                                                                       corner_radius=20)
            self.__TopTrumpsRatingLabelPlayer1.place(in_=self.Player1Card, relx=0.05,rely=0.9, 
                                                     relheight=0.1,relwidth=0.5)

            self.__TopTrumpsRatingPlayer1=customtkinter.CTkButton(self.Player1Card, fg_color='#ebae3b',
                                                                  corner_radius=20, text='', 
                                                                  font=('Berlin Sans FB Demi', 20),
                                                                  command=lambda valueChosen=
                                                                  'TopTrumpsRatingPlayer1':
                                                                  GetPlayer1Values.GetValueChosenByPlayer1__
                                                                  (self,valueChosen))
            self.__TopTrumpsRatingPlayer1.place(in_=self.Player1Card, relx=0.65,rely=0.9, 
                                                relheight=0.1,relwidth=0.2)

            
            #Card display for Player 2- displays all the widgets#
            
            self.__BackOfCards1Player2=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards1Player2.place(relx=0.585, rely=0.125,relwidth=0.3,relheight=0.8)

            self.__BackOfCards2Player2=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards2Player2.place(relx=0.575, rely=0.135,relwidth=0.3,relheight=0.8)

            self.__BackOfCards3Player2=customtkinter.CTkLabel(self, fg_color='#670001', 
                                                              image=imgBackOfCard, corner_radius=20)
            self.__BackOfCards3Player2.place(relx=0.597, rely=0.1,relwidth=0.3,relheight=0.8)

            self.Player2Card=customtkinter.CTkLabel(self,fg_color='#fae6e6',corner_radius=20, text='')
            self.Player2Card.place(relx=0.6, rely=0.15,relwidth=0.25,relheight=0.7)

            self.NameLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b', 
                                                         font=('Berlin Sans FB Demi', 20), text='')
            self.NameLabelPlayer2.place(in_=self.Player2Card, relx=0,rely=0, relheight=0.1,relwidth=1)

            self.__SpellSkillLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b', 
                                                                 text='SpellSkill:',text_color='white',
                                                                 font=('Berlin Sans FB Demi', 20), 
                                                                 corner_radius=20)
            self.__SpellSkillLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.15, 
                                                relheight=0.1,relwidth=0.5)

            self.__SpellSkillPlayer2=customtkinter.CTkButton(self.Player2Card, fg_color='#ebae3b',
                                                             corner_radius=20, text='', 
                                                             font=('Berlin Sans FB Demi', 20),
                                                             command=lambda valueChosen=
                                                             'SpellSkillPlayer2': 
                                                             GetPlayer2Values.__GetValueChosenByPlayer2__
                                                             (self,valueChosen))
            self.__SpellSkillPlayer2.place(in_=self.Player2Card, relx=0.65,rely=0.15, 
                                           relheight=0.1,relwidth=0.2)

            self.__BraverySkillLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, 
                                                                   fg_color='#8f0e1b', 
                                                                   text='BraverySkill:',
                                                                   text_color='white' ,
                                                                   font=('Berlin Sans FB Demi', 20), 
                                                                   corner_radius=20)
            self.__BraverySkillLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.3, 
                                                  relheight=0.1,relwidth=0.5)

            self.__BraverySkillPlayer2=customtkinter.CTkButton(self.Player2Card, fg_color='#ebae3b',
                                                               corner_radius=20, text='', 
                                                               font=('Berlin Sans FB Demi', 20),
                                                               command=lambda valueChosen=
                                                               'BraverySkillPlayer2': 
                                                               GetPlayer2Values.__GetValueChosenByPlayer2__
                                                               (self,valueChosen))
            self.__BraverySkillPlayer2.place(in_=self.Player2Card,relx=0.65,rely=0.30, relheight=0.1,
                                             relwidth=0.2)

            self.__BroomSkillLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b',
                                                                  text='BroomSkill:',text_color='white' ,
                                                                  font=('Berlin Sans FB Demi', 20), 
                                                                  corner_radius=20)
            self.__BroomSkillLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.45, 
                                                relheight=0.1,relwidth=0.5)
            
            self.__BroomSkillPlayer2=customtkinter.CTkButton(self.Player2Card, fg_color='#ebae3b',
                                                             corner_radius=20, text='', 
                                                             font=('Berlin Sans FB Demi', 20),
                                                             command=lambda valueChosen=
                                                             'BroomSkillPlayer2': 
                                                             GetPlayer2Values.__GetValueChosenByPlayer2__
                                                             (self,valueChosen))
            self.__BroomSkillPlayer2.place(in_=self.Player2Card,relx=0.65,rely=0.45, relheight=0.1,
                                           relwidth=0.2)

            self.__KindnessSkillLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b', 
                                                                    text='Kindness:',text_color='white', 
                                                                    font=('Berlin Sans FB Demi', 20), 
                                                                    corner_radius=20)
            self.__KindnessSkillLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.6, 
                                                   relheight=0.1,relwidth=0.5)


            self.__KindnessSkillPlayer2=customtkinter.CTkButton(self.Player2Card, fg_color='#ebae3b',
                                                                corner_radius=20, text='', 
                                                                font=('Berlin Sans FB Demi', 20),
                                                                command=lambda valueChosen=
                                                                'KindnessSkillPlayer2': 
                                                                GetPlayer2Values.__GetValueChosenByPlayer2__
                                                                (self,valueChosen))
            self.__KindnessSkillPlayer2.place(in_=self.Player2Card,relx=0.65,rely=0.60, relheight=0.1,
                                              relwidth=0.2)

            self.__StrengthSkillLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b', 
                                                                    text='StrengthSkill:',
                                                                    text_color='white', 
                                                                    font=('Berlin Sans FB Demi', 20), 
                                                                    corner_radius=20)
            self.__StrengthSkillLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.75, 
                                                   relheight=0.1,
                                                   relwidth=0.5)


            self.__StrengthSkillPlayer2=customtkinter.CTkButton(self.Player2Card, fg_color='#ebae3b',
                                                                corner_radius=20, text='', 
                                                                font=('Berlin Sans FB Demi', 20),
                                                                command=lambda valueChosen=
                                                                'StrengthSkillPlayer2': 
                                                                GetPlayer2Values.__GetValueChosenByPlayer2__
                                                                (self,valueChosen))
            self.__StrengthSkillPlayer2.place(in_=self.Player2Card,relx=0.65,rely=0.75, relheight=0.1,
                                              relwidth=0.2)

            self.__TopTrumpsRatingLabelPlayer2=customtkinter.CTkLabel(self.Player2Card, fg_color='#8f0e1b', 
                                                                      text='TopTrumpsRating:',
                                                                      text_color='white', 
                                                                      font=('Berlin Sans FB Demi', 20), 
                                                                      corner_radius=20)
            self.__TopTrumpsRatingLabelPlayer2.place(in_=self.Player2Card, relx=0.05,rely=0.9, 
                                                     relheight=0.1,relwidth=0.5)

            self.__TopTrumpsRatingPlayer2=customtkinter.CTkButton(self.Player2Card, 
                                                                  fg_color='#ebae3b',corner_radius=20, 
                                                                  text='', font=('Berlin Sans FB Demi', 20),
                                                                  command=lambda valueChosen=
                                                                  'TopTrumpsRatingPlayer2': 
                                                                  GetPlayer2Values.__GetValueChosenByPlayer2__
                                                                  (self, valueChosen))
            self.__TopTrumpsRatingPlayer2.place(relx=0.65,rely=0.9, relheight=0.1,relwidth=0.2)

            self.__countdownTimerIconPlayer1.place(relx=0.1, rely=0.025, relwidth=0.1, relheight=0.05)
            self.__countdownTimerIconPlayer2.place(relx=0.8, rely=0.025, relwidth=0.1, relheight=0.05)

            self.__PlayButton=customtkinter.CTkButton(self, fg_color='#04020a', corner_radius=20, 
                                                      text='PLAY GAME', font=('Berlin Sans FB Demi', 20), 
                                                      command= lambda: Player1Timer.__Player1Turn__(self))
            self.__PlayButton.place(relx=0.42, rely=0.3, relwidth=0.15, relheight=0.15)

            self.__YesPlayAgain=customtkinter.CTkButton(self, fg_color='#ebae3b', corner_radius=20, 
                                                        text='SHUFFLE', font=('Berlin Sans FB Demi',15 ),
                                                        command=lambda :CreateNewObjects.CreateNewObjects
                                                        (self) )
            self.__YesPlayAgain.place(relx=0.45, rely=0.55, relheight=0.1, relwidth=0.1)
            
            self.__PauseGame=customtkinter.CTkButton(self, fg_color='#04020a', corner_radius=20, 
                                                     text='PAUSE GAME', font=('Berlin Sans FB Demi',15 ), 
                                                     command= lambda: PauseTimer.__DecideWhoseTurn__(self))
            self.__PauseGame.place(relx=0.45, rely=0.75, relheight=0.1, relwidth=0.1)

            
            self.__BackOfCard=customtkinter.CTkLabel(self, fg_color='#670001', image=imgBackOfCard, 
                                                     corner_radius=20, text='')
            self.__BackOfCard.place_forget()
            
            self.__WinnerBanner=customtkinter.CTkLabel(self, fg_color='#670001', corner_radius=20, 
                                                       text='', text_color='white')
            self.__WinnerBanner.pack_forget()

    
    #Returns the stat values displayed on both Player1/Player2's buttons in a list#
    def ReturnSpellSkill(self):
        SpellSkillValues= [int(self.__SpellSkillPlayer1.cget("text")), 
                           int(self.__SpellSkillPlayer2.cget("text"))]
        print(SpellSkillValues)
        return SpellSkillValues
    
    def ReturnBraverySkill(self):
        BraverySkillValues= [int(self.__BraverySkillPlayer1.cget("text")), 
                             int(self.__BraverySkillPlayer2.cget("text"))]
        return BraverySkillValues
    
    def ReturnBroomSkill(self):
        BroomSkillValues= [int(self.__BroomSkillPlayer1.cget("text")), 
                           int(self.__BroomSkillPlayer2.cget("text"))]
        return BroomSkillValues
    
    def ReturnKindnessSkill(self):
        KindnessSkillValues= [int(self.__KindnessSkillPlayer1.cget("text")), 
                              int(self.__KindnessSkillPlayer2.cget("text"))]
        return KindnessSkillValues
    
    def ReturnStrengthSkill(self):
        StrengthSkillValues= [int(self.__StrengthSkillPlayer1.cget("text")), 
                              int(self.__StrengthSkillPlayer2.cget("text"))]
        return StrengthSkillValues
    
    def ReturnTopTrumpsRating(self):
        TopTrumpsRatingSkillValues= [int(self.__TopTrumpsRatingPlayer1.cget("text")), 
                                     int(self.__TopTrumpsRatingPlayer2.cget("text"))]
        return TopTrumpsRatingSkillValues

#Displays the value on the correct stat button on Player1's card using the value at the 
    #appropriate index of the CharacterValuesPlayer1 
#list
    def ConfigureCardPlayer1(self, CharacterValuesPlayer1):
        self.NameLabelPlayer1.configure(text=(CharacterValuesPlayer1[1],CharacterValuesPlayer1[2]))
        self.__SpellSkillPlayer1.configure(text=CharacterValuesPlayer1[3])
        self.__BraverySkillPlayer1.configure(text=CharacterValuesPlayer1[4])
        self.__BroomSkillPlayer1.configure(text=CharacterValuesPlayer1[5])
        self.__KindnessSkillPlayer1.configure(text=CharacterValuesPlayer1[6])
        self.__StrengthSkillPlayer1.configure(text=CharacterValuesPlayer1[7])
        self.__TopTrumpsRatingPlayer1.configure(text=CharacterValuesPlayer1[8])

#Displays the value on the correct stat button on Player2's card using the value at the 
        #appropriate index of the CharacterValuesPlayer2
#list    
    def ConfigureCardPlayer2(self, CharacterValuesPlayer2):
        self.NameLabelPlayer2.configure(text=(CharacterValuesPlayer2[1],CharacterValuesPlayer2[2]))
        self.__SpellSkillPlayer2.configure(text=CharacterValuesPlayer2[3])
        self.__BraverySkillPlayer2.configure(text=CharacterValuesPlayer2[4])
        self.__BroomSkillPlayer2.configure(text=CharacterValuesPlayer2[5])
        self.__KindnessSkillPlayer2.configure(text=CharacterValuesPlayer2[6])
        self.__StrengthSkillPlayer2.configure(text=CharacterValuesPlayer2[7])
        self.__TopTrumpsRatingPlayer2.configure(text=CharacterValuesPlayer2[8])

#Displays the string stored in the text variable on the countdownTimerIcons#    
    def ConfigureCountdownTimerIconPlayer1(self, text):
        self.__countdownTimerIconPlayer1.configure(text=text, text_color='#f5f0f0')
    
    def ConfigureCountdownTimerIconPlayer2(self, text):
        self.__countdownTimerIconPlayer2.configure(text=text, text_color='#f5f0f0')

#Returns the text on the countdownTimerIcons#
    def ReturnTimerPlayer1(self):
        try:
            return self.__countdownTimerIconPlayer1.cget('text')
        except:
            return None
    

    def ReturnTimerPlayer2(self):
        try:
            return self.__countdownTimerIconPlayer2.cget('text')
        except:
            return None

#Returns the KillTimerPlayer1/Player2 attribute values#
    def GetKillPlayer1(self):
        return self.__KillTimerPlayer1
    
    def GetKillPlayer2(self):
        return self.__KillTimerPlayer2
    
#Sets the KillTimerPlayer1/Player2 attribute values to whatever is stored in the value argument#
    def SetKillTimerPlayer1(self,value):
        self.__KillTimerPlayer1=value
    
    def SetKillTimerPlayer2(self,value):
        self.__KillTimerPlayer2=value

#Returns the PauseTimerPlayer1/Player2 attribute values#    
    def GetPausePlayer1(self):
        return self.__PauseTimerPlayer1
    
    def GetPausePlayer2(self):
        return self.__PauseTimerPlayer2

#Sets the PauseTimerPlayer1/Player2 attribute values to whatever is stored in the value argument#   
    def SetPauseTimerPlayer1(self,value):
        self.__PauseTimerPlayer1=value
    
    def SetPauseTimerPlayer2(self,value):
        self.__PauseTimerPlayer2=value


#Places the WinnerBanner label on the screen#
    def DisplayWinnerBanner(self):
        self.__WinnerBanner.place(relx=0,rely=0,relwidth=1,relheight=1)

#Removes the WinnerBanner label from the screen#    
    def ForgetWinnerBanner(self):
        self.__WinnerBanner.place_forget()

#Updates the text on the WinnerBanner label#
    def UpdateWinnerBannerText(self, text):
        self.__WinnerBanner.configure(text=text, text_color='white', font=('Berlin Sans FB Demi', 60))

#Places the BackOfCard image over the Player1Card#
    def HidePlayer1Card(self):
        self.__BackOfCard.place(relx=0.1, rely=0.1,relwidth=0.3,relheight=0.8)

#Places the BackOfCard image over the Player2Card#   
    def HidePlayer2Card(self):
        self.__BackOfCard.place(relx=0.6, rely=0.1,relwidth=0.3,relheight=0.8)

#Removes the BackOfCard image#   
    def RemoveBackOfCard(self):
        self.__BackOfCard.place_forget()

#Amends the state of the PlayGame/Shuffle/Pause buttons#   
    def AmendPlayGameButton(self, state):
        self.__PlayButton.configure(state=state)

    def AmendShuffleButton(self, state):
        self.__YesPlayAgain.configure(state=state)
    
    def AmendPauseButton(self, state):
        self.__PauseGame.configure(state=state)

#Updates the text on the Shuffle button#      
    def UpdateShuffleButton(self, text):
        self.__YesPlayAgain.configure(text=text)





