#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
import tkinter as tk
import ModellValue

# Creates Enter-UI
class ModellUI:

    def __init__(self):
        # Values for drop lists
        self.list_Employee_status = ["Employee", "Ex-Employee", "Firm", "Not_Employee", "Passiv_Employee"]
        self.list_Country = ["BO", "DE", "ES", "IT", "PY"]
        self.list_Sex = ["Man", "Woman"]
        self.list_Indrel = ["Indrel_1", "Indrel_2", "Indrel_3", "Indrel_4", "Indrel_5"]
        self.list_Relationships = ["Activ_rel", "Inactiv_rel", "Non_rel", "Formal_rel", "Potential_rel"]
        self.list_Type_of_country = ["Same_country", "Another_country"]
        self.list_Type_of_homecountry = ["Same_homecountry", "Another_homecountry"]
        self.list_Canal = ["Canal_004", "Canal_007", "Canal_013", "Canal_025", "Canal_K00", "Canal_KAA",
                           "Canal_KAB", "Canal_KAC", "Canal_KAD", "Canal_KAE", "Canal_KAF", "Canal_KAG",
                           "Canal_KAH", "Canal_KAI", "Canal_KAJ", "Canal_KAK", "Canal_KAL", "Canal_KAM",
                           "Canal_KAN", "Canal_KAO", "Canal_KAP", "Canal_KAQ", "Canal_KAR", "Canal_KAS",
                           "Canal_KAT", "Canal_KAU", "Canal_KAV", "Canal_KAW", "Canal_KAY", "Canal_KAZ",
                           "Canal_KBB", "Canal_KBD", "Canal_KBE", "Canal_KBF", "Canal_KBG", "Canal_KBH",
                           "Canal_KBJ", "Canal_KBL", "Canal_KBM", "Canal_KBN", "Canal_KBO", "Canal_KBP",
                           "Canal_KBQ", "Canal_KBR", "Canal_KBS", "Canal_KBU", "Canal_KBV", "Canal_KBW",
                           "Canal_KBX", "Canal_KBY", "Canal_KBZ", "Canal_KCA", "Canal_KCB", "Canal_KCC",
                           "Canal_KCD", "Canal_KCE", "Canal_KCF", "Canal_KCG", "Canal_KCH", "Canal_KCI",
                           "Canal_KCJ", "Canal_KCK", "Canal_KCL", "Canal_KCM", "Canal_KCN", "Canal_KCO",
                           "Canal_KCP", "Canal_KCQ", "Canal_KCR", "Canal_KCS", "Canal_KCT", "Canal_KCU",
                           "Canal_KCV", "Canal_KCX", "Canal_KDA", "Canal_KDB", "Canal_KDC", "Canal_KDD",
                           "Canal_KDE", "Canal_KDF", "Canal_KDG", "Canal_KDH", "Canal_KDI", "Canal_KDL",
                           "Canal_KDM", "Canal_KDN", "Canal_KDO", "Canal_KDP", "Canal_KDQ", "Canal_KDR",
                           "Canal_KDS", "Canal_KDT", "Canal_KDU", "Canal_KDV", "Canal_KDW", "Canal_KDX",
                           "Canal_KDY", "Canal_KDZ", "Canal_KEA", "Canal_KEB", "Canal_KEC", "Canal_KED",
                           "Canal_KEE", "Canal_KEF", "Canal_KEG", "Canal_KEH", "Canal_KEI", "Canal_KEJ",
                           "Canal_KEK", "Canal_KEL", "Canal_KEM", "Canal_KEN", "Canal_KEO", "Canal_KEQ",
                           "Canal_KES", "Canal_KEU", "Canal_KEV", "Canal_KEW", "Canal_KEY", "Canal_KEZ",
                           "Canal_KFA", "Canal_KFB", "Canal_KFC", "Canal_KFD", "Canal_KFE", "Canal_KFF",
                           "Canal_KFG", "Canal_KFH", "Canal_KFI", "Canal_KFJ", "Canal_KFK", "Canal_KFL",
                           "Canal_KFM", "Canal_KFN", "Canal_KFP", "Canal_KFR", "Canal_KFS", "Canal_KFT",
                           "Canal_KFU", "Canal_KFV", "Canal_KGC", "Canal_KGN", "Canal_KGU", "Canal_KGV",
                           "Canal_KGW", "Canal_KGX", "Canal_KGY", "Canal_KHA", "Canal_KHC", "Canal_KHD",
                           "Canal_KHE", "Canal_KHF", "Canal_KHK", "Canal_KHL", "Canal_KHM", "Canal_KHN",
                           "Canal_KHO", "Canal_KHP", "Canal_KHQ", "Canal_KHR", "Canal_KHS", "Canal_RED"]
        self.list_Primary_index = [1, 99]
        self.list_seniority_index = []
        for x in range(1, 100):
            self.list_seniority_index.append(x)
        self.list_Index_new_customer = ["New", "Old"]
        self.list_Type_adresse = ["Primary", "Not primary"]
        self.list_Activity_index = ["Activ", "Not activ"]

        self.list_Region = ["ALAVA", "ALBACETE", "ALICANTE", "ALMERIA", "ASTURIAS", "AVILA", "BADAJOZ",
                            "BALEARS, ILLES", "BARCELONA", "BIZKAIA", "BURGOS", "CACERES", "CADIZ", "CANTABRIA", "CASTELLON", "CEUTA",
                            "CIUDAD REAL", "CORDOBA", "CORUNA, A", "CUENCA", "GIPUZKOA", "GIRONA", "GRANADA", "GUADALAJARA", "HUELVA",
                            "HUESCA", "JAEN", "LEON", "LERIDA", "LUGO", "MADRID", "MALAGA", "MELILLA", "MURCIA", "NAVARRA",
                            "OURENSE", "PALENCIA", "PALMAS", "LAS", "PONTEVEDRA", "RIOJA, LA", "SALAMANCA",
                            "SANTA CRUZ DE TENERIFE", "SEGOVIA", "SEVILLA", "SORIA", "TARRAGONA", "TERUEL", "TOLEDO",
                            "VALENCIA", "VALLADOLID","ZAMORA", "ZARAGOZA"]
        self.list_Segment = ["Segment_1", "Segment_2", "Segment_3"]

        self.list_Products = ["_Saving_acc", "_Guarantees", "_Current_acc", "_Derivada_acc", "_Payroll_acc",
                              "_Junior_acc",
                              "_Mas_particular_acc", "_Particular_acc", "_Particular_Plus_acc", "_Short-term_deposits",
                              "_Medium-term_deposits", "_Long-term_deposits", "_E-account", "_Funds", "_Mortgage",
                              "_Pensions",
                              "_Loans", "_Taxes", "_Credit_card", "_Securities", "_Home_acc", "_Payroll", "_Pensions",
                              "_Direct_debit"]
        self.list_Type_model = ["Random_Forest", "Random_Forest_with_random_grid"]

        # Creating of UI elements

        self.createWindow()
        self.drawTextFields()
        self.drawDropListsAndEnterFields()
        self.drawButton()
        self.window.mainloop()

    def createWindow(self):
        self.window = tk.Tk()
        self.window.title("Wirtschaftsinformatik Projekt Data Sciense: Kim, Eric and Oleksandr")
        self.window.geometry("770x610")
        self.window.resizable(False, False)
        self.window.config(bg="#e6e6e6")

    def drawTextFields(self):
        text_features_customer = tk.Label(self.window, text="Features of customer:", fg="black", bg="#e6e6e6")
        text_features_customer.config(font=("Arial", 10, "bold"))
        text_features_customer.grid(row=2, column=2, sticky="w")

        text_product = tk.Label(self.window, text="Product:", fg="black", bg="#e6e6e6")
        text_product.config(font=("Arial", 10, "bold"))
        text_product.grid(row=2, column=4, sticky="w")

        text_product = tk.Label(self.window, text="Model Configuration:", fg="black", bg="#e6e6e6")
        text_product.config(font=("Arial", 10, "bold"))
        text_product.grid(row=7, column=4, sticky="w")

        listOfValues = ["Age:", "Month of transaction:", "Income:", "Last date prime:", "Sex:", "Employee status:",
                        "Country:", "Type of country:", "Type of homecountry:", "Adresse type:", "Index new customer:",
                        "Seniority index:", "Primary index:", "Activity index:", "Indrel:", "Relationships:", "Canal:",
                        "Region:", "Segment:"]

        for index, item in enumerate(listOfValues):
            text_product = tk.Label(self.window, text=str(item), fg="black", bg="#e6e6e6")
            text_product.config(font=("Arial", 10))
            text_product.grid(row=int(index + 5), column=2, sticky="w")

        list_model_config = ["Type of model:", "Name of CSV with data:", "Name of CSV with new head:",
                             "Size of test data:", "Random state:"]
        for index, item in enumerate(list_model_config):
            text_product = tk.Label(self.window, text=str(item), fg="black", bg="#e6e6e6")
            text_product.config(font=("Arial", 10))
            text_product.grid(row=int(index + 8), column=4, sticky="w")

    def drawDropListsAndEnterFields(self):

        self.enter_age = tk.Entry(self.window, width=25, bg="white")
        self.enter_age.grid(row=5, column=3)

        self.enter_Month_of_transaction = tk.Entry(self.window, width=25, bg="white")
        self.enter_Month_of_transaction.grid(row=6, column=3)

        self.enter_Income = tk.Entry(self.window, width=25, bg="white")
        self.enter_Income.grid(row=7, column=3)

        self.enter_Last_date_prime = tk.Entry(self.window, width=25, bg="white")
        self.enter_Last_date_prime.grid(row=8, column=3)

        self.CSV_db = tk.Entry(self.window, width=25, bg="white")
        self.CSV_db.grid(row=9, column=5)

        self.CSV_head = tk.Entry(self.window, width=25, bg="white")
        self.CSV_head.grid(row=10, column=5)

        self.test_size = tk.Entry(self.window, width=25, bg="white")
        self.test_size.grid(row=11, column=5)

        self.random_state = tk.Entry(self.window, width=25, bg="white")
        self.random_state.grid(row=12, column=5)

        self.enter_sex = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_sex, *self.list_Sex)
        drop.grid(row=9, column=3, sticky="w")
        drop.config(width=25)

        self.enter_employee = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_employee, *self.list_Employee_status)
        drop.grid(row=10, column=3, sticky="w")
        drop.config(width=25)

        self.enter_country = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_country, *self.list_Country)
        drop.grid(row=11, column=3, sticky="w")
        drop.config(width=25)

        self.enter_type_country = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_type_country, *self.list_Type_of_country)
        drop.grid(row=12, column=3, sticky="w")
        drop.config(width=25)

        self.enter_type_home = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_type_home, *self.list_Type_of_homecountry)
        drop.grid(row=13, column=3, sticky="w")
        drop.config(width=25)

        self.enter_type_adresse = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_type_adresse, *self.list_Type_adresse)
        drop.grid(row=14, column=3, sticky="w")
        drop.config(width=25)

        self.enter_index_new_customer = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_index_new_customer, *self.list_Index_new_customer)
        drop.grid(row=15, column=3, sticky="w")
        drop.config(width=25)

        self.enter_seniority_index = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_seniority_index, *self.list_seniority_index)
        drop.grid(row=16, column=3, sticky="w")
        drop.config(width=25)

        self.enter_primary_index = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_primary_index, *self.list_Primary_index)
        drop.grid(row=17, column=3, sticky="w")
        drop.config(width=25)

        self.enter_index_activity = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_index_activity, *self.list_Activity_index)
        drop.grid(row=18, column=3, sticky="w")
        drop.config(width=25)

        self.enter_indrel = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_indrel, *self.list_Indrel)
        drop.grid(row=19, column=3, sticky="w")
        drop.config(width=25)

        self.enter_relationship = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_relationship, *self.list_Relationships)
        drop.grid(row=20, column=3, sticky="w")
        drop.config(width=25)

        self.enter_canal = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_canal, *self.list_Canal)
        drop.grid(row=21, column=3, sticky="w")
        drop.config(width=25)

        self.enter_region = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_region, *self.list_Region)
        drop.grid(row=22, column=3, sticky="w")
        drop.config(width=25)

        self.enter_segment = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_segment, *self.list_Segment)
        drop.grid(row=23, column=3, sticky="w")
        drop.config(width=25)

        self.enter_product = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_product, *self.list_Products)
        drop.grid(row=5, column=4, sticky="w")
        drop.config(width=25)

        self.enter_type_model = tk.StringVar()
        drop = tk.OptionMenu(self.window, self.enter_type_model, *self.list_Type_model)
        drop.grid(row=8, column=5, sticky="w")
        drop.config(width=30)

    def updateValues(self):
        ModellValue.enter_age_value = self.enter_age.get()
        ModellValue.enter_index_new_customer_value = self.enter_index_new_customer.get()
        ModellValue.enter_primary_index_value = self.enter_primary_index.get()
        ModellValue.enter_type_adresse_value = self.enter_type_adresse.get()
        ModellValue.enter_Income_value = self.enter_Income.get()
        ModellValue.enter_Month_of_transaction_value = self.enter_Month_of_transaction.get()
        ModellValue.enter_employee_value = self.enter_employee.get()
        ModellValue.enter_country_value = self.enter_country.get()
        ModellValue.enter_sex_value = self.enter_sex.get()
        ModellValue.enter_indrel_value = self.enter_indrel.get()
        ModellValue.enter_relationship_value = self.enter_relationship.get()
        ModellValue.enter_type_country_value = self.enter_type_country.get()
        ModellValue.enter_type_home_value = self.enter_type_home.get()
        ModellValue.enter_canal_value = self.enter_canal.get()
        ModellValue.enter_region_value = self.enter_region.get()
        ModellValue.enter_segment_value = self.enter_segment.get()
        ModellValue.enter_index_activity_value = self.enter_index_activity.get()
        ModellValue.enter_seniority = self.enter_seniority_index.get()
        ModellValue.enter_Last_date_prime = self.enter_Last_date_prime.get()
        ModellValue.CSV_db = self.CSV_db.get()
        ModellValue.CSV_head = self.CSV_head.get()
        ModellValue.enter_test_size = self.test_size.get()
        ModellValue.enter_random_state = self.random_state.get()
        ModellValue.enter_produkt = self.enter_product.get()
        ModellValue.enter_typ_model = self.enter_type_model.get()

    def drawButton(self):
        self.button = tk.Button(self.window, text="Save Values", command=self.updateValues)
        self.button.config(width=15, height=2, bg="#b8b8b8", fg="black")
        self.button.grid(row=23, column=4)
        self.button2 = tk.Button(self.window, text="Prediction", command=self.window.destroy)
        self.button2.config(width=15, height=2, bg="#b8b8b8", fg="black")
        self.button2.grid(row=23, column=5)