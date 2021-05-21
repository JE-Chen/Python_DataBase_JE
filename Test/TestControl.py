from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'Test.sqlite', table_name='Test')

SQL.create_table(
    'CREATE TABLE IF NOT EXISTS Test(testNo VARCHAR(20) PRIMARY KEY,testData VARCHAR(20))')

SQL.insert_into_ignore("000", "001")

SQL.insert_into_replace("000", "002")

SQL.update("testData", "testData", "003", "002")

SQL.select_prefix = "*"

SQL.select_form()

SQL.select_where("testData", "003")

SQL.close()
