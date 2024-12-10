#AGGREGATE SQL FUNCTIONS#
import sqlite3
import subprocess

#Creates a connection object to connect to the database, and a cursor to navigate it#
tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()

#checks the number of wins by counting the number of 3s in all the tables of each database 
#using aggregate user-defined sql functions#
class CheckNumberOfWins():
    def __init__(self):
        self.count=0
    
    def step(self,points):
        if points==3:
            self.count+=1
    
    def finalize(self):
        return self.count

#Creates the aggregate function#
tableConnection.create_aggregate('checkWins',1,CheckNumberOfWins)

#Applies the aggregate function and fetches the number of wins total#
cur.execute("""SELECT checkWins(Points) FROM RecordWinsPlayer1""")
Player1TotalWins=cur.fetchall()
for i in range(0,2):
    Player1TotalWins=Player1TotalWins[0]

#Adds a new card into the CardsInPlay database if the user has more than 20 wins and clears the databse#
if Player1TotalWins//20>0:
    cur.execute("""SELECT ReleasedOrder FROM CardsInPlay""")
    #Finds the CardID of the last card in the CardsInPlay table#
    MaxCard=cur.fetchall()
    LastCard=MaxCard[len(MaxCard)-1]
    LastValue=LastCard[0]
    LastValue+=1
    #Adds card with CardID 1 greater than the last value currently in the table#
    Values=[LastValue,LastValue]
    cur.execute("""INSERT INTO CardsInPlay VALUES (?,?)""", Values)
    tableConnection.commit()

    cur.execute("""DELETE FROM RecordWinsPlayer1""")
    tableConnection.commit()

#opens the quiz if the user has more than 10 wins#
elif Player1TotalWins//15>0:
    subprocess.run(["python", "QuizWindow.py"])

