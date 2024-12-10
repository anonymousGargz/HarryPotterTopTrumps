from customtkinter import *
from time import *
import threading
import subprocess
import keyboard

# Imports the relevant classes from other files in the game#
from ChooseCards import Player1Cards, Player2Cards
from GameInterface import *
from AddPoints import AddPointsPlayer1, AddRunningTotalPointsPlayer1, AddRunningTotalPointsPlayer2
from SetCardValues import SetPlayer1CardValues, SetPlayer2CardValues
from GetCardValues import ReturnPlayer1Values, ReturnPlayer2Values
from DecideWinner import DecideWinner


#Creates an object of the class Player1Cards and Player2Cards, creating a deck of cards for each player#
Player1Card=Player1Cards()
Player2Card=Player2Cards()
InitialNumberOfCards=len(Player1Card.cardStack)


#This class handles all the threads in the game/ when to stop and start the threads#
class ThreadingElements():
    def __init__(self):
        pass
    
    #Sets up the game for Player 1's turn#
    def __Player1Turn__(self):
        #Starts Player 1's countdown timer#
        self.CountdownTimerThreadPlayer1=threading.Thread(target=Player1Timer.__UpdatePlayer1Timer__, 
                                                          args=(self,))
        self.CountdownTimerThreadPlayer1.start()
        #Calls methods of the SetPlayer1/2CardValues class#
        try:
            SetPlayer1CardValues.__GetCardValues__(self, Player1Card)
            SetPlayer2CardValues.__GetCardValues__(self, Player2Card)
        except:
            print("No cards left in deck")

        SetPlayer1CardValues.__RevealPlayer1Card__(self)
        SetPlayer2CardValues.__HidePlayer2Card__(self)

        #Disables the PlayAgain/Shuffle buttons so they can't be accessed until the game is over#
        self.AmendPlayGameButton('disabled')
        self.UpdateShuffleButton('SHUFFLE')
        self.AmendShuffleButton('disabled')

    #Sets up the game for Player 2's turn#
    def __Player2Turn__(self):
        #Starts the countdown timer for Player 2#
        self.CountdownTimerThreadPlayer2=threading.Thread(target=Player2Timer.__UpdatePlayer2Timer__, 
                                                          args=(self,))
        self.CountdownTimerThreadPlayer2.start()
        
        try:
            SetPlayer1CardValues.__GetCardValues__(self, Player1Card)
            SetPlayer2CardValues.__GetCardValues__(self, Player2Card)
        except:
            print("No cards left in deck")

        SetPlayer2CardValues.__RevealPlayer2Card__(self)
        SetPlayer1CardValues.__HidePlayer1Card__(self)
    

   # This restarts Player 1's timer by creating a new tumer thread after it has been paused, 
        #with TimerValue being the number it was paused at# 
    def __Player1RestartTimer__(self, TimerValue):
        CountdownTimerThreadPlayer1=threading.Thread(target=Player1Timer.__ReStartTimerPlayer1__, 
                                                     args=(self,TimerValue,))
        CountdownTimerThreadPlayer1.start()
    
    # This restarts Player 2's timer by creating a new tumer thread after it has been paused, with 
        #TimerValue being the number it was paused at#
    def __Player2RestartTimer__(self, TimerValue):
        CountdownTimerThreadPlayer2=threading.Thread(target=Player2Timer.__ReStartTimerPlayer2__, 
                                                     args=(self,TimerValue,))
        CountdownTimerThreadPlayer2.start()
    
    #This starts a thread that displays the winner of each round on a frame on the PlayPage#
    def __StartWinnerBannerThread__(self):
        self.__WinnerBannerThread=threading.Thread(target=WorkOutWinner.__DisplayWinnerBanner__, 
                                                   args=(self,))
        self.__WinnerBannerThread.start()
       
class CreateNewObjects():
    def __init__(self):
        pass
    #This creates a new object of the class Player1Cards/Player2Cards each time the player 
    #restarts the game#
    def CreateNewObjects(self):
        global Player1Card
        Player1Card=Player1Cards()
        global Player2Card
        Player2Card=Player2Cards()
        global InitialNumberOfCards
        InitialNumberOfCards=len(Player1Card.cardStack)

        self.UpdateShuffleButton('SHUFFLED')

