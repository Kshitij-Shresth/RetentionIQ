# RetentionIQ
Employee attrition software using a Random Forest Classifier. The pipeline includes data preprocessing, model training, evaluation metrics, and feature importance visualization. The model utilizes numerical scaling, one-hot encoding for categorical variables, and hyperparameter tuning through grid search.

### Load Data: 
The data is loaded and preprocessed via the function in data.py.

### Model Training:
Train the Random Forest model using the code in model.py.

### Model Evaluation: 
Evaluate the model’s performance using functions in evaluation.py.

### Feature Importance: 
Use features.py to visualize the top 10 most important features in the model.

## Evaluation Metrics
### Accuracy: 
Proportion of correct predictions.

### Confusion Matrix: 
Describes the model's performance on classification tasks.

### ROC AUC Score: 
Evaluates the model's ability to distinguish between classes.

### ROC Curve:
Visualizes true positive rate vs false positive rate.

![image](https://github.com/user-attachments/assets/bbc063c1-c6af-4d78-a2cc-0fc7c0387a50)

![image](https://github.com/user-attachments/assets/cfde2f42-800b-4580-a80e-2d2709ce522c)

![image](https://github.com/user-attachments/assets/127febdc-5536-4ea7-9e96-2b7c51e313e4)

Employee attrition, or turnover, is a significant concern for companies aiming to retain talent. This project applies machine learning techniques to predict whether an employee is likely to leave based on a variety of attributes, such as job satisfaction, work environment, and performance metrics. The goal is to provide businesses with actionable insights to reduce attrition rates.
