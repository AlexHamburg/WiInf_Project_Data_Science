#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 23:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
import tkinter as tk
import ModellValue

# creat UI with results
class ModellResultUI:
    def __init__(self):
        self.createWindow()
        self.createTextFields()
        self.createResultFields()
        self.drawButton()
        self.window.mainloop()

    def createWindow(self):
        self.window = tk.Tk()
        self.window.title("Result Page")
        self.window.geometry("610x300")
        self.window.resizable(False, False)
        self.window.config(bg="#e6e6e6")

    def createTextFields(self):
        listMitLabels = ["Accuracy (train set) ::", "Accuracy (test set) ::", ""]

        for index, item in enumerate(listMitLabels):
            label = tk.Label(self.window, text=str(item), fg="black", bg="#e6e6e6")
            label.config(font=("Arial", 10, "bold"))
            label.grid(row=index+2, column=2, sticky="w")

        lable_UI = tk.Label(self.window, text="Confusion Matrix ::", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=6, column=2, sticky="w")

        lable_UI = tk.Label(self.window, text="Real Values", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=5, column=6, sticky="w", columnspan = 3)

        lable_UI = tk.Label(self.window, text="Predict", fg="black", bg="#e6e6e6", justify="right")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=7, column=4, sticky="w")

        lable_UI = tk.Label(self.window, text="Values", fg="black", bg="#e6e6e6", justify="right")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=8, column=4, sticky="w")

        lable_UI = tk.Label(self.window, text="Will buy", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=6, column=6, sticky="w")

        lable_UI = tk.Label(self.window, text="Will not buy", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=6, column=7, sticky="w")

        lable_UI = tk.Label(self.window, text="Will buy", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=7, column=5, sticky="w")

        lable_UI = tk.Label(self.window, text="Will not buy", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=8, column=5, sticky="w")

        lable_UI = tk.Label(self.window, text="Prediction result ::", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=10, column=2, sticky="w")

        lable_UI = tk.Label(self.window, text="", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=11, column=2, sticky="w")

        lable_UI = tk.Label(self.window, text="Cross validation ::", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=12, column=2, sticky="w")

        lable_UI = tk.Label(self.window, text="Diff. time ::", fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=15, column=2, sticky="w")

    def createResultFields(self):

        lable_UI = tk.Label(self.window, text=str(ModellValue.trainAccuracy), fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=2, column=3, sticky="w")

        lable_UI = tk.Label(self.window, text=str(ModellValue.testAccuracy), fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=3, column=3, sticky="w")

        lable_UI = tk.Label(self.window, text=str(ModellValue.testAccuracy), fg="black", bg="#e6e6e6")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=3, column=3, sticky="w")

        lable_UI = tk.Label(self.window, text=ModellValue.confusionMatrix[0][0], fg="black", bg="#e6e6e6", justify="center")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=7, column=6, sticky="w")

        lable_UI = tk.Label(self.window, text=ModellValue.confusionMatrix[1][0], fg="black", bg="#e6e6e6", justify="center")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=8, column=6, sticky="w")

        lable_UI = tk.Label(self.window, text=ModellValue.confusionMatrix[0][1], fg="black", bg="#e6e6e6", justify="center")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=7, column=7, sticky="w")

        lable_UI = tk.Label(self.window, text=ModellValue.confusionMatrix[1][1], fg="black", bg="#e6e6e6", justify="center")
        lable_UI.config(font=("Arial", 10))
        lable_UI.grid(row=8, column=7, sticky="w")

        lable_UI = tk.Label(self.window, text="Client " + ModellValue.prediktionResult, fg="black", bg="#e6e6e6", justify="left")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=10, column=3, sticky="w", columnspan = 6, rowspan = 1)

        lable_UI = tk.Label(self.window, text=ModellValue.crossValidation, fg="black", bg="#e6e6e6", justify ="left")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=12, column=3, sticky="w", columnspan = 9, rowspan = 3)

        lable_UI = tk.Label(self.window, text="%s hr. %s min. %s sec." %(str(ModellValue.diffHr), str(ModellValue.diffMin),
                                                                         str(ModellValue.diffSec)), fg="black", bg="#e6e6e6", justify ="left")
        lable_UI.config(font=("Arial", 10, "bold"))
        lable_UI.grid(row=15, column=3, sticky="w")

    def drawButton(self):
        self.button2 = tk.Button(self.window, text="Close", command=self.window.destroy)
        self.button2.config(width=15, height=2, bg="#b8b8b8", fg="black")
        self.button2.grid(row=20, column=6)