class PauseTimer():
    def __init__(self):
        self.sleepCounter=0

    #This method works out whose turn the game is being paused on by checking which of the 
        #countdownTimer threads are running#
    def __DecideWhoseTurn__(self):
        try: #Prevents user from trying to pause the game before it's started#
            if self.CountdownTimerThreadPlayer1.is_alive():
                Player1Timer.__PauseTimerPlayer1__(self)
                Timer='Player1'
                TimerValue=int(self.ReturnTimerPlayer1())
            
            else:
                Player2Timer.__PauseTimerPlayer2__(self)
                Timer='Player2'
                TimerValue=int(self.ReturnTimerPlayer2())
            
            #This calls the method PauseThread#
            PauseTimer.__PauseThread__(self,Timer, TimerValue)
        except:
            print("Timer not started yet")

    #This creates a thread to execute the 'Pause' functionality of the game#
    def __PauseThread__(self, Timer, TimerValue):
        PauseThread=threading.Thread(target=PauseTimer.Pause,args=(self, Timer, TimerValue))
        PauseThread.start()
    
    
    # This calls the recursive function CheckSpacePressed until 'paused' returns as false#
    def Pause(self, Timer, TimerValue):
        paused=True
        while paused:   
            paused=PauseTimer.CheckSpacePressed(self, 10)
        try:
            PauseTimer.__Restart__(self, Timer,TimerValue)
        except:
            print("Invalid TimerValue")
            raise AttributeError
    
#This pauses the game for another second until the user presses the space bar or 10 seconds have elapsed and calls itself recursively#
    def CheckSpacePressed(self, count):
        while not keyboard.is_pressed('space'):
            if count<0:
                return False
            sleep(1)
            return PauseTimer.CheckSpacePressed(self, count-1)
        return False
    
    #Once paused is set to false again, this calls the methods the restart the game for the appropriate 
    #player#
    def __Restart__(self, Timer, TimerValue):
        if Timer=='Player1':
            ThreadingElements.__Player1RestartTimer__(self, TimerValue)
            Player1Timer.__UnPauseTimerPlayer1__(self)
        else:
            ThreadingElements.__Player2RestartTimer__(self, TimerValue)
            Player2Timer.__UnPauseTimerPlayer2__(self)

#This inherits from ThreadingElements and encompasses the methods that act on Player1's timer#
class Player1Timer(ThreadingElements):
    def __init__():
        super().__init__()

#While the user hasn't picked a choice/15 seconds aren't up, the method updates the countdown 
#icon with the new number#    
    def __UpdatePlayer1Timer__(self):
        self.SetKillTimerPlayer1(False)
        self.ConfigureCountdownTimerIconPlayer1('15')
        countdownTimer=15
        for i in range(15):
            countdownTimer-=1
            self.ConfigureCountdownTimerIconPlayer1(str(countdownTimer))
            sleep(1)
            if self.GetKillPlayer1()==True or self.GetPausePlayer1()==True:
                break
            elif i==14:
                WorkOutWinner.__DecideWinnerOnPlayer1Turn__(self,0,1)

    #Sets the PauseTimer attribute to true to pause the game#
    def __PauseTimerPlayer1__(self):
        self.SetPauseTimerPlayer1(True)
    
    #Sets the PauseTimer attribute to false to unpause the game#
    def __UnPauseTimerPlayer1__(self):
        self.SetPauseTimerPlayer1(False)

    #This restarts the Player1 timer on the value that they paused it at and displays the updated values on the countdownTimerIcon#
    def __ReStartTimerPlayer1__(self, CurrentTime):
        self.SetKillTimerPlayer1(False)
        
        self.ConfigureCountdownTimerIconPlayer1(str(CurrentTime))
        InitialTime=CurrentTime
        countdownTimer=CurrentTime
        try:
            for i in range(countdownTimer):
                countdownTimer-=1
                self.ConfigureCountdownTimerIconPlayer1(str(countdownTimer))
                sleep(1)
                if self.GetKillPlayer1()==True or self.GetPausePlayer1()==True:
                    break
                elif i==InitialTime-1:
                    WorkOutWinner.__DecideWinnerOnPlayer1Turn__(self,0,1)
        except:
            print("Invalid value for countdownTimer")
            self.SetKillTimerPlayer1("True")
            WorkOutWinner.__DecideWinnerOnPlayer1Turn__(self,0,1)

        
