import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import (
    LinearRegression, LassoCV, Ridge, ElasticNet, LogisticRegression
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVR, SVC
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    accuracy_score, classification_report
)
from sklearn.metrics import ConfusionMatrixDisplay
import joblib

# Define a class for model evaluation
class Evaluator:
    def __init__(self, model_type, file_path):
        """
        Initialize the Evaluator class.

        Parameters:
        - model_type (str): Type of the ML model (regressor or classifier).
        - file_path (str): Path to the CSV file containing the dataset.
        """
        self.model_type = model_type
        self.file_path = file_path
        self.df = None
        self.target_col = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        self.dependent_value = None

    # Load data from a CSV file
    def load_data(self):
        """
        Load the dataset from a CSV file specified by file_path.
        """
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("File not found. Please provide a valid CSV file.")
            exit(1)

    # Get user input for model selection and target column
    def get_user_input(self):
        """
        Get user input for model selection (regressor or classifier) and
        the name of the dependent target column.
        """
        print(f"What ML model would you like to use? (regressor or classifier): ")
        self.target_col = input("Enter the name of the dependent target: ")
        if self.target_col not in self.df.columns:
            error_message = f"'{self.target_col}' is not a valid target column. Please choose a column from the dataset."
            print(error_message)
            raise ValueError(error_message)  
        self.X = self.df.drop(self.target_col, axis=1)
        self.y = self.df[self.target_col]

    # Prepare the data for model training and testing
    def prepare_data(self):
        """
        Split the dataset into training and testing sets and perform
        standardization on the features.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=101)
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

    # Determine if the dependent variable is categorical or continuous
    def validate_dependent_value(self):
        """
        Determine if the dependent variable is categorical or continuous based on its dtype.
        """
        if self.y.dtype == "object":
            self.dependent_value = "categorical"
        else:
            self.dependent_value = "continuous"

    # Evaluate a machine learning model
    def evaluate_model(self, model):
        """
        Evaluate a machine learning model using appropriate metrics
        based on the type of dependent variable.

        Parameters:
        - model: The machine learning model to be evaluated.
        """
        print(f"{model} Model:")
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        if self.dependent_value == "continuous":
            mae = mean_absolute_error(self.y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
            r2 = r2_score(self.y_test, y_pred)
            print(f"MAE: {mae}")
            print(f"RMSE: {rmse}")
            print(f"R2 Score: {r2}")
        else:
            print(f"Classification Report:")
            print(classification_report(self.y_test, y_pred))
            print(f"Confusion Matrix:")
            confusion_matrix_plot = ConfusionMatrixDisplay.from_estimator(model, self.X_test, self.y_test)

    # Find the best regressor model
    def find_best_regressor_model(self):
        """
        Find the best regressor model among a set of regression models
        based on R-squared score.

        Returns:
        - best_model: The best performing regression model.
        - best_score: The R-squared score of the best model.
        """
        models = {
            "Linear Regression": LinearRegression(),
            "Lasso": LassoCV(),
            "Ridge": Ridge(),
            "ElasticNet": ElasticNet(),
            "Support Vector Regression": SVR(),
        }

        best_score = -float("inf")
        best_model = None

        for name, model in models.items():
            model.fit(self.X_train, self.y_train)
            y_pred = model.predict(self.X_test)
            score = r2_score(self.y_test, y_pred)
            if score > best_score:
                best_score = score
                best_model = model  

        return best_model, best_score
    
    # Find the best classifier model
    def find_best_classifier_model(self):
        """
        Find the best classifier model among a set of classification models
        based on accuracy score.

        Returns:
        - best_model: The best performing classification model.
        - best_score: The accuracy score of the best model.
        """
        models = {
            "Logistic Regression": LogisticRegression(),
            "KNN": KNeighborsClassifier(),
            "SVC": SVC(),
        }

        best_score = -float("inf")
        best_model = None

        for name, model in models.items():
            model.fit(self.X_train, self.y_train)
            y_pred = model.predict(self.X_test)
            score = accuracy_score(self.y_test, y_pred)
            if score > best_score:
                best_score = score
                best_model = model  

        return best_model, best_score

    # Save the best model to a file
    def save_best_model(self, best_model):
        """
        Save the best model to a file using joblib.

        Parameters:
        - best_model: The best performing machine learning model.
        """
        save_model = input("Do you want to save the best model? (y/n) ")
        if save_model.lower() == 'y':
            file_name = input("Enter the file name: ")
            joblib.dump(best_model, file_name)
            print("Model saved successfully!")
        else:
            print("Model not saved.")

# Main script execution
if __name__ == "__main__":
    model_type = input("What ML model would you like to use? (regressor or classifier): ")
    file_path = input("Enter the path and/or filename of the .csv file: ")

    model_evaluator = Evaluator(model_type, file_path)
    model_evaluator.load_data()
    model_evaluator.get_user_input()
    model_evaluator.prepare_data()
    model_evaluator.validate_dependent_value()

    if model_type == "regressor":
        best_model, best_score = model_evaluator.find_best_regressor_model()
    else:
        best_model, best_score = model_evaluator.find_best_classifier_model()

    if model_evaluator.dependent_value == "categorical" and model_type == "regressor":
        print("Data is not ready for machine learning. Missing data in columns:", model_evaluator.df.columns[model_evaluator.df.isnull().any()])
    else:
        model_evaluator.evaluate_model(best_model)

        print(f"The Best Model for this data is:", best_model.__class__.__name__)
        print(f"The best performing score is:", best_score)

        model_evaluator.save_best_model(best_model)
