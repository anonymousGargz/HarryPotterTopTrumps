#HANDLES THE QUIZ#

import customtkinter
from customtkinter import *
from Quiz import Questions
import random
from time import *
import sqlite3
from datetime import date

#Creates a connection object to connect to the database, and a cursor to navigate it#
tableConnection=sqlite3.connect('TopTrumpsDeck.db', check_same_thread=False)
cur=tableConnection.cursor()

#Tuple of questions and answers#
ListOfAllQuestions=[("What is the name of the pub at the entrance to Diagon Alley?", 
                     "The Three Broomsticks", "The Hog's Head", "The Leaky Cauldron"),
                 ("What does the Seeker catch in Quidditch?", "Quaffle","Bludger", "Bludger"),
                 ("What is revealed to be Neville's greatest fear by the boggart?", "Grandma", 
                  "Dementors", "Snape"),
                 ("What does Snape teach Harry in 'The Order Of The Phoenix'?","Legillemency", "Patronus", 
                  "Occlumency"),
                 ("What position does Harry play on his Quidditch team?","Chaser", "Keeper", "Seeker"),
                 ("Who knocks out the troll in 'The Philosopher's Stone'?","Harry", "Snape", "Ron"),
                 ("Who poses as Mad-Eye Moody in 'The Goblet of Fire'?","Voldemort", "Peter", 
                  "Barty Crouch Jr"),
                 ("Albus Dumbledore destroyed which Horcrux?","Cup", "Ring", "Locket"),
                 ("A wizard who cannot do magic is called?","Duddle", "Bleaker", "Squib"),
                 ("What is Filch's cat called?","Buttercup", "Jones", "Mrs Norris"),
                 ("What is not a form of currency in the wizarding world?","Sickles", "Knuts", "Doxies"),
                 ("Who gave Harry the invisibility cloak?","Snape", "Sirius", "Dumbledore"),
                 ("What model is Harry's first ever broom?","Cleansweep One", "Firebolt", "Nimbus 2000"),
                 ("What gemstone represents students from Ravenclaw?","Sapphire", "Emerald", "Topaz")]

ListOfQuestions=[]

#Creates a tuple of 3 random question/answer lists#
while len(ListOfQuestions)<3:
    randomQuestion=random.randint(0,len(ListOfAllQuestions)-1)
    if ListOfAllQuestions[randomQuestion] not in ListOfQuestions:
        ListOfQuestions.append(ListOfAllQuestions[randomQuestion])
       

