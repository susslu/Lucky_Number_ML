import unittest
from unittest.mock import patch
import pandas as pd
from ML_App import Evaluator

class TestEvaluator(unittest.TestCase):
    @patch('builtins.input', side_effect=["sales", "Advertising.csv", "regressor"])
    def test_evaluate_regressor(self, mock_input):
        # Test for evaluating a regressor model

        # Instantiate the Evaluator and load data
        self.evaluator = Evaluator("regressor", "Advertising.csv")
        self.evaluator.load_data()  # Call load_data to initialize self.df
    
        # Mock user input for the model type and target column
        self.evaluator.get_user_input()

        # Assertions to check the expected output
        self.assertEqual(self.evaluator.model_type, "regressor")
        self.assertEqual(self.evaluator.file_path, "Advertising.csv")
        self.assertEqual(self.evaluator.target_col, "sales")

    @patch('builtins.input', side_effect=["test_result", "hearing_test.csv", "classifier"])
    def test_evaluate_classifier(self, mock_input):
        # Test for evaluating a classifier model

        # Instantiate the Evaluator and load data
        evaluator = Evaluator("classifier", "hearing_test.csv")
        evaluator.load_data()
    
        # Mock user input for the model type and target column
        evaluator.get_user_input()

        # Assertions to check the expected output
        self.assertEqual(evaluator.model_type, "classifier")
        self.assertEqual(evaluator.file_path, "hearing_test.csv")
        self.assertEqual(evaluator.target_col, "test_result")

    def test_load_data(self):
        # Test for loading data

        # Instantiate the Evaluator
        evaluator = Evaluator("regressor", "Advertising.csv")

        # Load data
        evaluator.load_data()

        # Check if data is loaded as a DataFrame
        self.assertIsInstance(evaluator.df, pd.DataFrame)

    @patch('builtins.input', side_effect=["sales", "Advertising.csv", "regressor"])
    def test_prepare_data(self, mock_input):
        # Test for preparing data for a regressor model

        # Instantiate the Evaluator and load data
        evaluator = Evaluator("regressor", "Advertising.csv")
        evaluator.load_data()

        # Mock user input for the target column
        evaluator.get_user_input()

        # Prepare data
        evaluator.prepare_data()

        # Assertions to check the expected output
        self.assertIsNotNone(evaluator.X_train)
        self.assertIsNotNone(evaluator.X_test)
        self.assertIsNotNone(evaluator.y_train)
        self.assertIsNotNone(evaluator.y_test)

    @patch('builtins.input', side_effect=["sales", "Advertising.csv", "regressor"])
    def test_validate_dependent_value(self, mock_input):
        # Test for validating the dependent value type

        # Instantiate the Evaluator and load data
        evaluator = Evaluator("regressor", "Advertising.csv")
        evaluator.load_data()

        # Mock user input for the target column
        evaluator.get_user_input()

        # Validate dependent value
        evaluator.validate_dependent_value()

        # Assertions to check the expected output
        self.assertEqual(evaluator.dependent_value, "continuous")  # Expecting continuous as 'sales' is numeric

    @patch('builtins.input', side_effect=["sales", "Advertising.csv", "regressor"])
    def test_find_best_regressor_model(self, mock_input):
        # Test for finding the best regressor model

        # Instantiate the Evaluator and load data
        evaluator = Evaluator("regressor", "Advertising.csv")
        evaluator.load_data()

        # Mock user input for the target column
        evaluator.get_user_input()

        # Prepare data
        evaluator.prepare_data()

        # Find the best regressor model
        best_model, best_score = evaluator.find_best_regressor_model()

        # Assertions to check the expected output
        self.assertIsNotNone(best_model)
        self.assertIsNotNone(best_score)

    @patch('builtins.input', side_effect=["test_result", "hearing_test.csv", "classifier"])
    def test_find_best_classifier_model(self, mock_input):
        # Test for finding the best classifier model

        # Instantiate the Evaluator and load data
        evaluator = Evaluator("classifier", "hearing_test.csv")
        evaluator.load_data()

        # Mock user input for the target column
        evaluator.get_user_input()

        # Prepare data
        evaluator.prepare_data()  # Call prepare_data here

        # Check data preparation
        self.assertIsNotNone(evaluator.X_train)
        self.assertIsNotNone(evaluator.X_test)
        self.assertIsNotNone(evaluator.y_train)
        self.assertIsNotNone(evaluator.y_test)

        # Find the best classifier model
        best_model, best_score = evaluator.find_best_classifier_model()

        # Assertions to check the expected output
        self.assertIsNotNone(best_model)
        self.assertIsNotNone(best_score)

if __name__ == '__main__':
    unittest.main()
