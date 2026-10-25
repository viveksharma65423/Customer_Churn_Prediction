Customer Churn Prediction 📊

Project Overview

This Machine Learning project predicts whether a telecom customer is likely to leave the company (churn) or continue using its services. The project includes data preprocessing, exploratory data analysis, classification models, model evaluation, and a Streamlit web application.

Objectives

- Analyze customer churn data.
- Perform data cleaning and preprocessing.
- Handle categorical features using encoding.
- Train and compare classification models.
- Evaluate model performance using classification metrics.
- Build an interactive Streamlit application for churn prediction.

Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Tuned Random Forest Classifier

Evaluation Metrics

The models are evaluated using:

- Accuracy
- Recall
- F1-score
- Confusion Matrix

Recall and F1-score are particularly useful for evaluating the detection of customers who are likely to churn.

Features

- Data exploration and preprocessing
- Missing-value and categorical-feature handling
- Model training and comparison
- Customer churn prediction
- Interactive web interface using Streamlit

Project Files

- "ProjectCV.ipynb" — Data analysis, preprocessing, model training, and evaluation.
- "app.py" — Streamlit web application.
- "customer_churn_model.pkl" — Saved trained model, if included.
- "requirements.txt" — Required Python libraries.

How to Run Locally

1. Clone or download this repository.

2. Install dependencies:
   
   pip install -r requirements.txt

3. Run the Streamlit app:
   
   streamlit run app.py

Disclaimer

Predictions are estimates based on the available dataset and model. They should not be treated as guaranteed outcomes.

Author

Machine Learning Project by Vivek Manoj Sharma
