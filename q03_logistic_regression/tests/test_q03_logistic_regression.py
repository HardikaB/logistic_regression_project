# Default Imports
import pandas as pd
import numpy
from unittest import TestCase
from greyatomlib.logistic_regression_project.q02_data_cleaning_all.build import data_cleaning
from greyatomlib.logistic_regression_project.q02_data_cleaning_all_2.build import data_cleaning_2
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal
from ..build import logistic_regression
from inspect import getfullargspec
loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)
X, y, X_train, X_test, y_train, y_test = data_cleaning(loan_data)
X_train, X_test, y_train, y_test = data_cleaning_2(X_train, X_test, y_train, y_test)
cm = logistic_regression(X_train, X_test, y_train, y_test)

class TestLogistic_regression(TestCase):
    def test_logistic_regression_arguments(self):

        # Input parameters tests
        args = getfullargspec(logistic_regression)
        self.assertEqual(len(args[0]), 4, "Expected arguments %d, Given %d" % (4, len(args[0])))
    def test_logistic_regression_defaults(self):
        args = getfullargspec(logistic_regression)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
    def test_logistic_regression_return_data_type(self):  
        self.assertIsInstance(cm, numpy.ndarray,
                              "Expected data type for return value is `numpy.ndarray`, you are returning %s" % (
                                  type(cm)))

        # Return value tests
    def test_logistic_regression_return_value(self):
        self.assertEqual(cm.max(), 94, "Expected return value does not given return value")