#This class gets the values returned by the ReturnPlayer1Values class, stops the countdown timer, 
#and calls the decideWinner method from another class#
class GetPlayer1Values():
    def __init__(self):
        pass
    def __GetValueChosenByPlayer1__(self, valueChosen):
        Values=ReturnPlayer1Values.__GetValueChosenByPlayer1__(self, valueChosen)
        GetPlayer1Values.StopCountdownTimer(self)
        GetPlayer1Values.CallDecideWinner(self, Values[0], Values[1])
       


    def StopCountdownTimer(self):
        self.SetKillTimerPlayer1(True)
        
    
    def CallDecideWinner(self, Player1ValueForRound, Player2ValueForRound):
        #This calls the DecideWinner and AddPointsToTable methods using the Player1/2 values for the 
        #round as arguments#
        try:
            WorkOutWinner.__DecideWinnerOnPlayer1Turn__(self, Player1ValueForRound, Player2ValueForRound)
            WorkOutWinner.__AddPointsToTable__(Player1ValueForRound,Player2ValueForRound)
        except:
            print("Invalid values for Player1/Player2 round")
            WorkOutWinner.__DecideWinnerOnPlayer1Turn__(self, 1, 0)
            WorkOutWinner.__AddPointsToTable__(1,0)


#This class gets the values returned by the ReturnPlayer2Values class, stops the countdown timer, 
#and calls the decideWinner method from another class#
class GetPlayer2Values():
    def __init__(self):
        pass

    def __GetValueChosenByPlayer2__(self, valueChosen):
        Values=ReturnPlayer2Values.__GetValueChosenByPlayer2__(self, valueChosen)
        GetPlayer2Values.CallDecideWinner(self, Values[0], Values[1])
        GetPlayer2Values.StopCountdownTimer(self)


    def StopCountdownTimer(self):
        self.SetKillTimerPlayer2(True)
    
    def CallDecideWinner(self, Player1ValueForRound, Player2ValueForRound):
        #This calls the DecideWinner and AddPointsToTable methods using the Player1/2 values for the 
        #round as arguments#
        try:
            WorkOutWinner.__DecideWinnerOnPlayer2Turn__(self, Player1ValueForRound, Player2ValueForRound)
            WorkOutWinner.__AddPointsToTable__(Player1ValueForRound,Player2ValueForRound)
        except:
            print("Invalid values for Player1/Player2 round")
            WorkOutWinner.__DecideWinnerOnPlayer2Turn__(self, 0, 1)
            WorkOutWinner.__AddPointsToTable__(0,1)


#This inherits from ThreadingElements and encompasses the methods that act on Player2's timer#    
class Player2Timer(ThreadingElements):
    def __init__():
        super().__init__()

#While the user hasn't picked a choice/15 seconds aren't up, the method updates the countdown icon with 
#the new number#       
    def __UpdatePlayer2Timer__(self):
        self.SetKillTimerPlayer2(False)
        self.ConfigureCountdownTimerIconPlayer2('15')
        countdownTimer=15
        for i in range(15):
            countdownTimer-=1
            self.ConfigureCountdownTimerIconPlayer2(str(countdownTimer))
            sleep(1)
            if self.GetKillPlayer2()==True or self.GetPausePlayer2()==True:
                break

            elif i==14:
                WorkOutWinner.__DecideWinnerOnPlayer2Turn__(self,1,0)
    
    #sets the PauseTimerPlayer2 attribute to true when called#
    def __PauseTimerPlayer2__(self):
        self.SetPauseTimerPlayer2(True)
    
    #sets the PauseTimerPlayer2 attribute to false when called#
    def __UnPauseTimerPlayer2__(self):
        self.SetPauseTimerPlayer2(False)

