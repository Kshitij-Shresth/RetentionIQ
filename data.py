from imports import pd, np, train_test_split, StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

#One hot encoding
def preprocess_data(data):
    data['Attrition'] = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
    data['Gender'] = data['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
    data['Over18'] = data['Over18'].apply(lambda x: 1 if x == 'Y' else 0)
    data['OverTime'] = data['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)
    data.fillna(method='ffill', inplace=True)
    
    X = data.drop('Attrition', axis=1) 
    y = data['Attrition']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
