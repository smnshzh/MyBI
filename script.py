from peewee import *
import pandas as pd
database = SqliteDatabase('db.sqlite3')

database.connect()
tabels = database.get_tables()
print(tabels)
df = pd.read_excel("../Data/goods.xlsx")
df = df.dropna()
mainGroup = set(df["گروه اصلی"])
i=1
for item in mainGroup:
    database.create(code = i,name = item )
    i+=1