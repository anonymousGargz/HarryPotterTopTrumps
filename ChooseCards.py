#Creates an object containing a deck of cards for each player and encapsulates the methods needed to 
#act on it#
from customtkinter import *
import random
import sqlite3

#Creates a connection object to connect to the the database#
tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()
#cur.execute("""DROP TABLE CardsInPlay""")
cur.execute("""CREATE TABLE IF NOT EXISTS CardsInPlay (
            ReleasedOrder INTEGER NOT NULL PRIMARY KEY,
            CardID INTEGER NOT NULL
)""")
#CREATES THE topTrumpsDeck table
cur.execute("""CREATE TABLE IF NOT EXISTS topTrumpsDeck (
            CardID INTEGER NOT NULL PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            SpellSkill INTEGER NOT NULL,
            Bravery INTEGER NOT NULL,
            BroomSkill INTEGER NOT NULL,
            Kindness INTEGER NOT NULL,
            Strength INTEGER NOT NULL,
            TopTrumpsRating INTEGER NOT NULL
)""")
#Inserts the values for the character card into it#
#Values=[(1, 'Harry', 'Potter', 80,98,90,81,90,100),(2,'Albus','Dumbledore', 100,75,60,70,96,98),
#(3,'Ron', 'Weasley',72,92,88,68,69,90),(4,'Hermione', 'Granger',83,91,44,90,72,92),
         #(5,'Sirius', 'Black',86,95,78,75,89,86),(6,'Remus', 'Lupin',85,85,71,55,83,88),
#(7,'Peter', 'Pettigrew',59,34,40,25,41,24),
         #(8,'Arthur', 'Weasley', 74,79,61,80,63,75),(9,'Draco', 'Malfoy',75,85,82,40,71,69),
#(10,'Bellatrix', 'Lestrange',88,94,30,10,84,79), (11, 'Lord', 'Voldemort',99,50,20,0,100,99)]
#Values2=[(12,'Serverus','Snape',90,100,25,40,85,95),(13,'Neville','Longbottom',60,80,22,84,62,71),
#(14,'Horace','Slughorn',77,55,37,58,69,64),
#(15,'Minerva','McGonagall',87,79,65,88,75,80), (16,'Ginny','Weasley',70,87,87,78,67,85),
#(17,'Parvati','Patil',58,62,49,73,55,51),(18,'Vincent','Crabbe',44,18,70,29,49,43),
        #(19,'Nymphadora','Tonks',82,81,73,77,76,78),(20,'Rubeus','Hagrid',26,82,15,96,60,84)]
#Values3=[(21,'Viktor','Krum',68,69,100,56,73,60),(22,'Cho','Chang',56,57,53,60,57,55),
#(23,'Argus','Filch',1,11,5,21,20,22),
        #(24,'Fleur','Delacour',65,70,68,76,59,67), (25,'Lucius','Malfoy',79,38,69,33,74,74),
#(26,'Cedric','Diggory',69,86,80,72,78,82),(27,'Sybill','Trelawney',61,48,28,54,56,53),
        #(28,'Gilderoy','Lockhart',30,37,50,23,50,45),(29,'Quirinus','Quirrel',50,61,19,20,54,42),
#(30,'Luna','Lovegood',69,83,39,94,70,87),(31,'Colin','Creevey',48,60,33,63,47,65),
        #(32,'Fenrir','Greyback',82,22,21,6,86,57),(33,'Fred','Weasley',67,87,93,70,81,81), 
#(34,'Dobby','Elf',97,98,1,92,32,91),(35,'Molly','Weasley',89,88,41,91,79,79),
        #(36,'Narcissa','Malfoy',76,52,29,30,61,48),(37,'Seamus','Finnigan',54,66,62,59,58,61),
