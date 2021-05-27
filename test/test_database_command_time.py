import datetime

from je_database import sqlite_core

print(datetime.datetime.now())
sql = sqlite_core(db_name=r'test.sqlite', table_name='test', check_same_thread=True)
sql.create_table(
    'CREATE TABLE IF NOT EXISTS test(testNo VARCHAR(20) PRIMARY KEY,testData VARCHAR(20))')
for i in range(1000):
    sql.insert_into_replace(str(i), str(i))
print(datetime.datetime.now())
