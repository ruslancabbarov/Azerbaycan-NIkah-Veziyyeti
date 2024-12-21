from idlelib.iomenu import errors

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)

file_path="2023 cu il bey ve gelinin yas qruplarina gore nikahlarin sayi.xls"
data=pd.read_excel(file_path,header=None)

yas_qrupu=data.iloc[7:18,1]
nikah_sayi=data.iloc[7:18,2]
yas_qrupu = yas_qrupu.astype(str).str.strip()
data_gelin=pd.DataFrame({
    "Gelinin yas qrupu":yas_qrupu,
    "Nikahlarin sayi":nikah_sayi
})
print(data_gelin)
# data_gelin.to_csv("Gelinin yasi ve nikahi 2023.csv",index=False)

print(data)
yas_qrupu_kisi=["18 yaşadək","18-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60 və yuxarı"]
nikah_sayi_kisi=[0,217,9324,22484,13014,4297,1742,988,716,518,900]
data_kisi=pd.DataFrame({
    "Kisilerin yas qrupu:":yas_qrupu_kisi,
    "Nikaha daxil olan kisilerin sayi:":nikah_sayi_kisi
})
print(data_kisi)
# data_kisi.to_csv("Kisilerin yas qruplara gore nikah gostericileri 2023.csv",index=False)