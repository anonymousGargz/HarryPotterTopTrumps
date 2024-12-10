import random
#Creates a Questions class#
class Questions():
    def __init__(self, Question, WrongAnswer1,WrongAnswer2, RightAnswer):
        self.Question=Question
        self.WrongAnswer1=WrongAnswer1
        self.WrongAnswer2=WrongAnswer2
        self.RightAnswer=RightAnswer
        self.AnswersArray=[WrongAnswer1,WrongAnswer2,RightAnswer]
    
    def GetQuestion(self):
        return self.Question
    
    def GetWrongAnswer1(self):
        return self.WrongAnswer1
    
    def GetWrongAnswer2(self):
        return self.WrongAnswer2
    
    def GetRightAnswer(self):
        return self.RightAnswer
    
    #Returns a random answer from the AnswersArray by shuffling the list#
    def GetAnAnswer(self):
        random.shuffle(self.AnswersArray)
        Answer=self.AnswersArray[0]
        self.AnswersArray.remove(Answer)
        return(Answer)
