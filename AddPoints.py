#Adds points to each player's tables in the database#
import sqlite3
from datetime import date

#Creates a connection object to connect to the database, and creates a cursor to navigate a database#
tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()

#CREATES THE RECORDWINSPLAYER1, RUNNINGTOTALPOINTSPLAYER1, AND RUNNINGTOTALPOINTSPLAYER2 TABLES#

#cur.execute("""CREATE TABLE RecordWinsPlayer1(
            #EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
            #Date integer,
            #Points integer
#)""")

#cur.execute("""CREATE TABLE RunningTotalWinsPlayer1 (
            #PointsWonID INTEGER PRIMARY KEY AUTOINCREMENT,
            #Date integer,
            #GamePoints integer,
            #QuizPoints integer
#)""")


#cur.execute("""CREATE TABLE RunningTotalWinsPlayer2 (
            #PointsWonID INTEGER PRIMARY KEY AUTOINCREMENT,
            #Date integer,
            #GamePoints integer,
            #QuizPoints integer
#)""")




#Adds points to the RecordPlayer1Wins table, with today's date as the date column entry#
class AddPointsPlayer1():
    def __init__():
        pass
    def __AddPoints__(Player1):
        Date=date.today()
        TodaysDate = Date.strftime("%d/%m/%Y")
        Values=[TodaysDate, Player1]
        cur.execute("""INSERT INTO RecordWinsPlayer1(Date,Points) VALUES(?,?)""", Values)
        tableConnection.commit()
        
#Add points to the RunningTotalWinsPlayer1 table, with today's date as the date column entry#
class AddRunningTotalPointsPlayer1():
    def __init__():
        pass
    def __AddPoints__(Player1):
        Date=date.today()
        TodaysDate = Date.strftime("%d/%m/%Y")
        Values=[TodaysDate,Player1]
        cur.execute("""INSERT INTO RunningTotalWinsPlayer1(Date,GamePoints) VALUES(?,?)""",Values)
        tableConnection.commit()
        

#Add points to the RunningTotalWinsPlayer2 table, with today's date as the date column entry#
class AddRunningTotalPointsPlayer2():
    def __init__():
        pass
    def __AddPoints__(Player2):
        Date=date.today()
        TodaysDate = Date.strftime("%d/%m/%Y")
        Values=[TodaysDate,Player2]
        cur.execute("""INSERT INTO RunningTotalWinsPlayer2(Date,GamePoints) VALUES(?,?)""",Values)
        tableConnection.commit()
        


