
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.interchange.dataframe_protocol import DataFrame

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)

data=pd.read_excel("resmi qeydiyyata alinmis nikaha daxil olan sexslerin yas ortalamasi.xls")
data=data.drop(columns=["Unnamed: 0"])
data["Unnamed: 1"]=pd.to_numeric(data["Unnamed: 1"],errors='coerce')
# print(data["Unnamed: 1"].unique())
data=data.dropna(subset=["Unnamed: 1"])
data=data.rename(columns={"Unnamed: 1":"Illər",
                          "Unnamed: 2":"Kişilər1",
                          "Unnamed: 3":"Qadınlar1",
                          "Unnamed: 4":"Kişilər2",
                          "Unnamed: 5":"Qadınlar2"})
print("Nikaha daxil olanların orta yaşı")
data1=data[["Illər","Kişilər1","Qadınlar1"]]
print(data1)
# print(data)
# data.info()
x = np.arange(len(data["Illər"]))
width=0.35

fig,ax=plt.subplots(figsize=(12,6))
ax.bar(x-width/2,data["Kişilər1"],width,label="Kişilər1")
ax.bar(x+width/2,data["Qadınlar1"],width,label="Qadınlar1")

ax.set_title("Nikaha daxil olanların orta yaşı(1990-2023)",fontsize=14)
ax.set_xlabel("Illər",fontsize=12)
ax.set_ylabel("Nikaha Daxil Olmuş Şəxslər",fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(data["Illər"], rotation=45, fontsize=10)

max_y_value = int(data[["Kişilər1", "Qadınlar1"]].max().max())
ax.set_yticks(range(0, max_y_value + 1, 1))

ax.legend(title="Cinsiyyət")
plt.tight_layout()

# plt.savefig("nikah_orta_yaslari.png", dpi=300)
plt.show()
