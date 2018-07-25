#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
from ModellRandomForestService import ModelRandomForestService
from ModellSVMService import ModelSVMService
import pandas as pd
from sklearn.model_selection import train_test_split
import time
import ModellValue

# Read and clean data from .csv file
class ModellService():
    def __init__(self, name_of_csv, name_of_new_head, test_size, random_state, name_of_product,
                 model_type, prediction_vector):

        # Global Variable
        self.dataset = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.hr = 0
        self.min = 0
        self.sec = 0
        self.accur_result = None

        self.best_accuracy = None
        self.best_param = None
        self.classifier = None
        self.X_train_after = None
        self.X_test_after = None
        self.prediction_train = None
        self.prediction_test = None
        self.prediction_product = None

        #Check time
        self.befor = time.time()
        #Call of functions     
        self.readAndCleanData(name_of_csv, name_of_new_head, name_of_product)
        self.splitDataSet(test_size, random_state)
        
        if model_type is "SVM":
            svm_model = ModelSVMService(self.X_train, self.y_train, self.X_test, prediction_vector)

            self.best_accuracy = svm_model.best_accuracy
            self.best_param = svm_model.best_param
            self.classifier = svm_model.classifier
            self.X_train_after = svm_model.X_train
            self.X_test_after = svm_model.X_test
            self.prediction_train = svm_model.prediction_train
            self.prediction_test = svm_model.prediction_test
            self.prediction_product = svm_model.prediction_product
        else:
            ModelRandomForestService(self.X_train, self.y_train, self.X_test, self.y_test, model_type,
                                                self.X, prediction_vector)
            self.X_train_after = self.X_train
            self.X_test_after = self.X_test
            self.result = ModellValue.prediktionResult
            self.trainAccuracy = ModellValue.trainAccuracy
            self.testAccuracy = ModellValue.testAccuracy
            self.confusionMatrix = ModellValue.confusionMatrix
            self.crossValidation = ModellValue.crossValidation

        self.after = time.time()
        try:
            self.estimateTimeDiff(self.befor, self.after)
            ModellValue.diffHr = self.hr
            ModellValue.diffMin = self.min
            ModellValue.diffSec = self.sec
        finally:
            pass



    def readAndCleanData (self, name_of_csv, name_of_new_head, name_of_product):
        
        self.dataset = pd.read_csv(str(name_of_csv), sep="\t")
        self.dataset.columns = list(pd.read_csv(str(name_of_new_head), sep=";"))
        self.dataset = self.dataset.iloc[:,1:284]
        db_head = list(self.dataset)
        str_var_drop_set = ['Date_of_Transaction','Customer_code','First_contact']
        db_head_right = [x for x in db_head if x not in str_var_drop_set]
    
        for s in db_head_right:
            self.dataset[s] = pd.to_numeric(self.dataset[s], errors="coerce")
    
        self.dataset.loc[self.dataset.Last_date_prime.isnull(), 'Last_date_prime'] = 0
        self.dataset.isnull().any()
    
        indepent_var_drop_set = ['Date_of_Transaction','Customer_code','First_contact', 'Code_district', '_Saving_acc', '_Guarantees', '_Current_acc',
                                 '_Derivada_acc', '_Payroll_acc', '_Junior_acc', '_Mas_particular_acc', '_Particular_acc', '_Particular_Plus_acc', 
                                 '_Short-term_deposits', '_Medium-term_deposits', '_Long-term_deposits', '_E-account', '_Funds', '_Mortgage', '_Pensions',
                                 '_Loans', '_Taxes', '_Credit_card', '_Securities', '_Home_acc', '_Payroll', '_Pensions', '_Pensions_second', '_Direct_debit', 'Alive' , 'Dead']
        self.X = self.dataset.drop(indepent_var_drop_set, axis=1)
        self.y = self.dataset.loc[:, str(name_of_product)].values

    def splitDataSet (self, test_size, random_state):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = float(test_size), random_state = int(random_state))
    
    def estimateTimeDiff(self, befor, after):
        diff = after - befor
        if diff > 60:
            self.min = int(diff / 60)
            if self.min > 60:
                self.hr = int(min / 60)
                self.min = min % 60
            self.sec = int(diff % 60)
        else:
            self.sec = int(diff)