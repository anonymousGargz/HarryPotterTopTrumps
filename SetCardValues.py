
#This class deals with displaying the character values on the user interface for the Player#
class SetPlayer1CardValues():
    def __init__(self):
        pass

    def __GetCardValues__(self, Player1Card):
        Current=Player1Card.cardStack
        #Gets the card at the top of the cardStack for a player#
        CharacterValuesPlayer1=Current.pop()
        print(Player1Card.cardStack)
        SetPlayer1CardValues.__UpdatePlayer1CardValues__(self, CharacterValuesPlayer1)
       
    #This displays the character values onto Player1's card by calling the ConfigureCardPlayer1 
        #method from the PlayPage class#
    def __UpdatePlayer1CardValues__(self, CharacterValuesPlayer1):
        self.ConfigureCardPlayer1(CharacterValuesPlayer1)
    
    #This hides Player1's card by calling the method from the PlayPage class#
    def __HidePlayer1Card__(self):
        self.HidePlayer1Card()
    
    #This removes the back of the card, revealing Player1's card by calling the method from the PlayPage class#
    def __RevealPlayer1Card__(self):
        self.RemoveBackOfCard()


#This class deals with displaying the character values on the user interface for Player2#
class SetPlayer2CardValues():
    def __init__(self):
        pass
    
    def __GetCardValues__(self, Player2Card):
        Current=Player2Card.cardStack
        #Gets the card at the top of the cardStack for a player#
        CharacterValuesPlayer2=Current.pop()
        print(Player2Card.cardStack)
        SetPlayer2CardValues.__UpdatePlayer2CardValues__(self, CharacterValuesPlayer2)
        
#This displays the character values onto Player2's card by calling the ConfigureCardPlayer1 
        #method from the PlayPage class#
    def __UpdatePlayer2CardValues__(self, CharacterValuesPlayer2):
        self.ConfigureCardPlayer2(CharacterValuesPlayer2)
    
    #This hides Player2's card by calling the method from the PlayPage class#
    def __HidePlayer2Card__(self):
        self.HidePlayer2Card()
    
    #This removes the back of the card, revealing Player2's card by calling the method from the PlayPage class#
    def __RevealPlayer2Card__(self):
        self.RemoveBackOfCard()

