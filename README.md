# Salary Prediction
End-to-End project I made as a machine learning intern @ Mentorness
Steps performed: 
1. ### Data Preprocessing:
   - Handled duplicate and missing values (imputed them).
   - Performed Feature Engineering: utilized DOJ and CURRENT DATE to calculate current experience in terms of years.
2. ### Model Comparison Notebook Description

   This notebook details a systematic approach to comparing multiple regression models for optimal performance. Key steps include:

   a. **Data Preprocessing**
      - **Encoding**: Ordinal Encoding for ordered categories and Label Encoding for unordered categories.
      - **Train-Test Split**: Divided data for evaluation.
   
   b. **Feature Engineering**
      - **Feature Selection**: Used SelectKBest for selecting relevant features.
   
   c. **Model Training**
      - Trained models including Linear Regression, Ridge, Lasso, Gradient Boosting, XGBoost, SVR, and KNN Regression. 
   
   d. **Model Evaluation**
      - Metrics: Evaluated using MAE, MSE, RMSE, and R² score.
      - Visualization: Plotted metrics for comparison.
   
   e. **Performance Comparison**
      - Used a custom scorer and train test comparison function for consistent evaluation.
      - Analyzed results to determine the best model.
   
   You can find the full notebook and code [here](https://github.com/sanhiitaa/salary-prediction/blob/main/salary_prediction_model_comparison.ipynb).
