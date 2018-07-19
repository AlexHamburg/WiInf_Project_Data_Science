#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 22:08:31 2018

@author: Kim, Eric, Oleksandr
"""

# Required Python Packages
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
import pydot
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import cross_val_score
import ModelValue

class ModelRandomForestService ():
    def __init__(self, train_features, train_target, test_feature, test_target, model_type, features, prediction_vector):
        if model_type is "Random_Forest":
            self.gridSearchRandomForest(RandomForestClassifier(), train_features, train_target)
        else:
            self.randomizedSearchCVRandomForest(RandomForestClassifier(), train_features, train_target)
                   
        self.randomForestClassifier(train_features, train_target, test_feature, prediction_vector, self.best_param["n_estimators"],
                                    self.best_param["max_features"],
                                    self.best_param["max_depth"], self.best_param["bootstrap"])
        self.visualisationRandomForest(self.classifier, 3, features)
        self.errorAndAccuracy( train_features, train_target, test_target, self.prediction_test, self.prediction_train)

    def randomForestClassifier(self, train_features, train_target, test_features, prediction_vector, number_of_trees, max_features, max_depth, bootstrap):
        if number_of_trees == None:
            number_of_trees = 30
        if max_features == None:
            max_features = 'auto'
        if max_depth == None:
            max_depth = 15
        if bootstrap == None:
            bootstrap = True

        self.classifier = RandomForestClassifier(criterion = 'entropy', n_estimators = int(number_of_trees), max_features = max_features,
                                                 max_depth = int(max_depth), bootstrap = bool(bootstrap))
        self.classifier.fit(train_features, train_target)
        self.prediction_train = self.classifier.predict(train_features)
        self.prediction_test = self.classifier.predict(test_features)
        self.prediction_product = self.classifier.predict(prediction_vector)
        if self.prediction_product[0] == 0:
            ModelValue.prediktionResult = "will buy"
        elif  self.prediction_product[1] == 1:
            ModelValue.prediktionResult = "will not buy"

    def gridSearchRandomForest (self, classifier, train_features, train_target):
        parameters = [{'n_estimators': [15], 'max_features': [15, 20, 25, 30, 35, 'auto', 'sqrt', 'log2'], 'max_depth': [15, 20, 25], 'bootstrap': [True, False]},
                      {'n_estimators': [20], 'max_features': [15, 20, 25, 30, 35, 'auto', 'sqrt', 'log2'], 'max_depth': [15, 20, 25], 'bootstrap': [True, False]},
                      {'n_estimators': [25], 'max_features': [15, 20, 25, 30, 35, 'auto', 'sqrt', 'log2'], 'max_depth': [15, 20, 25], 'bootstrap': [True, False]},
                      {'n_estimators': [30], 'max_features': [15, 20, 25, 30, 35, 'auto', 'sqrt', 'log2'], 'max_depth': [15, 20, 25], 'bootstrap': [True, False]}]

        grid_search = GridSearchCV(estimator = classifier, param_grid = parameters, scoring = 'accuracy', cv = 10, n_jobs = -1)
        grid_search = grid_search.fit(train_features, train_target)
        self.best_accuracy = grid_search.best_score_
        self.best_param = grid_search.best_params_

    def randomizedSearchCVRandomForest (self, classifier, train_features, train_target):
        # Number of trees in random forest
        n_estimators = [int(x) for x in np.linspace(start = 10, stop = 100, num = 10)]
        # Number of features to consider at every split
        max_features = [20, 25, 35, 'auto', 'sqrt', 'log2']
        # Maximum number of levels in tree
        max_depth = [int(x) for x in np.linspace(10, 50, num = 11)]
        max_depth.append(None)
        # Minimum number of samples required to split a node
        min_samples_split = [2, 5, 10, 20, 50]
        # Minimum number of samples required at each leaf node
        min_samples_leaf = [1, 2, 4, 5, 9, 12, 15]
        # Method of selecting samples for training each tree
        bootstrap = [True, False]
        #Check how many time does random_grid need
        random_grid = {'n_estimators': n_estimators, 'max_features': max_features, 'max_depth': max_depth,
                       'min_samples_split': min_samples_split, 'min_samples_leaf': min_samples_leaf, 'bootstrap': bootstrap}
        random_search = RandomizedSearchCV(estimator = classifier, param_distributions = random_grid, n_iter = 100, cv = 10, n_jobs = -1)
        # Fit the random search model
        random_search.fit(train_features, train_target)
        self.best_accuracy = random_search.best_score_
        self.best_param = random_search.best_params_

    def visualisationRandomForest (self, classifier, num_of_trees, features):
        # Pull out one tree from the forest
        tree = classifier.estimators_[num_of_trees]
        # Export the image to a dot file
        X_train_list = list(features.columns.values)
        export_graphviz(tree, out_file = 'tree.dot', feature_names = X_train_list, rounded = True, max_depth = 5)
        # Use dot file to create a graph
        (graph, ) = pydot.graph_from_dot_file('tree.dot')
        # Write graph to a png file
        graph.write_png('tree2.jpg')

    def errorAndAccuracy(self, train_features, train_target, test_target, prediction_test, prediction_train):
        # cross validation
        accuracies = cross_val_score(estimator=self.classifier, X=train_features, y=train_target, cv=10, n_jobs=-1)
        k_Fold_accur = accuracies.mean()
        variance = abs(accuracies.std())
        ModelValue.trainAccuracy = accuracy_score(train_target, prediction_train)
        ModelValue.testAccuracy = accuracy_score(test_target, prediction_test)
        ModelValue.confusionMatrix = confusion_matrix(test_target, prediction_test)
        ModelValue.crossValidation = "Mean accuracy (train) :: %s \nVariance :: %s" %(str(k_Fold_accur), str(variance))