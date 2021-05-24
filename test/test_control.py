from je_database.core.sqlite_core import sqlite_core

SQL = sqlite_core(db_name=r'test.sqlite', table_name='test')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS test(testNo VARCHAR(20) PRIMARY KEY,testData VARCHAR(20))')

SQL.insert_into_ignore("000", "001")

SQL.insert_into_replace("000", "002")

SQL.update("testData", "testData", "003", "002")

SQL.select_prefix = "*"

SQL.select_form()

SQL.select_where("testData", "003")

SQL.close()
