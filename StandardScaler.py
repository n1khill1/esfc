import pandas as pd
from sklearn.preprocessing import StandardScaler
data={
    "age":[25,30,35,40,45],
    "height":[150,160,170,180,190],
    "weight":[50,60,70,80,90],

}
df=pd.DataFrame(data)
print("original dataframe:")
print(df)
scaler=StandardScaler()
standardized_data=scaler.fit_transform(df)
standardized_df=pd.DataFrame(standardized_data,columns=df.columns)
print("\nstandardized dataframe(scaled to range[0,1]):")
print(standardized_df)