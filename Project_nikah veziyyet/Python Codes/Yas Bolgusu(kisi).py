import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("Kisilerin yas qruplara gore nikah gostericileri 2023.csv")
data.columns=data.columns.str.strip()
data["Kisilerin yas qrupu:"]=data["Kisilerin yas qrupu:"].replace({
    "18 yaşadək":"18",
    "60 və yuxarı":"60"
})
yaslar=data["Kisilerin yas qrupu:"]
nikahlar=data["Nikaha daxil olan kisilerin sayi:"]

plt.figure(figsize=(10,6))
plt.bar(yaslar,nikahlar,color="skyblue")
plt.title("Kişilərin yaş qruplarına görə nikaha daxil olma göstəriciləri(2023)")
plt.xlabel("Yaş qrupu")
plt.ylabel("Nikahların sayı")
plt.yticks(np.arange(0,int(yaslar.max())+25000,700))
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Kişilərin yaş qruplarına görə nikaha daxil olma göstəriciləri_2023")
plt.show()
#---------------------------------------------PieChart diagram'nın code'u--------------------------------------------
# data.columns=data.columns.str.strip()
# data["Kisilerin yas qrupu"] = data["Kisilerin yas qrupu:"].replace({
#     "18 yaşadək": "0-18",
#     "60 və yuxarı": "60-80"
# })
#
# data["Kisilerin yas qrupu"] = data["Kisilerin yas qrupu"].str.replace(
#     r"^(\d+)$", r"\1-\1", regex=True
# )
# data = data[~data["Kisilerin yas qrupu"].isin(["18-19"])]
#
# yaslar=data["Kisilerin yas qrupu"]
# nikahlar=data["Nikaha daxil olan kisilerin sayi:"]
# explode = [0.5 if yas=="0-18" or yas == "60-80" else 0 for yas in yaslar]
# plt.figure(figsize=(8,8))
# plt.pie(nikahlar,labels=yaslar,autopct="%1.1f%%",startangle=140,textprops={'fontsize': 10},explode=explode)
# plt.title("Kişilərin yaş qruplarına görə nikaha daxil olma göstəriciləri(2023)")
# plt.tight_layout()
# plt.legend(yaslar, title="Yaş Qrupları", bbox_to_anchor=(1, -0.15), loc='lower right', fontsize=10)
# plt.savefig("Kişilərin yaş qruplarına görə nikaha daxil olma göstəriciləri_2023",dpi=300)
# plt.show()