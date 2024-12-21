import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("Gelinin yasi ve nikahi 2023.csv")
data.columns = data.columns.str.strip()
yaslar=data["Gelinin yas qrupu"]
nikahlar=data["Nikahlarin sayi"]

plt.figure(figsize=(10,6))
plt.bar(yaslar,nikahlar,color="skyblue")

plt.title("Yaş qrupları üzrə qadın nikahları(2023)")
plt.xlabel("Yaş qrupu")
plt.ylabel("Nikahların sayı")
plt.yticks(range(0,int(nikahlar.max())+1000,1000))
plt.xticks(rotation=45)

plt.tight_layout()

# plt.savefig("yas_qruplari_qadin_nikahlar_2023",dpi=300)
plt.show()
# data.info()