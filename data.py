from imports import pd, np, train_test_split, StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

#Function to preprocess data and create a full pipeline including preprocessing and model
def create_pipeline(data):
    data['Attrition'] = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

#Defining feature and categorical columns
    X = data.drop('Attrition', axis=1)
    y = data['Attrition']
    categorical_cols = X.select_dtypes(include=['object']).columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

 
