#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
from ModellService import ModellService
from ModellUI import ModellUI
from ModellResultUI import ModellResultUI
import ModellValue
import numpy as np


# Coordinates other tools and determines which model to use based on data from the user interface
class ModellWerkzeug():
    def __init__(self):

        self.UI = ModelUI()
        self.prediction_vector = []
        self.creatingOfPredictionVector()
        self.MS = ModelService(str(ModellValue.CSV_db), str(ModellValue.CSV_head), float(ModellValue.enter_test_size),
                               int(ModellValue.enter_random_state), str(ModellValue.enter_produkt),
                               str(ModellValue.enter_typ_model), self.prediction_vector)
        ModelResultUI()

    def set_list_index (self, list, index, value):
        try:
            list[index] = value
        except IndexError:
            for x in range(index - len(list) + 1):
                list.append(0)
                list[index] = value


    #converts the entered data from the user interface into vector
    def creatingOfPredictionVector(self):

        self.prediction_vector.append(int(ModellValue.enter_age_value))

        if ModellValue.enter_index_new_customer_value == "New":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)
        self.prediction_vector.append(int(ModellValue.enter_seniority))
        self.prediction_vector.append(int(ModellValue.enter_primary_index_value))

        self.prediction_vector.append(ModellValue.enter_Last_date_prime)
        if ModellValue.enter_type_adresse_value == "Primary":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)

        if ModellValue.enter_index_activity_value == "Activ":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)
        
        self.prediction_vector.append(int(ModellValue.enter_Income_value))

        self.prediction_vector.append(int(ModellValue.enter_Month_of_transaction_value))
        
        if ModellValue.enter_employee_value == "Employee":
            self.prediction_vector.extend([1, 0, 0, 0, 0])
        elif ModellValue.enter_employee_value == "Ex-Employee":
            self.prediction_vector.extend([0, 1, 0, 0, 0])
        elif ModellValue.enter_employee_value == "Firm":
            self.prediction_vector.extend([0, 0, 1, 0, 0])
        elif ModellValue.enter_employee_value == "Not_Employee":
            self.prediction_vector.extend([0, 0, 0, 1, 0])
        elif ModellValue.enter_employee_value == "Passiv_Employee":
            self.prediction_vector.extend([0, 0, 0, 0, 1])
        if ModellValue.enter_country_value == "BO":
            self.prediction_vector.extend([1, 0, 0, 0, 0])
        elif ModellValue.enter_country_value == "DE":
            self.prediction_vector.extend([0, 1, 0, 0, 0])
        elif ModellValue.enter_country_value == "ES":
            self.prediction_vector.extend([0, 0, 1, 0, 0])
        elif ModellValue.enter_country_value == "IT":
            self.prediction_vector.extend([0, 0, 0, 1, 0])
        elif ModellValue.enter_country_value == "PY":
            self.prediction_vector.extend([0, 0, 0, 0, 1])
        
        if ModellValue.enter_sex_value == "Man":
            self.prediction_vector.extend([1, 0])
        else:
            self.prediction_vector.extend([0, 1])
        
        dummy_list = []
        length = len(self.UI.list_Indrel)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Indrel.index(ModellValue.enter_indrel_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Relationships)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Relationships.index(ModellValue.enter_relationship_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Type_of_country)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Type_of_country.index(ModellValue.enter_type_country_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Type_of_homecountry)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Type_of_homecountry.index(ModellValue.enter_type_home_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Canal)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Canal.index(ModellValue.enter_canal_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Region)
        for x in range(0, length-1):
            dummy_list.append(0)
        index_element = self.UI.list_Region.index(ModellValue.enter_region_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Segment)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Segment.index(ModellValue.enter_segment_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        self.prediction_vector = np.transpose(np.array(list(zip(self.prediction_vector, self.prediction_vector))))

    def setNewValues (self):
        self.trainAccuracy = ModellValue.trainAccuracy
        self.testAccuracy = ModellValue.testAccuracy
        self.confusionMatrix = ModellValue.confusionMatrix
        self.crossValidation = ModellValue.crossValidation
        print(str(self.trainAccuracy), str(self.crossValidation))