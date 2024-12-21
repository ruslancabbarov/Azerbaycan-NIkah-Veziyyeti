from idlelib.iomenu import errors

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)

data=read_excel("bey ve gelinlerin yas qruplarina gore nikahlarin sayi.xls")
data=data.drop(columns=["Unnamed: 0"])

# print(data)
iller=data.iloc[44:80,0]
yasadek=data.iloc[44:80,2]
araliq1=data.iloc[44:80,3]
araliq2=data.iloc[44:80,4]
araliq_yuxari=data.iloc[44:80,5]
qadinlar_umumi=pd.DataFrame({
    "İllər:":iller,
    "18 yaşadək:":yasadek,
    "18-24":araliq1,
    "25-34":araliq2,
    "35 və yuxarı":araliq_yuxari
})
print(qadinlar_umumi)
# qadinlar_umumi.to_csv("Qadınların yaş qruplarına görə nikahların sayı(ümumi)",index=False)

#--------------------------Qadınların yaş qruplarına görə nikahların sayı(ümumi)---vizuallasdirma------

data1=pd.read_csv("Qadınların yaş qruplarına görə nikahların sayı(ümumi)")
data1.replace("-", 0,inplace=True,regex=True)
data1["18 yaşadək:"]=pd.to_numeric(data1["18 yaşadək:"],errors="coerce")
print(data1)
iller=data1["İllər:"]
yasadek_18=data1["18 yaşadək:"]
nikah_18_24=data1["18-24"]
nikah_25_34=data1["25-34"]
nikah_35_plus=data1["35 və yuxarı"]

fig, axs =plt.subplots(2,2, figsize=(8,6))
# 18 yasadek olanlar ucun qrafik
axs[0,0].plot(iller,yasadek_18,marker="o",color="g",label="18 yaşadək")
axs[0,0].set_title("18 yaşa qədər nikah sayı")
axs[0,0].set_xlabel("İllər",fontsize=16)
axs[0,0].set_ylabel("Nikah sayı(nəfər)")
axs[0,0].set_xticks(range(iller.min(),iller.max()+3,3))
axs[0,0].set_yticks(range(0,yasadek_18.max(),500))

axs[0,0].tick_params(axis='x', rotation=45)
axs[0,0].grid(True)
axs[0,0].legend()

#18-24 yas qrupu ucun qrafik
axs[0,1].plot(iller,yasadek_18,marker="o",color="b",label="18-24 yaş")
axs[0,1].set_title("18-24 yaş aralığında nikah sayı")
axs[0,1].set_xlabel("İllər",fontsize=16)
axs[0,1].set_ylabel("Nikah sayı-(nəfər)")
axs[0,1].set_xticks(range(iller.min(),iller.max()+3,3))
axs[0,1].set_yticks(range(0,6500,500))
axs[0,1].tick_params(axis='x', rotation=45)
axs[0,1].grid(True)
axs[0,1].legend()

#25-34 yas qrupu ucun qrafik
axs[1,0].plot(iller,yasadek_18,marker="o",color="r",label="25-34 yaş")
axs[1,0].set_title("25-34 yaş aralığında nikah sayı")
axs[1,0].set_xlabel("İllər",fontsize=16)
axs[1,0].set_ylabel("Nikah sayı-(nəfər)")
axs[1,0].set_xticks(range(iller.min(),iller.max()+3,3))
axs[1,0].set_yticks(range(0,6500,500))
axs[1,0].tick_params(axis='x', rotation=45)

axs[1,0].grid(True)
axs[1,0].legend()

#35 ve yuxari yaslar ucun qrafik

axs[1,1].plot(iller,yasadek_18,marker="o",color="purple",label="35 və yuxarı yaş")
axs[1,1].set_title("35 və yuxarı yaş aralığında nikah sayı")
axs[1,1].set_xlabel("İllər",fontsize=16)
axs[1,1].set_ylabel("Nikah sayı-(nəfər)")
axs[1,1].set_xticks(range(iller.min(),iller.max()+3,3))
axs[1,1].set_yticks(range(0,nikah_35_plus.max(),500))
axs[1,1].tick_params(axis='x', rotation=45)
axs[1,1].grid(True)
axs[1,1].legend()
# fig.suptitle("Yaş qruplarına görə illər üzrə nikaha girən qadınlar",fontsize=18)
plt.tight_layout()
plt.savefig("Yaş qruplarına görə illər üzrə nikaha girən qadınlar",dpi=300)
plt.show()
