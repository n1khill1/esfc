import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {
    "customer_id": [1, 2, 3, 4, 5],
    "gender": ["male", "female", "male", "female", "male"],
    "city": ["Hyderabad", "Paris", "London", "Vizag", "New York"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

one_hot_encoder = OneHotEncoder(sparse_output=False)
columns_to_encode = ["gender", "city"]
encoded_data = one_hot_encoder.fit_transform(df[columns_to_encode])

encoded_columns = one_hot_encoder.get_feature_names_out(columns_to_encode)
encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)

encoded_df = pd.DataFrame(encoded_data, columns=encoded_columns)
print("\nDataFrame after One-Hot Encoding:")
print(encoded_df)