#This restarts the Player2 timer on the value that they paused it at and displays the updated values on 
        #the countdownTimerIcon#
    def __ReStartTimerPlayer2__(self,CurrentTime):
        self.SetPauseTimerPlayer2(False)
        self.SetKillTimerPlayer2(False)
        
        try:
            self.ConfigureCountdownTimerIconPlayer2(str(CurrentTime))
            InitialTime=CurrentTime
            countdownTimer=CurrentTime
            for i in range(countdownTimer):
                countdownTimer-=1
                self.ConfigureCountdownTimerIconPlayer2(str(countdownTimer))
                sleep(1)
                if self.GetKillPlayer2()==True or self.GetPausePlayer2()==True:
                    break
                elif i==InitialTime-1:
                    WorkOutWinner.__DecideWinnerOnPlayer2Turn__(self,1,0)
        except:
            self.SetKillTimerPlayer2(True)
            print("Invalid value for countdownTimer")
            WorkOutWinner.__DecideWinnerOnPlayer2Turn__(self,1,0)


#This class works out the winner for each round/game and determines if the game is over, 
            #whilst adding points to each players' stack#
class WorkOutWinner():
    def __init__():
        pass

#This displays the winner banner for 2 seconds after each round#   
    def __DisplayWinnerBanner__(self):
        self.DisplayWinnerBanner()
        sleep(2)
        self.ForgetWinnerBanner()

#This takes both Player1/2's scores for the round as arguments and determines the winner of the 
        #round on Player 1's turn#   
    def __DecideWinnerOnPlayer1Turn__(self, Player1, Player2):
        print(Player1, Player2)
        ThreadingElements.__StartWinnerBannerThread__(self)
        DecideWinner.__DecideWinner__(self, Player1, Player2, Player1Card, Player2Card)
        

        #If all the cards have been played in the game, DecideGameWinner is called#
        if DecideWinner.__CheckGameOver__(self, InitialNumberOfCards, Player1Card):
            Winner= DecideWinner.__DecideGameWinner__(self, Player1Card, Player2Card)
            WorkOutWinner.__DecideGameWinner__(self, Winner)
        
        #Else, the method Player2Turn is called#
        
        else:
            ThreadingElements.__Player2Turn__(self)

#This takes both Player1/2's scores for the round as arguments and determines the winner of the round 
            #on Player 2's turn#   
    def __DecideWinnerOnPlayer2Turn__(self, Player1, Player2):
        ThreadingElements.__StartWinnerBannerThread__(self)
        DecideWinner.__DecideWinner__(self, Player1, Player2, Player1Card, Player2Card)

        #If all the cards have been played in the game, DecideGameWinner is called#
        if DecideWinner.__CheckGameOver__(self, InitialNumberOfCards, Player1Card):
            print(Player1Card.pointsStack)
            print(Player2Card.pointsStack)
            Winner= DecideWinner.__DecideGameWinner__(self, Player1Card, Player2Card)
            WorkOutWinner.__DecideGameWinner__(self, Winner)

        #Else, the method Player1Turn is called#
        else:
            ThreadingElements.__Player1Turn__(self)
    

#This method displays the winner of the game depending on the value of the 'Winner' argument#       
    def __DecideGameWinner__(self, Winner):
        ThreadingElements.__StartWinnerBannerThread__(self)
        if Winner=='Player1':
            self.UpdateWinnerBannerText('PLAYER 1 WINS GAME!')
        else:
            self.UpdateWinnerBannerText('PLAYER 2 WINS GAME!')
    
        self.AmendPlayGameButton('active')
        self.AmendShuffleButton('active')
        
        #This runs the file FindTotalWins as a subprocess#
        subprocess.run(["python","FindTotalWins.py"])
    
    #This calls methods from the AddPoints file to add points to the database#
    def __AddPointsToTable__(Player1,Player2):
        if Player1>Player2:
            Player1Score=3
            Player2Score=1
        else:
            Player1Score=1
            Player2Score=3
        
        AddPointsPlayer1.__AddPoints__(Player1Score)
        AddRunningTotalPointsPlayer1.__AddPoints__(Player1Score)
        AddRunningTotalPointsPlayer2.__AddPoints__(Player2Score)
    

