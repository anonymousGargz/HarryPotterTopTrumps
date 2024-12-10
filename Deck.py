#MERGESORTS THE CHARACTER CARDS FOR THE DECK PAGE#
import sqlite3

tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()

#Fetches all rows of cards from the table topTrumpsDeck#
cur.execute("""SELECT * FROM topTrumpsDeck """)
try:
    AllCards=cur.fetchall()
    CharacterNames=[]


    for i in range(len(AllCards)):
        IndividualCard=AllCards[i]
        CharacterNames.append(IndividualCard[1])
    
    
except:
    print("Can't fetch cards")

#Repeatedly splits the dataset in half recursively 
#until each name is in an individual list
#calls the merge function on each list
def MergeSortCharacterNames(CharacterNames):
    ListLength=len(CharacterNames)
    if ListLength > 1:
    
        MiddleOfList = ListLength // 2
        FirstHalf=[]
        SecondHalf=[]

        for i in range(0, MiddleOfList):
            FirstHalf.append(CharacterNames[i])
        
        for j in range(MiddleOfList, ListLength):
            SecondHalf.append(CharacterNames[j])
        
        FirstHalf=MergeSortCharacterNames(FirstHalf)
        SecondHalf=MergeSortCharacterNames(SecondHalf)
        
        return MergeNames(FirstHalf, SecondHalf)
    else:
        return CharacterNames

#Puts the lists back together in alphabetical order#
def MergeNames(First, Second):
    OriginalList=[]
    for i in range(0, len(First)):
        OriginalList.append(First[i])
    
    for i in range(0, len(Second)):
        OriginalList.append(Second[i])
    MergedList= []
    
    IndexLeft=0
    IndexMiddle=len(First)
    IndexRight=IndexMiddle
    End=len(OriginalList)
    
    while IndexLeft < IndexMiddle and IndexRight < End:
        if OriginalList[IndexLeft] < OriginalList[IndexRight]:
            MergedList.append(OriginalList[IndexLeft])
            IndexLeft += 1
            
        else:
            MergedList.append(OriginalList[IndexRight])
            IndexRight+=1
    
    if IndexLeft!=IndexMiddle:
        for i in range(IndexLeft, IndexMiddle):
            MergedList.append(OriginalList[i])
    
    elif IndexRight!=End:
        for i in range(IndexRight, End):
            MergedList.append(OriginalList[i])
    
    return MergedList




#Appends each card (in alphabetical order) to a list of tuples called ListOfCharacters#
def GetValues(CharacterNamesAlphabetical):
    ListOfCharacters=[]
    for i in range(len(CharacterNamesAlphabetical)):
        cur.execute("SELECT * FROM topTrumpsDeck WHERE FirstName=(?)", (CharacterNamesAlphabetical[i],))
        CharacterValues=cur.fetchone()
        CardID=CharacterValues[0]
        FirstName=CharacterValues[1]
        LastName=CharacterValues[2]
        SpellSkill=CharacterValues[3]
        Bravery=CharacterValues[4]
        BroomSkill=CharacterValues[5]
        Kindness=CharacterValues[6]
        Strength=CharacterValues[7]
        TopTrumpsRating=CharacterValues[8]
       
        cur.execute("""SELECT * FROM topTrumpsDeck INNER JOIN CardsInPlay 
                    ON topTrumpsDeck.CardID=CardsInPlay.CardID WHERE CardsInPlay.CardID=(?) """, 
                    (CardID,))
        InPlay=cur.fetchone()
        if InPlay is None:
            Unlocked=False
        else:
            Unlocked=True
        Character=(CardID,FirstName,LastName,SpellSkill,Bravery,BroomSkill,Kindness,Strength,
                   TopTrumpsRating,Unlocked)
        ListOfCharacters.append(Character)
    
    return ListOfCharacters


CharacterNamesAlphabetical = MergeSortCharacterNames(CharacterNames)
Results=GetValues(CharacterNamesAlphabetical)


#Returns list of sorted cards#
class CardInDeck():
    def __init__():
        pass
    def __ReturnSortedCards__():
        try:
            return Results
        except:
            return("Can't get cards")

