import pandas as pd

# Load your raw data
raw_data_path = 'data_dictionary.xlsx'

# Mapping definitions based on your data dictionary
data_dict = {
    'SEX': {1: "FEMALE", 2: "MALE", 99: "UNKNOWN"},
    'HOSPITALIZED': {1: "YES", 2: "NO", 99: "UNKNOWN"},
    'INTUBATED': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'PNEUMONIA': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'PREGNANCY': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'SPEAKS_NATIVE_LANGUAGE': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'DIABETES': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'COPD': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'ASTHMA': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'INMUSUPR':{1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'HYPERTENSION': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'OTHER_DISEASE': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'CARDIOVASCULAR': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'OBESITY': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'CHRONIC_KIDNEY': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'TOBACCO': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'ANOTHER_CASE': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'MIGRANT': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'ICU': {1: "YES", 2: "NO", 97: "DOES NOT APPLY", 98: "IGNORED", 99: "UNKNOWN"},
    'OUTCOME': {1: "POSITIVE", 2: "NEGATIVE", 3: "PENDING"},
    'NATIONALITY': {1: "MEXICAN", 2: "FOREIGN", 99: "UNKNOWN"},
}

raw_data = pd.read_excel(raw_data_path)

# Apply the mapping to each variable
for column in raw_data.columns:
    if column in data_dict:
        raw_data[column] = raw_data[column].map(data_dict[column])

# Save the transformed data to a new excel
transformed_data_path = 'transformed_raw_data.xlsx'
raw_data.to_excel(transformed_data_path, index=False)

df=pd.read_excel('transformed_raw_data.xlsx')
df.columns = df.columns.str.upper()
df=df.apply(lambda x: x.str.upper() if x.dtype== 'object' else x)
df