#(38,'Dolores','Umbridge',57,40,10,8,32,30), (39,'Alastor','Moody',92,93,71,50,92,89),
#(40,'Newt','Scammander',84,94,36,100,77,96),(41,'Gellert','Grindelwald',98,78,57,17,95,97),
#(42,'Jacob','Kowalski',0,73,0,89,24,35), (43,'Tina','Goldstein',78,72,34,66,80,76),
        #(48,'Leta','Lestrange',79,84,45,65,82,58),(49,'Picket','Scammander',2,16,2,44,10,22)]
#Values=[(44,'Queenie', 'Goldstein', 81, 68, 24, 85, 68, 66), 
#(45, 'Credence', 'Barebone', 54, 22, 11, 19, 53, 49),
        #(47, 'Theseus', 'Scammander', 66, 53, 77, 67, 66, 59), 
#(46, 'Aberforth', 'Dumbledore', 61, 74, 42, 64, 54, 63)]
#cur.executemany("""INSERT INTO topTrumpsDeck VALUES(?,?,?,?,?,?,?,?,?)""", Values)

#INSERTS 10 CARDS INTO CARDSINPLAY INITIALLY
#Values=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]
#cur.executemany("""INSERT INTO CardsInPlay VALUES (?,?)""", Values)


#Selects the ReleasedOrder from the CardsInPlay table#
cur.execute("""SELECT ReleasedOrder FROM CardsInPlay""")
MaxCard=cur.fetchall()
LastCard=MaxCard[len(MaxCard)-1]
#Selects the value of the ReleasedID of the most recent card that's been released#
LastValue=LastCard[0]

#Creates a list of random integers that can be used to select the CardIDs for a list of random cards#
randomCardsList=[]
while (len(randomCardsList)<LastValue):
    randomNumber=random.randint(1,LastValue)
    if randomNumber not in randomCardsList:
        randomCardsList.append(randomNumber)
Half=len(randomCardsList)//2

#CREATES A DECK OF CARDS FOR EACH PLAYER BY SELECTING ALL THE RELEASED CARDS, SPLITTING THE RANDOM CARD 
#IDs GENERATED IN HALF, 
#AND THEN USING THESE CARD IDs TO CREATE A STACK OF CHARACTER CARDS FROM THE RELEASED CARDS#
class Card():
    def __init__(self):
        self.randomCardValues=[]
        self.LastCard=0
        self.randomCardsList=[]
        self.cardStack=[]
        self.pointsStack=[]

        self.SetRandomCardValues()
        self.AddCardsToStack()
    
    #Splits random CardIDs list in half#
    def SetRandomCardValues(self):
        for i in range(0, len(randomCardsList)//2):
            self.randomCardValues.append(randomCardsList[i])
    
    #Adds cards to card stack using random CardIDs#
    def AddCardsToStack(self):
        for i in range (0,len(self.randomCardValues)):
            CurrentCardIndex=self.randomCardValues[i]
            cur.execute("""SELECT * FROM topTrumpsDeck INNER JOIN CardsInPlay ON 
                        topTrumpsDeck.CardID=CardsInPlay.CardID WHERE topTrumpsDeck.CardID=(?) """,
                          (CurrentCardIndex,))
            results=cur.fetchall()
            self.cardStack.append(results[0])
            tableConnection.commit()
    
    #Removes top card from the stack#
    def RemoveCards(self):
        self.cardStack.pop(0)

    #Adds points to each player's card stack#
    def AddPoints(self, Result):
        if Result=='Win':
            self.pointsStack.append(3)
        else:
            self.pointsStack.append(1)
        print(self.pointsStack)

class Player1Cards(Card): #Inheritance from Card#
    def __init__(self):
     super().__init__()
    
    
class Player2Cards(Card):
    def __init__(self):
     super().__init__()
    
    def SetRandomCardValues(self): #Polymorphism; takes second half of randomly generated CardIDs, 
                                    #rather than the first#
        for i in range((len(randomCardsList)//2), (len(randomCardsList)//2)+Half ):
            self.randomCardValues.append(randomCardsList[i])



