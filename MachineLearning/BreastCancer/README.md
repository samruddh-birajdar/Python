# Breast Cancer Classification Using Random Forest & Pipeline

An end-to-end machine learning project that predicts whether a breast cancer tumor is **Benign (2) or Malignant (4)** using the Breast Cancer Wisconsin dataset. The project demonstrates a structured machine learning workflow with automated preprocessing, model training, evaluation, visualization, and model persistence.

## Features

- **Data Preprocessing:** Handles missing values and converts features to numeric data types.
- **Machine Learning Pipeline:** Combines preprocessing and classification into a single Scikit-learn pipeline.
- **Missing Value Imputation:** Uses `SimpleImputer` with the median strategy.
- **Random Forest Classifier:** Trains an ensemble model with 300 decision trees.
- **Model Evaluation:** Measures accuracy and generates a confusion matrix and classification report.
- **Data Visualization:** Visualizes feature importance and the confusion matrix using Matplotlib.
- **Model Persistence:** Saves and loads trained models using Joblib for future predictions.

## Dataset

**Dataset:** Breast Cancer Wisconsin (Original)  
**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original)

The dataset contains nine predictive features and one target variable.

### Features

| Feature | Description |
|---|---|
| `ClumpThickness` | Thickness of cell clumps |
| `UniformityCellSize` | Uniformity of cell size |
| `UniformityCellShape` | Uniformity of cell shape |
| `MarginalAdhesion` | Marginal adhesion |
| `SingleEpithelialCellSize` | Size of single epithelial cells |
| `BareNuclei` | Bare nuclei |
| `BlandChromatin` | Bland chromatin |
| `NormalNucleoli` | Normal nucleoli |
| `Mitoses` | Mitoses |

### Target Classes

| Value | Diagnosis |
|---|---|
| `2` | Benign |
| `4` | Malignant |

The original dataset may contain missing values represented by `?`. These are converted to `NaN` and handled during preprocessing.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your GitHub repository URL and folder name.

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

## Project Structure

```text
Breast-Cancer-Classification/
│
├── breast_cancer_pipeline.py
├── breast-cancer-wisconsin.data
├── breast_cancer.csv
├── bc_rf_pipeline.joblib
└── README.md
```

**Note:** The CSV file and trained model are generated during execution, depending on how the script is implemented. The original dataset file must be available at the expected path.

## Machine Learning Workflow

### 1. Data Preparation

- Load the raw dataset.
- Assign column headers to the nine features and target.
- Replace `?` with `NaN`.
- Convert feature columns to numeric data types.
- Prepare the feature matrix (`X`) and target vector (`y`).

### 2. Train-Test Split

The dataset is divided into:

- **70% training data**
- **30% testing data**

Stratified sampling preserves the approximate distribution of benign and malignant cases in both sets.

### 3. Pipeline Construction

The Scikit-learn pipeline consists of two steps:

1. **SimpleImputer:** Replaces missing feature values using the median calculated from the training data.
2. **RandomForestClassifier:** Classifies tumors using an ensemble of 300 decision trees.

Using a pipeline ensures that preprocessing is fitted on the training data and applied consistently to test data and future predictions.

### 4. Model Training and Evaluation

The model is trained on the training dataset and evaluated on unseen test data using:

- Training accuracy
- Testing accuracy
- Confusion matrix
- Classification report, including precision, recall, and F1-score

### 5. Visualization

The project generates:

- **Feature Importance Plot:** Highlights the features that contribute most to the Random Forest model's predictions.
- **Confusion Matrix:** Shows correct and incorrect classifications for each target class.

### 6. Model Saving and Loading

The trained pipeline is saved to a Joblib file:

```text
bc_rf_pipeline.joblib
```

It can be loaded later to make predictions without retraining the model.

## Running the Project

### Step 1: Prepare the Dataset

If the script provides a `data_file_to_csv()` function, run it once to convert the raw dataset into a CSV file:

```python
from breast_cancer_pipeline import data_file_to_csv

data_file_to_csv()
```

Ensure that the raw dataset is present in the expected location before running this step.

### Step 2: Train and Evaluate the Model

Run the main Python script:

```bash
python breast_cancer_pipeline.py
```

The script should train the pipeline, evaluate its performance, display the visualizations, and save the trained model.

### Expected Output

The following values are illustrative; actual results may vary depending on the dataset, preprocessing, train-test split, and model configuration.

```text
Train Accuracy :: 1.0
Test Accuracy :: 0.97

Classification Report:
              precision    recall    f1-score    support
              ...

Confusion Matrix:
[[...]]

Model saved to bc_rf_pipeline.joblib
Loaded model prediction for first test sample: 2
```

## Making Predictions

After training, load the saved model and use it to predict the diagnosis of a sample.

```python
import pandas as pd
from breast_cancer_pipeline import load_model

model = load_model("bc_rf_pipeline.joblib")

sample = pd.DataFrame([{
    "ClumpThickness": 5,
    "UniformityCellSize": 1,
    "UniformityCellShape": 1,
    "MarginalAdhesion": 1,
    "SingleEpithelialCellSize": 2,
    "BareNuclei": 1,
    "BlandChromatin": 3,
    "NormalNucleoli": 1,
    "Mitoses": 1
}])

prediction = model.predict(sample)

print("Prediction:", prediction[0])
```

The sample values above are illustrative inputs for demonstrating the prediction workflow, not a medical assessment.

**Prediction labels:**
- `2` — Benign
- `4` — Malignant

The input DataFrame must contain the same feature names and compatible data types used during model training.

## Loading the Saved Model

To load the trained pipeline independently:

```python
from breast_cancer_pipeline import load_model

model = load_model("bc_rf_pipeline.joblib")
```

The loaded pipeline can be used directly with new input data, provided the expected features are supplied.

## Key Learning Outcomes

This project demonstrates practical machine learning concepts, including:

- Data cleaning and missing value handling
- Train-test splitting and stratified sampling
- Scikit-learn pipelines
- Random Forest classification
- Model evaluation using classification metrics
- Feature importance and confusion matrix visualization
- Saving and reusing trained machine learning models

## Future Improvements

- Add cross-validation for more reliable performance estimates.
- Tune hyperparameters using `GridSearchCV` or `RandomizedSearchCV`.
- Compare Random Forest with Logistic Regression, SVM, and other classifiers.
- Add a prediction interface using Streamlit or FastAPI.
- Track recall, precision, and ROC-AUC alongside accuracy.
- Add automated tests and a reproducible dependency file.

## Disclaimer

This project is intended for educational and research purposes only. It is not a medical diagnostic tool and must not be used to make clinical decisions.

## License

Add a license file if you intend to distribute or reuse this project publicly.