#displays the quiz window#
class QuizWindow():
    def __init__(self):
        self.top=customtkinter.CTkToplevel()
        self.top.title("QUIZ WINDOW")
        self.top.geometry("1000x500")
        
        #Displays the frame#
        self.Frame=customtkinter.CTkLabel(self.top, fg_color='#f5c020', text='')
        self.Frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        #Displays 'Ask Question' button#
        self.AskQuestion=customtkinter.CTkButton(self.top, fg_color='#d6870f', text='ASK QUESTION', 
                                                 font=('Berlin Sans FB Demi',20), corner_radius=20, 
                                                 text_color='#fcf8f2', bg_color='#f5c020', 
                                                 command= lambda: QuizWindow.__GetQuestion__(self))
        self.AskQuestion.place(relx=0.4,rely=0.75,relwidth=0.2,relheight=0.2)

        #Displays the question label#
        self.QuestionLabel=customtkinter.CTkLabel(self.top, fg_color='#d6870f', 
                                                  text='QUESTION', font=('Berlin Sans FB Demi',20), 
                                                  corner_radius=20, bg_color='#f5c020')
        self.QuestionLabel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

        #Displays the first answer button#
        self.Answer1=customtkinter.CTkButton(self.top, fg_color='#d6870f', text='ANSWER1',
                                              font=('Berlin Sans FB Demi',20), corner_radius=20, 
                                              text_color='#fcf8f2', bg_color='#f5c020',
                                                command=lambda AnswerChosen='Answer1': 
                                                QuizWindow.__CheckAnswer__(self, AnswerChosen))
        self.Answer1.place(relx=0.15, rely=0.5, relwidth=0.2, relheight=0.2)

        #Displays the second answer button#
        self.Answer2=customtkinter.CTkButton(self.top, fg_color='#d6870f', text='ANSWER2',
                                              font=('Berlin Sans FB Demi',20), corner_radius=20, 
                                              text_color='#fcf8f2',bg_color='#f5c020', 
                                              command=lambda AnswerChosen='Answer2': 
                                              QuizWindow.__CheckAnswer__(self, AnswerChosen))
        self.Answer2.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.2)

        #Displays the third answer button#
        self.Answer3=customtkinter.CTkButton(self.top, fg_color='#d6870f', text='ANSWER3', 
                                             font=('Berlin Sans FB Demi',20), corner_radius=20, 
                                             text_color='#fcf8f2', bg_color='#f5c020', 
                                             command=lambda AnswerChosen='Answer3': 
                                             QuizWindow.__CheckAnswer__(self, AnswerChosen))
        self.Answer3.place(relx=0.65, rely=0.5, relwidth=0.2, relheight=0.2)

        self.Question=None
        self.RightAnswer=None

        self.top.mainloop()
    
    #chooses a question/answer list from the tuple defined above#
    def __GetQuestion__(self):
        #Closes the window if 3 questions have been answered#
        try:
            if len(ListOfQuestions)==0:
                self.top.destroy()
            
            if len(ListOfQuestions)==1:
                QuestionNumber=0

            #Generates a random question number#  
            else:  
                QuestionNumber=random.randint(0,len(ListOfQuestions)-1)
            #Selects a question/answer list from the ListOfQuestions tuple#
            QuestionPack=ListOfQuestions[QuestionNumber]
            
            Question=QuestionPack[0]
            WrongAnswer1=QuestionPack[1]
            WrongAnswer2=QuestionPack[2]
            RightAnswer=QuestionPack[3]

            #Creates an object of the questions class using the question and answers as parameters#
            self.Question=Questions(Question,WrongAnswer1,WrongAnswer2,RightAnswer) #COMPOSITION#
            self.RightAnswer=RightAnswer
            
            #Removes the first question from the list#
            ListOfQuestions.pop(QuestionNumber)

            self.__ConfigureQuestions__()
        except:
            print("Questions not in range")

    #Displays the questions and answers onto the quiz window#   
    def __ConfigureQuestions__(self):
        self.QuestionLabel.configure(text=self.Question.GetQuestion())
        self.Answer1.configure(text=self.Question.GetAnAnswer())
        self.Answer2.configure(text=self.Question.GetAnAnswer())
        self.Answer3.configure(text=self.Question.GetAnAnswer())

    #Checks whether the answer is right or not#
    def __CheckAnswer__(self, AnswerChosen):
        #Checks whether the answer chosen by the user matches right answer from the Questions class 
        #attribute rightAnswer#
        match AnswerChosen:
            case 'Answer1':
                Answer=self.Answer1.cget('text')
            case 'Answer2':
                Answer=self.Answer2.cget('text')
            case 'Answer3':
                Answer=self.Answer3.cget('text')
        
        #Displays a message to indicate whether the user got the question right/not#
        if Answer==self.RightAnswer:
            self.QuestionLabel.configure(text='Correct! 3 Points Won!')
            
            #inserts points into the database depending on whether the user's answer was correct/not#
            Values=[date.today().strftime("%d/%m/%Y"),3]
            cur.execute("INSERT INTO RunningTotalWinsPlayer1(Date,QuizPoints) VALUES (?,?)", Values)
            tableConnection.commit()
            cur.execute("INSERT INTO RunningTotalWinsPlayer2(Date,QuizPoints) VALUES (?,?)", Values)
            tableConnection.commit()
        
        else:
            self.QuestionLabel.configure(text='Incorrect! 0 Points Won!')
            
            Values=[date.today().strftime("%d/%m/%Y"),0]
            cur.execute("INSERT INTO RunningTotalWinsPlayer1(Date,QuizPoints) VALUES (?,?)", Values)
            tableConnection.commit()
            cur.execute("INSERT INTO RunningTotalWinsPlayer2(Date,QuizPoints) VALUES (?,?)", Values)
            tableConnection.commit()
        

QuizWindow()
