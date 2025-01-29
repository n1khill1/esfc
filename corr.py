import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
np.random.seed(42)
data = {
    "Study Hours" : np.random.randint(1,10,10),
    "Marks" : np.random.randint(50,100,10),
    "screen time" : np.random.randint(1,10,10),
    "travelling time" : np.random.randint(1,10,10),
    "sleep hours": np.random.randint(1,10,10),
}
df = pd.DataFrame(data)
corr = df.corr()
plt.figure(figsize=(8,6)) 
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("feature Correlation Heatmap")
plt.show()