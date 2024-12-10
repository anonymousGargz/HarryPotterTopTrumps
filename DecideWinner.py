from time import *

class DecideWinner():
    def __init__():
        pass

#This takes both Player1/2's scores for the round as arguments and determines the winner of the 
    #round on Player 1's turn#   
    def __DecideWinner__(self, Player1Score, Player2Score, Player1Card, Player2Card):
        #AddPoints adds points to each player's pointStack depending on the result#
        try:
            if Player1Score>Player2Score:
                print("Player1 Wins")
                Player1Card.AddPoints('Win')
                Player2Card.AddPoints('Loss')
                self.UpdateWinnerBannerText('PLAYER 1 WINS ROUND!')
            else:
                print("Player2 Wins")
                Player2Card.AddPoints('Win')
                Player1Card.AddPoints('Loss')
                self.UpdateWinnerBannerText('PLAYER 2 WINS ROUND!')
        except:
            print("Invalid scores")
            self.UpdateWinnerBannerText('No one wins')
    
    def __CheckGameOver__(self, InitialNumberOfCards, Player1Card):
        #If all the cards have been played in the game, DecideGameWinner is called#
        if (len(Player1Card.pointsStack))==InitialNumberOfCards:
            return True

#This method recursively finds the sum of the pointStack for a player#
    def __FindSumOfPointsStack__(self, StackToUse, LengthOfStack):
        if (LengthOfStack)==0:
            return 0
        else:
            return StackToUse[LengthOfStack-1]+DecideWinner.__FindSumOfPointsStack__(self, StackToUse, 
                                                                                     LengthOfStack-1)

#This method determines the winner of a game depending on who gained more points in the game and 
#returns the winner's name#       
    def __DecideGameWinner__(self, Player1Card, Player2Card):
        Player1Total=(DecideWinner.__FindSumOfPointsStack__(self,Player1Card.pointsStack, 
                                                            len(Player1Card.pointsStack)))
        Player2Total=(DecideWinner.__FindSumOfPointsStack__(self,Player2Card.pointsStack, 
                                                            len(Player2Card.pointsStack)))
        if Player1Total>Player2Total:
            return ("Player1")
        else:
            return ("Player2")