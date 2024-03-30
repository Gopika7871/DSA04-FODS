import pandas as pd
import numpy as np
data={
    "city_A_temp":[20,30,25,32,19],
    "city_B_temp":[21,20,32,35,42],
    "year":[2020,2021,2022,2023,2024]
    }
df=pd.DataFrame(data)
m1=np.mean(df["city_A_temp"])
m2=np.mean(df["city_B_temp"])
print("The mean temperature of city A:",m1)
print("\nThe mean temperature of city B:",m2)
std_div1=np.std(df["city_A_temp"])
std_div2=np.std(df["city_B_temp"])
print("\nThe standard deviation of temperature of city A:",std_div1)
print("\nThe standard deviation of temperature of city B:",std_div2)
d1=np.max(df["city_A_temp"])-np.min(df["city_A_temp"])
d2=np.max(df["city_B_temp"])-np.min(df["city_B_temp"])
if(d1>d2):
    print("\nCity A has highest temperature range:",d1)
else:
    print("\nCity B has highest temperature range:",d2)
if(std_div1>std_div2):
    print("\nCity B has most consistent temperatures")
else:
    print("\nCity A has most consistent temperatures")
