import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)
data=read_excel("bey ve gelinlerin yas qruplarina gore nikahlarin sayi.xls")
data=data.drop(columns=["Unnamed: 0"])
#
# iller=data.iloc[5:40,0]
# nikah_say=data.iloc[5:40,1]
# nikah_saylari=pd.DataFrame({
#     "İllər":iller,
#     "Nikahların sayı":nikah_say
# })
# print(nikah_saylari)
# nikah_saylari.to_csv("1980-2023 nikah saylari",index=False)
#
# data1=pd.read_csv("1980-2023 nikah saylari")
# print(data1)
# iller=data1["İllər"]
# nikah_say=data1["Nikahların sayı"]
# plt.figure(figsize=(12,6))
# plt.plot(iller,nikah_say,color="r",marker="o")
# plt.xlabel("İllər")
# plt.ylabel("Nikahların sayı")
# plt.xticks(ticks=range(iller.min(),iller.max()+1,2),rotation=45)
# plt.yticks(ticks=range(nikah_say.min(),nikah_say.max()+5000,5000))
# plt.savefig("1980-2023 nikah saylari",dpi=300)
# plt.show()

#---------------------------------------------------
# data=read_excel("bey ve gelinlerin yas qruplarina gore nikahlarin sayi.xls")
# # data=data.drop(columns=["Unnamed: 0"])
#
# iller=data.iloc[4:40,0]
# yasadek=data.iloc[4:40,2]
# araliq1=data.iloc[4:40,3]
# araliq2=data.iloc[4:40,4]
# araliq_yuxari=data.iloc[4:40,5]
# kisiler_umumi=pd.DataFrame({
#     "İllər:":iller,
#     "18 yaşadək:":yasadek,
#     "18-24":araliq1,
#     "25-34":araliq2,
#     "35 və yuxarı":araliq_yuxari
# })
# # kisiler_umumi.to_csv("Bəyərin yaş qruplarına görə nikahların sayı(ümumi)"index=False)

#--------------------kisilerin  nikaha daxil olmalari (umumi) vizuallasdirma----------------
from matplotlib.ticker import MaxNLocator

data1=pd.read_csv("Bəyərin yaş qruplarına görə nikahların sayı(ümumi)")
iller=data1["İllər:"]
data1["18 yaşadək:"]=data1["18 yaşadək:"].replace("-",pd.NA,regex=True)
data1["18 yaşadək:"]=data1["18 yaşadək:"].fillna(0).astype(int)
yasadek_18=data1["18 yaşadək:"]

nikah_18_24=data1["18-24"]
print(nikah_18_24)
nikah_25_34=data1["25-34"]
nikah_35_plus=data1["35 və yuxarı"]
# print(data1)


fig, axs =plt.subplots(2,2, figsize=(8,6))
# 18 yasadek olanlar ucun qrafik
axs[0,0].plot(iller,yasadek_18,marker="o",ms=2,color="b",label="18 yaşadək")
axs[0,0].set_title("18 yaşa qədər nikah sayı")
axs[0,0].set_xlabel("İllər",fontsize=16)
axs[0,0].set_ylabel("Nikah sayı(nəfər)")
axs[0,0].set_xticks(range(iller.min(),iller.max()+3,3))
axs[0,0].set_yticks(range(yasadek_18.min(),yasadek_18.max()+10,10))
axs[0,0].tick_params(axis='x', rotation=45,labelsize=8)
axs[0,0].grid(True)
axs[0,0].legend()

#18-24 yas qrupu ucun qrafik
axs[0,1].plot(iller,nikah_18_24,marker="o",ms=2,color="r",label="18-24 yaş")
axs[0,1].set_title("18-24 yaş aralığında nikah sayı")
axs[0,1].set_xlabel("İllər",fontsize=16)
axs[0,1].set_ylabel("Nikah sayı-(nəfər)")
axs[0,1].set_xticks(range(iller.min(),iller.max()+3,3))
axs[0,1].set_yticks(range(3000,nikah_18_24.max()+1000,3000))
axs[0,1].tick_params(axis='x', rotation=45,labelsize=8)
axs[0,1].grid(True)
axs[0,1].legend()

#25-34 yas qrupu ucun qrafik
axs[1,0].plot(iller,nikah_25_34,marker="o",ms=2,color="g",label="25-34 yaş")
axs[1,0].set_title("25-34 yaş aralığında nikah sayı")
axs[1,0].set_xlabel("İllər",fontsize=16)
axs[1,0].set_ylabel("Nikah sayı-(nəfər)")
axs[1,0].set_xticks(range(iller.min(),iller.max()+3,3))
axs[1,0].set_yticks(range(3000,nikah_25_34.max()+1000,5000))
axs[1,0].tick_params(axis='x', rotation=45,labelsize=8)
axs[1,0].grid(True)
axs[1,0].legend()

#35 ve yuxari yaslar ucun qrafik

axs[1,1].plot(iller,nikah_35_plus,marker="o",ms=2,color="purple",label="35 və yuxarı yaş")
axs[1,1].set_title("35 və yuxarı yaş aralığında nikah sayı")
axs[1,1].set_xlabel("İllər",fontsize=16)
axs[1,1].set_ylabel("Nikah sayı-(Min/nəfər)")
axs[1,1].set_xticks(range(iller.min(),iller.max()+3,3))
axs[1,1].set_yticks(range(3000,nikah_35_plus.max()+500,1000))
axs[1,1].tick_params(axis='x', rotation=45,labelsize=8)
axs[1,1].grid(True)
axs[1,1].legend()
fig.suptitle("Yaş qruplarına görə illər üzrə nikaha girən kişilər",fontsize=18)
plt.tight_layout()
# plt.savefig("Yaş qruplarına görə illər üzrə nikaha girən kişilər",dpi=300)
plt.show()