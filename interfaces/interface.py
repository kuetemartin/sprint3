from tkinter import *
import tkinter.messagebox
import customtkinter
import  os
from logiques.construction import creationListeBoutons

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class Calculatrice(customtkinter.CTk):
    width = 800
    height = 800

    def __init__(self):
        super().__init__()

        # Creation de la fenêtre
        self.title("calculatrice")
        self.geometry(f'{Calculatrice.width}x{Calculatrice.height}')
        self.protocol("WM_DELETE_WINDOW",self.on_closing)


        # Creation des grid ou composantes
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self,
            width=400,
            height=730,
            corner_radius=0)
        self.frame_left.grid(row=0,column=0,padx=20,pady=20)

        self.frame_right = customtkinter.CTkFrame(
            master=self, width=300,
            height=700,)
        self.frame_right.grid(row=0,column=1,padx=20,pady=20)

        self.equation = Variable()
        self.equation.set("0")
        self.ecran = Label(
            self.frame_left,
            textvariable=self.equation,
            bg="#101419",
            fg="#FFF",
            height=4,
            width=42
        )
        self.ecran.grid(columnspan=4)

        tab = [7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
        boutons = creationListeBoutons(tab)
        ligne = 1
        colone = 0

        for bouton in boutons:
            b = Label(self.frame_left, text=str(bouton.getValeur()), bg="#476C9B", fg="#FFF", height=8, width=10)
            # Rendre le texte cliquable
            b.bind("<Button-1>", lambda e, bouton=bouton: self.appuyer(bouton.getValeur()))

            b.grid(row=ligne, column=colone)

            colone += 1
            if colone == 4:
                colone = 0
                ligne += 1


        b = Label(self.frame_left,text="Effacer",bg="#984447",fg="#FFF",height=4,width=42)
        b.bind("<Button-1>", lambda e: self.effacer())
        b.grid(columnspan=4)

        self.expression = ""

        self.fichier()

    def on_closing(self,event=0):
        self.destroy()



    def appuyer(self,touche):
        print(touche)
        if touche == "=":
            self.calculer()
            return

        self.expression += str(touche)
        self.equation.set(self.expression)

    def effacer(self):
        self.expression = ""
        self.equation.set("0")

    def calculer(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = total
        except:
            self.equation.set("erreur")
            self.expression = ""


    def fichier(self):
        if os.path.exists("fichiers/expression.txt"):
            with open("fichiers/expression.txt","r") as fichier :
                self.expression =  fichier.readline()
                try:
                    total = str(eval(self.expression))
                    self.equation.set(total)
                    self.expression = total
                except:
                    self.equation.set("erreur")
                    self.expression = ""

