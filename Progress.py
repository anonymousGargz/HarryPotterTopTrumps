#ADDING UP POINTS IN THE DATABASE FOR THE LAST 5 DAYS FUNCTIONALITY TO BE USED FOR THE PROGRESS PAGE#

import sqlite3
import datetime
from datetime import date
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()

#Gets today's date#
today=date.today()

#Returns the number of points won for the current day using a user-defined aggregate SQL function#
class CheckNumberOfWinsToday():
    def __init__(self):
        self.GameCount=0
        self.PointCount=0
        self.date=date.today().strftime("%d/%m/%Y")
    
    def step(self,date,gamePoints, quizPoints):
        if date==self.date:
            if gamePoints==3:
                self.GameCount+=1
            if quizPoints==3:
                self.PointCount+=1
    
    def finalize(self):
        return self.GameCount + self.PointCount

#Creates the aggregate function#
tableConnection.create_aggregate('checkWins',3,CheckNumberOfWinsToday)

#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer1 """)
Player1WinsToday=cur.fetchall()

try:
    for i in range(0,2):
        Player1WinsToday=Player1WinsToday[0]
except:
    Player1WinsToday=0

#Executes the aggregate function and returns the number of points won for Player2#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer2 """)
Player2WinsToday=cur.fetchall()

try:
    for i in range(0,2):
        Player2WinsToday=Player2WinsToday[0]
except:
    Player2WinsToday=0



#Works out yesterday's date#
DaysToTakeAway=datetime.timedelta(days=1)
Yesterday=today-DaysToTakeAway
Yesterday=Yesterday.strftime("%d/%m/%Y")


#Returns the number of points won from yesterday using a user-defined aggregate SQL function#
class CheckNumberOfWinsYesterday():
    def __init__(self):
        self.GameCount=0
        self.PointCount=0
        self.date=Yesterday
    
    def step(self,date,gamePoints, quizPoints):
        if date==self.date:
            if gamePoints==3:
                self.GameCount+=1
            if quizPoints==3:
                self.PointCount+=1
    
    def finalize(self):
        return self.GameCount + self.PointCount

#Creates the aggregate function#
tableConnection.create_aggregate('checkWins',3,CheckNumberOfWinsYesterday)

#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer1 """)
Player1WinsYesterday=cur.fetchall()
try:
    for i in range(0,2):
        Player1WinsYesterday=Player1WinsYesterday[0]
except:
    Player1WinsYesterday=0

#Executes the aggregate function and returns the number of points won for Player2#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer2 """)
Player2WinsYesterday=cur.fetchall()
try:
    for i in range(0,2):
        Player2WinsYesterday=Player2WinsYesterday[0]
except:
    Player2WinsYesterday=0



#Work's out the date from 2 days ago#
DaysToTakeAway=datetime.timedelta(days=2)
DayBefore1=today-DaysToTakeAway
DayBefore1=DayBefore1.strftime("%d/%m/%Y")


#Returns the number of points won from the day before yesterday using a user-defined aggregate 
#SQL function#
class CheckNumberOfWinsDayBefore1():
    def __init__(self):
        self.GameCount=0
        self.PointCount=0
        self.date=DayBefore1
    
    def step(self,date,gamePoints, quizPoints):
        if date==self.date:
            if gamePoints==3:
                self.GameCount+=1
            if quizPoints==3:
                self.PointCount+=1
    
    def finalize(self):
        return self.GameCount + self.PointCount

#creates aggregate function#
tableConnection.create_aggregate('checkWins',3,CheckNumberOfWinsDayBefore1)

#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer1 """)
Player1WinsDayBefore1=cur.fetchall()
try:
    for i in range(0,2):
        Player1WinsDayBefore1=Player1WinsDayBefore1[0]
except:
    Player1WinsDayBefore1=0

#Executes the aggregate function and returns the number of points won for Player2#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer2 """)
Player2WinsDayBefore1=cur.fetchall()

try:
    for i in range(0,2):
        Player2WinsDayBefore1=Player2WinsDayBefore1[0]
except:
    Player2WinsDayBefore1=0


#Works out the date from 3 days ago#
DaysToTakeAway=datetime.timedelta(days=3)
DayBefore2=today-DaysToTakeAway
DayBefore2=DayBefore2.strftime("%d/%m/%Y")

#Returns the number of points won from 3 days ago using a user-defined aggregate SQL function#
class CheckNumberOfWinsDayBefore2():
    def __init__(self):
        self.GameCount=0
        self.PointCount=0
        self.date=DayBefore2
    
    def step(self,date,gamePoints, quizPoints):
        if date==self.date:
            if gamePoints==3:
                self.GameCount+=1
            if quizPoints==3:
                self.PointCount+=1
    
    def finalize(self):
        return self.GameCount + self.PointCount

#Creates the aggregate function#
tableConnection.create_aggregate('checkWins',3,CheckNumberOfWinsDayBefore2)


#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer1 """)
Player1WinsDayBefore2=cur.fetchall()
try:
    for i in range(0,2):
        Player1WinsDayBefore2=Player1WinsDayBefore2[0]
except:
    Player1WinsDayBefore2=0

#Executes the aggregate function and returns the number of points won for Player2#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer2 """)
Player2WinsDayBefore2=cur.fetchall()
try:
    for i in range(0,2):
        Player2WinsDayBefore2=Player2WinsDayBefore2[0]
except:
    Player1WinsDayBefore2=0



#Works out the date from 4 days ago#
DaysToTakeAway=datetime.timedelta(days=4)
DayBefore3=today-DaysToTakeAway
DayBefore3=DayBefore3.strftime("%d/%m/%Y")

#Returns the number of points won from 4 days ago using a user-defined aggregate SQL function#
class CheckNumberOfWinsDayBefore3():
    def __init__(self):
        self.GameCount=0
        self.PointCount=0
        self.date=DayBefore3
    
    def step(self,date,gamePoints, quizPoints):
        if date==self.date:
            if gamePoints==3:
                self.GameCount+=1
            if quizPoints==3:
                self.PointCount+=1
    
    def finalize(self):
        return self.GameCount + self.PointCount

#Creates the aggregate function#
tableConnection.create_aggregate('checkWins',3,CheckNumberOfWinsDayBefore3)

#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer1 """)
Player1WinsDayBefore3=cur.fetchall()
try:
    for i in range(0,2):
        Player1WinsDayBefore3=Player1WinsDayBefore3[0]
except:
    Player1WinsDayBefore3=0

#Executes the aggregate function and returns the number of points won for Player1#
cur.execute("""SELECT checkWins(Date,GamePoints, QuizPoints) FROM RunningTotalWinsPlayer2 """)
Player2WinsDayBefore3=cur.fetchall()
try:
    for i in range(0,2):
        Player2WinsDayBefore3=Player2WinsDayBefore3[0]
except:
    Player2WinsDayBefore3=0


#Creates a list of the total player points each day for the last 5 days#

Player1=(Player1WinsDayBefore3,Player1WinsDayBefore2, Player1WinsDayBefore1, 
         Player1WinsYesterday,Player1WinsToday)
Player2=(Player2WinsDayBefore3,Player2WinsDayBefore2, Player2WinsDayBefore1, 
         Player2WinsYesterday,Player2WinsToday)


#FReturns the number of points for each player#
class PlayerPoints():
    def __init__(self):
        pass

    def ReturnPlayer1Points(self):
        return Player1

    def ReturnPlayer2Points(self):
        return Player2
