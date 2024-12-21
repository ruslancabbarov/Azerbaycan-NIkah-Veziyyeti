
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)

data=pd.read_excel("2023cu ilde bey ve gelinin yas qruplarina gore niikah veziyyeti.xls")
secilen_data=data.iloc[8:17,1:6]
secilen_data.columns=["Yaslar","Nikah sayi","nikahda olmayanlar","bosananlar","dullar"]
# secilen_data.to_csv("Kisiler nikah,bosanma,dullar(2023)",index=False)
print(secilen_data)


