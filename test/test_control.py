from je_database.core.sqlite_core import sqlite_core

sql = sqlite_core(db_name=r'test.sqlite', table_name='test', check_same_thread=True)

sql.create_table(
    'CREATE TABLE IF NOT EXISTS test(testNo VARCHAR(20) PRIMARY KEY,testData VARCHAR(20))')

sql.insert_into_ignore("000", "001")

sql.insert_into_replace("000", "002")

sql.update("testData", "testData", "003", "002")

sql.select_prefix = "*"

sql.select_form()

sql.select_where("testData", "003")

sql.close()
