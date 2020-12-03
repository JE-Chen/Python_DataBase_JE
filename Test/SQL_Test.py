from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(r'..\Test_Source\Account.db', table_name='Account')

SQL.create_table('CREATE TABLE IF NOT EXISTS Account(id INTEGER PRIMARY KEY,email VARCHAR(50),password VARCHAR(15))')

SQL.insert_into_replace(1, 'test1@gmail.com', 'test_password')

SQL.select_form('id', 'email')

SQL.insert_into_replace(2, 'test2@gmail.com', 'test_password')

SQL.delete('email', 'test1@gmail.com')

SQL.insert_into_replace(3, 'test3@gmail.com', 'test_password')

SQL.select_distinct('email')

SQL.select_where('email', 'email', 'test3@gmail.com')

SQL.close()
