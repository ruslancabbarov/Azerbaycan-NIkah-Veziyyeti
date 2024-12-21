import pymysql
import pandas as pd


# data=pd.read_csv("Kisiler nikah,bosanma,dullar(2023)")
# data.replace("-",0,inplace=True,regex=True)
# # print(data)
#
# connection=pymysql.connect(host='localhost',
#                            user='root',
#                            password='xxxxxxxxxxxxx',
#                            db='kisi_nikahlar_2023',
#                            charset='utf8mb4',
#                            cursorclass=pymysql.cursors.DictCursor)
# try:
#     with connection.cursor() as cursor:
#         for index, row in data.iterrows():
#             sql = """
#             INSERT INTO kisi_nikahlar(Yaslar, Nikah_sayi, Nikahda_olmayanlar, Bosananlar, Dullar)
#             VALUES (%s, %s, %s, %s, %s)
#             """
#             cursor.execute(sql, (row['Yaslar'], row['Nikah sayi'], row['nikahda olmayanlar'], row['bosananlar'], row['dullar']))
#         connection.commit()
# finally:
#     connection.close()

#---------------------------------------------------------------------------
# data=pd.read_csv("Qadinlar nikah,bosanma,dullar(2023)")
# data.replace("-",0,inplace=True,regex=True)
# print(data)
# connection2=pymysql.connect(host='localhost',
#                             user='root',
#                             password='xxxxxxxxxxxxxxx',
#                             db='qadin_nikahlar_2023',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)
# try:
#     with connection2.cursor() as cursor2:
#         for index2, row2 in data.iterrows():
#             sql2="""
#             INSERT INTO qadin_nikahlar(Yaslar,Nikah_sayi,Nikahda_olmayanlar,Bosananlar,Dullar)
#             VALUES (%s, %s, %s, %s, %s)
#             """
#             cursor2.execute(sql2,(row2['Yaslar'], row2['Nikah sayi'],row2['nikahda olmayanlar'], row2['bosananlar'], row2['dullar']))
#         connection2.commit()
# finally:
#     connection2.close()


#--------------------------------------------------------------------------------------------
data2=pd.read_csv("Kisi ve qadinlarin 2023 ili uzre nikah veziyyetleri")
print(data2)
connection3=pymysql.connect(host='localhost',
                            user='root',
                            password='xxxxxxxxxxxxxxx',
                            db='cemi_nikah_veziyyet_2023',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
try:
    with connection3.cursor() as cursor3:
        for index3,row3 in data2.iterrows():
            sql3="""INSERT INTO nikah_veziyyet_cemi_2023(Cinsiyyet,Nikah_sayi,Nikahda_olmayanlar,Bosananlar,Dullar)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor3.execute(sql3,(row3['Cinsiyyet'], row3['Cemi nikah sayi'],row3['Hec vaxt nikahda olmayanlar'], row3['Bosananlar'], row3['Dullar']))
        connection3.commit()
finally:
    connection3.close()