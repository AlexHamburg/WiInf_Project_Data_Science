#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# Model SVM (ready but not deployed)
class ModellSVMService:
    def __init__ (self, train_features, train_target, test_features, prediction_vector):
        #Global Variables
        self.classifier
        self.prediction_train
        self.prediction_test
        self.best_accuracy
        self.best_param
        self.X_train
        self.X_test
        self.X_prediction
        self.prediction_product

        self.skalingOfData(train_features, prediction_vector, test_features)
        self.gridSearchSVM(SVC(), train_features, train_target)
        if self.best_param['kernel'] is 'linear':
            self.kernelSVMLinear(self.X_train, train_target, self.best_param['C'])
        elif self.best_param['kernel'] is 'poly':
            self.kernelSVMPoly(self.X_train, train_target, self.best_param['C'], self.best_param['gamma'], self.best_param['degree'])
        else:
            self.kernelSVM(self.X_train, train_target, self.best_param['C'], self.best_param['kernel'], self.best_param['gamma'])
        self.kernelSVMPrediction(self.X_train, self.X_test, self.X_prediction)
        

    def kernelSVMPrediction (self, train_features, test_features, prediction_vector):
        self.classifier.fit(train_features, prediction_vector)
        self.prediction_product = self.classifier.predict(prediction_vector)
        self.prediction_test = self.classifier.predict(test_features)
        
    def kernelSVM (self, train_features, train_target, c_param, kernel_param, gamma_param):
        self.classifier = SVC(c = c_param, kernel = str(kernel_param), random_state = 100)
        self.classifier.fit(train_features, train_target)
        self.prediction = self.classifier.predict(train_features)
    
    def kernelSVMLinear (self, train_features, train_target, c_param):
        self.classifier = SVC(c = c_param, kernel = 'linear', random_state = 100)
        self.classifier.fit(train_features, train_target)
        self.prediction = self.classifier.predict(train_features)
        
    def kernelSVMPoly (self, train_features, train_target, c_param, gamma_param, degree_param):
        self.classifier = SVC(c = c_param, kernel = 'poly', random_state = 100)
        self.classifier.fit(train_features, train_target)
        self.prediction_train = self.classifier.predict(train_features)

    def gridSearchSVM (self, classifier, train_features, train_target):
        parameters = [{'C': [1, 10], 'kernel': ['rbf'], 'gamma': [0.5, 0.1, 0.01, 0.001, 0.0001]}, 
                      {'C': [1, 10], 'kernel': ['linear']}, 
                      {'C': [1, 10], 'kernel': ['poly'], 'degree': [3, 4, 5, 6, 7], 'gamma': [0.5, 0.1, 0.01, 0.001, 0.0001]}, 
                      {'C': [1, 10], 'kernel': ['sigmoid'], 'gamma': [0.5, 0.1, 0.01, 0.001, 0.0001]}]
        grid_search = GridSearchCV (estimator = classifier, param_grid = parameters, scoring = 'accuracy', cv = 10, n_jobs = -1)
        grid_search = grid_search.fit(train_features, train_target)
        self.best_accuracy = grid_search.best_score_
        self.best_param = grid_search.best_params_
    
    def skalingOfData (self, train_features, prediction_vector, test_features):
        sc_X = StandardScaler()
        self.X_train = sc_X.fit_transform(train_features)
        self.X_test = sc_X.fit_transform(test_features)
        self.X_prediction = sc_X.transform(prediction_vector)