#Function to evaluate the trained model using various metrics
def evaluate_model(pipeline, X_test, y_test):
    y_pred = pipeline.predict(X_test)

#Evaluation metrics
    report = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])

    print("Classification Report:\n", report)
    print("Accuracy Score: ", accuracy)
    print("Confusion Matrix:\n", conf_matrix)
    print("ROC AUC Score: ", roc_auc)

#Plotting the ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, pipeline.predict_proba(X_test)[:, 1])
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', label='ROC Curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='red', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()
