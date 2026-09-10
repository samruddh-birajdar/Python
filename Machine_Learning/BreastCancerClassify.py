#==============================================================================================================================================================================
#
# Program      : Breast Cancer Classification
# Functions    : load_data(), preprocess_data(), perform_eda(), train_model(), evaluate_model(), main()
# Input        : Breast Cancer Wisconsin dataset (sklearn)
# Output       : Accuracy, Confusion Matrix, Classification Report
# Description  : Builds ML model to classify tumors as Malignant or Benign
# Author       : Samruddh Shivkumar Birajdar
#
#==============================================================================================================================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def load_data():
    dataset = load_breast_cancer()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    df['Target'] = dataset.target
    print("Dataset Loaded Successfully")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    return df

def preprocess_data(df):
    # Handle missing values
    df = df.dropna()
    # Scale features
    scaler = StandardScaler()
    X = scaler.fit_transform(df.drop('Target', axis=1))
    y = df['Target']
    return X, y

def perform_eda(df):
    print("Summary Statistics:\n", df.describe())
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.show()

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)
    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

def main():
    df = load_data()
    X, y = preprocess_data(df)
    perform_eda(df)
    model, X_test, y_test = train_model(X, y)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
