# Salary Prediction
   - An end-to-end data science project I made as a machine learning intern @ Mentorness.
   - This project predicts employee salaries using advanced regression techniques and thorough data preprocessing. We compare multiple machine learning models to select the best-performing one, which is then integrated into a pipeline. This pipeline includes all necessary preprocessing steps, ensuring accurate predictions and easy deployment.
   - **You can find the web app [here](https://salary-prediction-1806.streamlit.app/).**

Steps performed: 
## 1. Exploratory Data Analysis
   - Gender Distribution: More females than males.
   - Unit Distribution: Most employees are in the `IT` department.
   - Designation Distribution: A significantly large population of analysts.
   - Age Trend: Older employees tend to have higher salaries.
   - Experience Trend: Higher experience correlates with higher salaries.
   - Notebook link [here](https://github.com/sanhiitaa/salary-prediction/blob/main/salary_prediction_EDA.ipynb)
  
## 2. Data Preprocessing
   - **Encoding**: Ordinal Encoding for ordered categories and Label Encoding for unordered categories.
   - Dropped duplicates.
   - Checked for null values.
   - Imputed `DOJ`, `AGE`, and `RATINGS` columns with mode.
   - Imputed `LEAVES USED`, `LEAVES REMAINING` columns with median.
   - Dropped `FIRST NAME`, `LAST NAME` columns.
   - Notebook link [here](https://github.com/sanhiitaa/salary-prediction/blob/main/salary_prediction_data_processing.ipynb)

## 3. **Feature Engineering**
   - Converted DOJ and CURRENT DATE columns to datetime datatype.
   - Created a new feature: years_experience.
   - Dropped date columns.

## 4. **Feature Selection**:
   - Used SelectKBest to select best features.
   - Extracted selected feature names: `SEX`, `DESIGNATION`, `AGE`, `UNIT`, `PAST EXP`, `years_experience`.
   - Reassigned selected features to training and test datasets.
   - Conducted correlation study and dropped columns with correlation exceeding [-0.8, 0.8].

## 5. **Model Training and Evaluation**
   - **Trained models**: Linear Regression, Ridge, Lasso, Gradient Boosting, XGBoost, SVR, and KNN Regression. 
   - **Metrics**: Evaluated using MAE, MSE, RMSE, and R² score.
   - **Visualization**: Plotted metrics for comparison.

## 6. **Performance Comparison**
   - Used a custom scorer and train test comparison function for consistent evaluation.
   - Analyzed results to determine the best model.

## 7. **Model Selection**
   - Selected Gradient Boosting Regression as the best-performing model with an R2 score of `0.9495` for final pipeline integration.
   - Notebook link [here](https://github.com/sanhiitaa/salary-prediction/blob/main/salary_prediction_model_comparison.ipynb)

## 7. **Hyperparameter Tuning**
   - Conducted hyperparameter tuning using RandomizedSearchCV to optimize the Gradient Boosting Regressor.
   - Tuned hyperparameters such as `n_estimators`, `learning_rate`, `max_depth`, `min_samples_split`, `min_samples_leaf`, and `subsample`.

## 8. **Pipeline Building**
   - Built a preprocessing pipeline using ColumnTransformer to handle different types of categorical encoding (ordinal and nominal).
   - Integrated SelectKBest for feature selection within the pipeline to automatically choose the most relevant features.
   - Incorporated the best-performing model, Gradient Boosting Regressor, into the pipeline.
   - Configured the final pipeline to include all preprocessing steps, feature selection, and the regression model for seamless integration and deployment.
   - Ensured that the entire pipeline, including preprocessing and model training, could be saved and reused efficiently.
   - Notebook link [here](https://github.com/sanhiitaa/salary-prediction/blob/main/salary_prediction_final_pipeline.ipynb)

### 9. **Web Application Deployment**
   - Developed a web application using Streamlit for  easy and interactive salary prediction.
   - Created a user-friendly interface for inputting employee information and obtaining salary predictions.
   - Deployed the application using Streamlit's built-in sharing platform.
   - Included a `requirements.txt` file to ensure easy replication of the development environment for deployment.
   - App file [link](https://github.com/sanhiitaa/salary-prediction/blob/main/app-files/app.py)
     
## Thank you for taking the time to check this project out!
