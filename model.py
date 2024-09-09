from imports import RandomForestClassifier, train_test_split, classification_report, accuracy_score
import pandas as pd
import numpy as np

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
