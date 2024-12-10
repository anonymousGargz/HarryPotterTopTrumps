from tkinter import ttk
import customtkinter 
from customtkinter import *
from PIL import ImageTk, Image
from Deck import CardInDeck

#Displays the elements on the DeckPage, inherits from gameInterface frame mainArea#
class DeckPage(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color='#93cf9c')
        
        #Displays background image#
        imgBackground=Image.open('Slytherin_common_room_HL.webp')
        resized=imgBackground.resize((2250,1500))
        backgroundImage=ImageTk.PhotoImage(resized)
        
        self.__imageBackground=customtkinter.CTkLabel(self, image=backgroundImage)
        self.__imageBackground.place(relx=0,rely=0,relheight=1,relwidth=1)
       
        #Displays title#
        self.__title=customtkinter.CTkLabel(self, text='Deck Page', font=('Berlin Sans FB Demi',40))
        self.__title.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

        #Creates a 'Style' class object that allows you to style ttk widgets#
        style=ttk.Style()
        style.configure("Treeview",background='#afedd3', foreground='#02243d', rowheight=50, 
                        font=('Berlin Sans FB Demi',15))
        style.configure("Treeview.Heading", background='#93cf9c', font=('Berlin Sans FB Demi',18))
        
        #Creates a table with different column headings using the Treeview module#
        self.__CardsTable=ttk.Treeview(self, columns=('CardID','FirstName', 'LastName', 'SpellSkill', 
                                                      'Bravery', 'BroomSkill', 
                                               'Kindness', 'Strength', 'TopTrumpsRating', 'Unlocked'), 
                                               show='headings', cursor='arrow')
        
        #Formats the headings of the table#
        self.__CardsTable.heading('CardID', text='CardID')
        self.__CardsTable.heading('FirstName', text='First Name')
        self.__CardsTable.heading('LastName', text='Last Name')
        self.__CardsTable.heading('SpellSkill', text='Spell Skill')
        self.__CardsTable.heading('Bravery', text='Bravery')
        self.__CardsTable.heading('BroomSkill', text='Broom Skill')
        self.__CardsTable.heading('Kindness', text='Kindness')
        self.__CardsTable.heading('Strength', text='Strength')
        self.__CardsTable.heading('TopTrumpsRating', text='Top Trumps Rating')
        self.__CardsTable.heading('Unlocked', text='Unlocked')

        #Formats the columns of the table#
        self.__CardsTable.column('CardID',anchor=CENTER, width=50)
        self.__CardsTable.column('FirstName',anchor=CENTER, width=100)
        self.__CardsTable.column('LastName',anchor=CENTER, width=100)
        self.__CardsTable.column('SpellSkill',anchor=CENTER, width=50)
        self.__CardsTable.column('Bravery',anchor=CENTER, width=50)
        self.__CardsTable.column('BroomSkill',anchor=CENTER, width=50)
        self.__CardsTable.column('Kindness',anchor=CENTER, width=50)
        self.__CardsTable.column('Strength',anchor=CENTER, width=50)
        self.__CardsTable.column('TopTrumpsRating',anchor=CENTER, width=50)
        self.__CardsTable.column('Unlocked',anchor=CENTER, width=50)
        
        self.__CardsTable.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)
        #Gets the sorted cards#
        Results=CardInDeck.__ReturnSortedCards__()
        #Sets the values of each individual card to different attributes, then inserts them into 
        #each row of the table#
        try:
            for i in range (len(Results)):
                CardID=Results[i][0]
                FirstName=Results[i][1]
                LastName=Results[i][2]
                SpellSkill=Results[i][3]
                Bravery=Results[i][4]
                BroomSkill=Results[i][5]
                Kindness=Results[i][6]
                Strength=Results[i][7]
                TopTrumpsRating=Results[i][8]
                Unlocked=Results[i][9]
                Attributes=(CardID,FirstName,LastName,SpellSkill,Bravery,BroomSkill,Kindness,Strength,
                            TopTrumpsRating,Unlocked)
                self.__CardsTable.insert(parent='', index='end', values=Attributes)
        except:
            print("Cannot fetch cards")
            
