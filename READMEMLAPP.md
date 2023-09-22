Machine Learning Model Evaluator

Description
This Python script evaluates machine learning models for both regression and classification tasks.

Features
User-friendly input validation.
Data preprocessing and standardization.
Evaluation of regression and classification models.
Saving the best-performing model.

Usage
Run the script in a Python environment.
Specify the ML model type (regressor or classifier).
Provide the path or filename of the dataset in CSV format.
Follow on-screen prompts to enter target column information.
The script loads data, splits it, and standardizes features.
It identifies the type of dependent variable (categorical or continuous).
For regression tasks, it finds the best regressor model based on R-squared score.
Options include Linear Regression, LassoCV, Ridge, ElasticNet, and SVR.
For classification tasks, it finds the best classifier model based on accuracy.
Options include Logistic Regression, K-Nearest Neighbors (KNN), and Support Vector Classifier (SVC).
The script evaluates the selected model and displays performance metrics.
Optionally, you can save the best-performing model to a file using joblib.

Requirements
Python 3.x
numpy (imported as np)
pandas (imported as pd)
scikit-learn (sklearn) for machine learning libraries
joblib for model persistence

Note
Ensure that your dataset is in CSV format.
Follow the prompts to select the ML model type and target column name.
The script will handle data preprocessing, model selection, and evaluation.






