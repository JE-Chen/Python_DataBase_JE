import datetime

from je_database import sqlite_core

print(datetime.datetime.now())
SQL = sqlite_core(db_name=r'Test.sqlite', table_name='Test')
SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Test(testNo VARCHAR(20) PRIMARY KEY,testData VARCHAR(20))')
for i in range(1000):
    SQL.insert_into_replace(str(i), str(i))
print(datetime.datetime.now())
