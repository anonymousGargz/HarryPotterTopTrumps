
import customtkinter 
from customtkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from Progress import PlayerPoints



#Displays the elements of the Progress Page, inherits from the gameInterface frame mainArea#
class ProgressPage(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, fg_color='#e6ecfa')

        #Displays the background image#
        imgBackground=Image.open('RavenclawRoom.webp')
        resized=imgBackground.resize((2250,1500))
        backgroundImage=ImageTk.PhotoImage(resized)
        
        self.__imageBackground=customtkinter.CTkLabel(self, image=backgroundImage)
        self.__imageBackground.place(relx=0,rely=0,relheight=1,relwidth=1)
        
        #Displays the title of the page#
        self.__title=customtkinter.CTkLabel(self, text='Progress Page', font=('Berlin Sans FB Demi',40), corner_radius=20, fg_color='#e6ecfa')
        self.__title.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.1)

        #Creates a canvas/grid to display the bar chart#
        self.fig, self.ax= plt.subplots()
        self.__canvas=FigureCanvasTkAgg(self.fig, master=self)
        self.__canvas.get_tk_widget().place(relx=0.15,rely=0.3,relwidth=0.7,relheight=0.5)

        #Creates an object of the PlayerPoints class#
        self.__Player1Points=PlayerPoints() #composition
        self.__Player2Points=PlayerPoints() #composition

        self.__Plot__()
        
    def __Plot__(self):

        #Gets the points list for Player1/2#
        try:
            Player1=self.__Player1Points.ReturnPlayer1Points()
            Player2=self.__Player2Points.ReturnPlayer2Points()
        except:
            print("Cannot access total points")

        plt.figure(facecolor='#8cc2f5')

        #Declares the values of the independent variables on the x-axis#
        Days=['4 Days Ago', '3 days ago', '2 days ago', 'Yesterday', 'Today']

        index=np.arange(5)

        #Creates two bars for the Player1/Player2 score#
        self.ax.bar(index, Player1, width=0.2, label='Player1Score', color='#103894')
        self.ax.bar(index+0.2, Player2, width=0.2, label='Player2Score', color='#648be8')

        #Sets the x/y axis labels#
        self.ax.set_xlabel('Day', fontsize=15, fontname='Berlin Sans FB Demi')
        self.ax.set_ylabel('Points Gained', fontsize=15, fontname='Berlin Sans FB Demi')
        self.ax.set_xticks(index+0.2, Days)
        self.ax.set_ylim(0,40)
        self.ax.legend(loc="upper right", ncols=2)

        #Creates the bar chart#
        self.__canvas.draw()