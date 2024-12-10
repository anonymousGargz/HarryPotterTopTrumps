import customtkinter
from customtkinter import *
from PIL import ImageTk, Image

#Displays the RulesPage, inherits from the gameInterface frame mainArea#
class RulesPage(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color='#ebae3b')
        
        #Displays the background image for the RulesPage#
        imgBackground=Image.open('HufflepuffRoom.webp')
        resized=imgBackground.resize((2250,1500))
        backgroundImage=ImageTk.PhotoImage(resized)
        
        self.__imageBackground=customtkinter.CTkLabel(self, image=backgroundImage)
        self.__imageBackground.place(relx=0,rely=0,relheight=1,relwidth=1)

        #Displays the canvas#
        self.__canvas=customtkinter.CTkCanvas(self, background='#ffcc12', scrollregion=(0,0,1500, 1500))
        self.__canvas.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)

        self.__Frame=customtkinter.CTkFrame(self.__canvas, fg_color='#ffcc12')

        #Displays the rules of the game on a scrolling window#
        RulesLabel1=customtkinter.CTkLabel(self.__Frame, text='1. Game Rules', 
                                           font=('Berlin Sans FB Demi',20))
        RulesLabel1.pack()

        RulesLabel2=customtkinter.CTkLabel(self.__Frame, 
                                           text= "\n -To start playing the game, click the 'Play Game' button on the play page screen. Player1 has the deck on the left, and Player2 has the deck on the right.", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel2.pack()
        
        RulesLabel3=customtkinter.CTkLabel(self.__Frame, text="\n -The aim of the game is to win as many points as possible per round, so you can unlock more cards and have a go at the quiz!", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel3.pack()

        RulesLabel4=customtkinter.CTkLabel(self.__Frame, text="\n -Each player will be randomly dealt a deck of cards, whose size will depend on the overall size of the deck; at the start each player gets 5 cards", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel4.pack()

        RulesLabel15=customtkinter.CTkLabel(self.__Frame, text="\n -But up to 49 cards can be unlocked, so eventually, each player can have up to 24 cards in their deck for each game!", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel15.pack()

        RulesLabel5=customtkinter.CTkLabel(self.__Frame, text="\n -It is always Player 1's turn first.", font=('Berlin Sans FB Demi',15))
        RulesLabel5.pack()
        RulesLabel6=customtkinter.CTkLabel(self.__Frame, text="\n - When you click 'Play Game', Player 1's countdown timer will start, and they will have 10 seconds to pick a category from their character card", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel6.pack()

        RulesLabel6=customtkinter.CTkLabel(self.__Frame, text="\n -Either player cannot see the other's deck.", font=('Berlin Sans FB Demi',15))
        RulesLabel6.pack()

        RulesLabel17=customtkinter.CTkLabel(self.__Frame, text="\n -Each character card has a rating out of a hundred for each of SpellSkill, Bravery, BroomSkill, Strength, Kindness, and out of 10 for TopTrumpsRating", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel17.pack()

        RulesLabel7=customtkinter.CTkLabel(self.__Frame, text="\n -You have to select a category for your character by clicking on it whose score you think would be higher than the other player's to win the round and gain 3 points", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel7.pack()

        RulesLabel8=customtkinter.CTkLabel(self.__Frame, text="\n -If your score is lower, you will only gain 1", font=('Berlin Sans FB Demi',15))
        RulesLabel8.pack()

        RulesLabel8=customtkinter.CTkLabel(self.__Frame, text="\n -However,it is not as simple as picking the highest number", font=('Berlin Sans FB Demi',15))
        RulesLabel8.pack()

        RulesLabel9=customtkinter.CTkLabel(self.__Frame, text="\n -For example, if you've already played a card with SpellSkill 100, and your card has SpellSkill 99, pick this(no higher/same rankings in this category).", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel9.pack()

        RulesLabel9=customtkinter.CTkLabel(self.__Frame, text="\n -No two cards can have the same ranking for any category. Once Player1 has picked, it's Player 2's turn, and the process repeats until the deck runs out", 
                                           font=('Berlin Sans FB Demi',15))
        RulesLabel9.pack()

        RulesLabel10=customtkinter.CTkLabel(self.__Frame, text="\n -Once the game is over, an overall winner will be declared (whoever won the most rounds). To play game again, click 'Shuffle cards' and 'Play Game' again", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel10.pack()

        RulesLabel11=customtkinter.CTkLabel(self.__Frame, text="\n -For every 15 points Player 1 wins in the rounds, a quiz will pop up; you can only answer up to 3 questions, and gain 3 points for each correct answer", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel11.pack()

        RulesLabel12=customtkinter.CTkLabel(self.__Frame, text="\n -For every 20 points Player 1 wins, including points gained from the quiz, a new card is unlocked!", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel12.pack()

        RulesLabel20=customtkinter.CTkLabel(self.__Frame, text="\n -All cards and their status( locked/unlocked) can be viewed on the Deck page ", font=('Berlin Sans FB Demi',15))
        RulesLabel20.pack()

        RulesLabel13=customtkinter.CTkLabel(self.__Frame, text="\n -You can pause the game at any time to visit other pages by clicking the pause button, and then pressing the space bar to resume ", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel13.pack()

        RulesLabel14=customtkinter.CTkLabel(self.__Frame, text="\n -The points you've gained overall in the last 5 days are displayed in bar chart format for each player on the Progress page", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel14.pack()
        
        RulesLabel21=customtkinter.CTkLabel(self.__Frame, text="\n 2.The Categories", font=('Berlin Sans FB Demi',20))
        RulesLabel21.pack()
        RulesLabel22=customtkinter.CTkLabel(self.__Frame, text="\n - SpellSkill- How good the character is at casting spells (Speed/Strength of spell)", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel22.pack()
        RulesLabel23=customtkinter.CTkLabel(self.__Frame, text="\n - Bravery - How ready a character is to be in a dangerous situation (for selfish/selfless reasons)", 
        font=('Berlin Sans FB Demi',15))
        RulesLabel23.pack()
        RulesLabel24=customtkinter.CTkLabel(self.__Frame, text="\n - BroomSkill- How comfortable/ talented a character is on a broom", 
                                            font=('Berlin Sans FB Demi',15))
        RulesLabel24.pack()
        RulesLabel26=customtkinter.CTkLabel(self.__Frame, text="\n - Kindness - How kind a character is to others (selflessness)", font=('Berlin Sans FB Demi',15))
        RulesLabel26.pack()

        RulesLabel25=customtkinter.CTkLabel(self.__Frame, text="\n - Strength - A measure of a character's physical and mental strength", font=('Berlin Sans FB Demi',15))
        RulesLabel25.pack()

        RulesLabel27=customtkinter.CTkLabel(self.__Frame, text="\n - TopTrumpsRating - A character's overall importance to the story", font=('Berlin Sans FB Demi',15))
        RulesLabel27.pack()

        RulesLabel15=customtkinter.CTkLabel(self.__Frame, text="\n -Have fun playing the game, and don't let the muggles get you down!", font=('Berlin Sans FB Demi',20))
        RulesLabel15.pack()
        #Creates a window using the frame#
        self.__canvas.create_window((0,0),window=self.__Frame, anchor='nw', width=1700, height=1500)
        #Allows the user to scroll using their mouse#
        self.__canvas.bind_all('<MouseWheel>', lambda event:self.__canvas.yview_scroll(-int(event.delta/60), "units"))