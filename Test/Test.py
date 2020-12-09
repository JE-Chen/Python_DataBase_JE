from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(r'Account.sqlite', table_name='Account')

SQL.create_table('CREATE TABLE IF NOT EXISTS Account(id PRIMARY KEY ,email VARCHAR(50),password VARCHAR(15))')

SQL.insert_into_ignore(1, 'test1@gmail.com', 'test_password')

SQL.insert_into_ignore(2, 'test2@gmail.com', 'test_password')

SQL.delete('email', 'test1@gmail.com')

SQL.select_form()

SQL.select_distinct()

SQL.insert_into_ignore(3, 'test3@gmail.com', 'test_password')

SQL.update('new_test@gmail.com', 'test2@gmail.com', field='email', where_what='email')

SQL.select_account('new_test@gmail.com', 'test_password')

SQL.close()
