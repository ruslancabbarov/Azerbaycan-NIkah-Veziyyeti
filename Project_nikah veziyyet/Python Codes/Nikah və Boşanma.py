import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import rotate

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)
data=pd.read_excel("Resmi qeyde alinmis nikah ve bosanmalarin sayi ve umumi emsallari.xls")
data=data.drop(columns=["Unnamed: 0"])
data["Unnamed: 1"]=pd.to_numeric(data["Unnamed: 1"],errors="coerce")
data=data.dropna(subset=["Unnamed: 1"])
data=data.rename(columns={"Unnamed: 1":"Illər",
                          "Unnamed: 2":"Nikahların Sayı",
                          "Unnamed: 3":"Boşanmaların sayı"})
data["Illər"]=data["Illər"].astype(int)
# print(data)
print(data.columns)

iller=data["Illər"]
nikah=data["Nikahların Sayı"]
bosanma=data["Boşanmaların sayı"]
fig ,ax=plt.subplots(figsize=(12,6))
ax.plot(iller,nikah,label="Nikahların Sayı",color="b",marker="o")
ax.plot(iller,bosanma,label="Boşanmaların sayı",color="r",marker=".")
max_x_value=iller.max()
ax.set_xticks(range(1935,max_x_value+1,5))
plt.xticks(rotation=45)
max_y_value=iller.max()
ax.set_yticks(range(0,max_y_value+100000,10000))


ax.set_title("Rəsmi qeydə alınmış nikah və boşanmaların sayı və ümumi əmsalları",fontsize=14)
ax.legend(title="Statistika")
# plt.savefig("Rəsmi qeydə alınmış nikah və boşanmaların sayı və ümumi əmsalları",dpi=300)
plt.show()
