from operator import delitem

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_excel

pd.set_option("Display.max_columns",None)
pd.set_option("Display.max_rows",None)
pd.set_option("Display.width",None)
data=read_excel("2023cu ilde bey ve gelinin yas qruplarina gore niikah veziyyeti.xls")
# cins1="Kisi"
# cins2="Qadin"
# cemi_nikah_kisi=data.iloc[6,2]
# nikah_olmayan_kisi=data.iloc[6,3]
# bosananlar_kisi=data.iloc[6,4]
# dullar_kisi=data.iloc[6,5]
#
# cemi_nikah_qadin=data.iloc[6,6]
# nikah_olmayan_qadin=data.iloc[6,7]
# bosananlar_qadin=data.iloc[6,8]
# dullar_qadin=data.iloc[6,9]
#
# veziyyet_bey_gelin=pd.DataFrame({
#     "Cinsiyyet":[cins1,cins2],
#     "Cemi nikah sayi":[cemi_nikah_kisi,cemi_nikah_qadin],
#     "Hec vaxt nikahda olmayanlar":[nikah_olmayan_kisi,nikah_olmayan_qadin],
#     "Bosananlar":[bosananlar_kisi,bosananlar_qadin],
#     "Dullar":[dullar_kisi,dullar_qadin]
# })
# print(veziyyet_bey_gelin)
# veziyyet_bey_gelin.to_csv('Kisi ve qadinlarin 2023 ili uzre nikah veziyyetleri',index=False)
# data=pd.read_csv("Kisi ve qadinlarin 2023 ili uzre nikah veziyyetleri")
# print(data)
