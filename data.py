data = pd.read_csv('employee.csv')

#One hot encoding 
data['Attrition'] = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
data['Gender'] = data['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
data['Over18'] = data['Over18'].apply(lambda x: 1 if x == 'Y' else 0)
data['OverTime'] = data['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

