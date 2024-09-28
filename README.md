# RetentionIQ

RetentionIQ is a comprehensive employee attrition prediction software designed to help organizations forecast employee turnover. Employee attrition, or turnover, is a significant concern for companies aiming to retain talent. This project applies machine learning techniques to predict whether an employee is likely to leave based on a variety of attributes, such as job satisfaction, work environment, and performance metrics. The goal is to provide businesses with actionable insights to reduce attrition rates. By analyzing employee-related data, this tool identifies key factors contributing to employee attrition and improving retention strategies. The core of the model is a Random Forest classifier, integrated into a robust data preprocessing pipeline to handle both numerical and categorical data. The software evaluates model performance using a variety of metrics, including accuracy, ROC AUC scores, and feature importance analysis.

This project also includes hyperparameter tuning using GridSearchCV to optimize model performance, with the potential to further integrate real-time attrition risk scoring and visualization tools.

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
