import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={
    "smoking_patients":[200,220,240,260,300],
    "lung_cancer_patients":[20,35,30,45,50],
    }
df= pd.DataFrame(data)
plt.scatter(df['smoking_patients'], df['lung_cancer_patients'],color="red")
plt.xlabel("smoking patients")
plt.ylabel("lung cancer patients")
plt.title("CANCER PATIENTS DETAILS")
plt.show()
correlation=df.corr()
print(correlation)
