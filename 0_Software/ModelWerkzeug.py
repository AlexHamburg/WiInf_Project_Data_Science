#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""
from ModelService import ModelService
from ModelUI import ModelUI
from ModelResultUI import ModelResultUI
import ModelValue
import numpy as np
from ObserverPattern import Observer

class ModelWerkzeug():
    def __init__(self):

        self.UI = ModelUI()
        self.prediction_vector = []
        self.creatingOfPredictionVector()
        self.MS = ModelService(str(ModelValue.CSV_db), str(ModelValue.CSV_head), float(ModelValue.enter_test_size),
                     int(ModelValue.enter_random_state), str(ModelValue.enter_produkt),
                     str(ModelValue.enter_typ_model), self.prediction_vector)

        ModelResultUI()

    def set_list_index (self, list, index, value):
        try:
            list[index] = value
        except IndexError:
            for x in range(index - len(list) + 1):
                list.append(0)
                list[index] = value
    
    def creatingOfPredictionVector(self):

        self.prediction_vector.append(int(ModelValue.enter_age_value))

        if ModelValue.enter_index_new_customer_value == "New":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)
        self.prediction_vector.append(int(ModelValue.enter_seniority))
        self.prediction_vector.append(int(ModelValue.enter_primary_index_value))

        self.prediction_vector.append(ModelValue.enter_Last_date_prime)
        if ModelValue.enter_type_adresse_value == "Primary":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)

        if ModelValue.enter_index_activity_value == "Activ":
            self.prediction_vector.append(1)
        else:
            self.prediction_vector.append(0)
        
        self.prediction_vector.append(int(ModelValue.enter_Income_value))

        self.prediction_vector.append(int(ModelValue.enter_Month_of_transaction_value))
        
        if ModelValue.enter_employee_value == "Employee":
            self.prediction_vector.extend([1, 0, 0, 0, 0])
        elif ModelValue.enter_employee_value == "Ex-Employee":
            self.prediction_vector.extend([0, 1, 0, 0, 0])
        elif ModelValue.enter_employee_value == "Firm":
            self.prediction_vector.extend([0, 0, 1, 0, 0])
        elif ModelValue.enter_employee_value == "Not_Employee":
            self.prediction_vector.extend([0, 0, 0, 1, 0])
        elif ModelValue.enter_employee_value == "Passiv_Employee":
            self.prediction_vector.extend([0, 0, 0, 0, 1])
        if ModelValue.enter_country_value == "BO":
            self.prediction_vector.extend([1, 0, 0, 0, 0])
        elif ModelValue.enter_country_value == "DE":
            self.prediction_vector.extend([0, 1, 0, 0, 0])
        elif ModelValue.enter_country_value == "ES":
            self.prediction_vector.extend([0, 0, 1, 0, 0])
        elif ModelValue.enter_country_value == "IT":
            self.prediction_vector.extend([0, 0, 0, 1, 0])
        elif ModelValue.enter_country_value == "PY":
            self.prediction_vector.extend([0, 0, 0, 0, 1])
        
        if ModelValue.enter_sex_value == "Man":
            self.prediction_vector.extend([1, 0])
        else:
            self.prediction_vector.extend([0, 1])
        
        dummy_list = []
        length = len(self.UI.list_Indrel)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Indrel.index(ModelValue.enter_indrel_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Relationships)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Relationships.index(ModelValue.enter_relationship_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Type_of_country)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Type_of_country.index(ModelValue.enter_type_country_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Type_of_homecountry)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Type_of_homecountry.index(ModelValue.enter_type_home_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Canal)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Canal.index(ModelValue.enter_canal_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Region)
        for x in range(0, length-1):
            dummy_list.append(0)
        index_element = self.UI.list_Region.index(ModelValue.enter_region_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        dummy_list.clear()
        length = len(self.UI.list_Segment)
        for x in range(0, length):
            dummy_list.append(0)
        index_element = self.UI.list_Segment.index(ModelValue.enter_segment_value)
        self.set_list_index(dummy_list, index_element, 1)
        self.prediction_vector.extend(dummy_list)

        self.prediction_vector = np.transpose(np.array(list(zip(self.prediction_vector, self.prediction_vector))))

    def setNewValues (self):
        self.trainAccuracy = ModelValue.trainAccuracy
        self.testAccuracy = ModelValue.testAccuracy
        self.confusionMatrix = ModelValue.confusionMatrix
        self.crossValidation = ModelValue.crossValidation
        print(str(self.trainAccuracy), str(self.crossValidation))