__author__ = 'piatskia'

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from numpy import genfromtxt
from sklearn import datasets
from sklearn.cross_validation import StratifiedKFold
from sklearn.externals.six.moves import xrange
from sklearn.mixture import GMM
from sklearn.linear_model import LogisticRegression

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB



def emm_class():

    em_classifier = GMM(n_components = np.unique(y_train).shape[0], n_iter=1000,  init_params='wc')
    em_classifier.fit(X_train)
    y_train_pred = em_classifier.predict(X_train)
    y_test_pred =  em_classifier.predict(X_test)
    train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    y_test_pred = em_classifier.predict(X_test)
    test_accuracy = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100

    print 'emm test accuracy:', test_accuracy

def log_reg_class():

    log_classifier = LogisticRegression(C=1.0, penalty='L2')
    log_classifier.fit(X_train, y_train)
    y_train_pred = log_classifier.predict(X_train)
    y_test_pred =  log_classifier.predict(X_test)
    train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    y_test_pred = log_classifier.predict(X_test)
    test_accuracy = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100

    print 'log reg test accuracy:', test_accuracy

def nb_class():
    nb_classifier = MultinomialNB(alpha=0.01)
    nb_classifier.fit(X_train, y_train)
    y_train_pred = nb_classifier.predict(X_train)
    y_test_pred =  nb_classifier.predict(X_test)
    train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    y_test_pred = nb_classifier.predict(X_test)
    test_accuracy = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100
    print 'multinomial naive bayes test accuracy:', test_accuracy



if __name__ == '__main__':
    fake_data = genfromtxt('fake_data.csv', delimiter=',')
    X_train = fake_data[0:20, :-1]
    X_test = fake_data[20:, :-1]
    y_train = fake_data[0:20,3]
    y_test = fake_data[20:, 3]
    emm_class()
    log_reg_class()
    nb_class()


