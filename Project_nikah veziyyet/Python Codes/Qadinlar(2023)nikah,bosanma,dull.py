
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)
data=pd.read_excel("2023cu ilde bey ve gelinin yas qruplarina gore niikah veziyyeti.xls")
print(data)
# secilen_data2=data.iloc[8:17,[1,6,7,8,9]]
# secilen_data2.columns=["Yaslar","Nikah sayi","nikahda olmayanlar","bosananlar","dullar"]
# secilen_data2.to_csv("Qadinlar nikah,bosanma,dullar(2023)",index=False)
# print(secilen_data2)
