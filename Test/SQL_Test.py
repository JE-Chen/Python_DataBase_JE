from JEDatabase.Core import SQLite_Core

SQL=SQLite_Core(r'..\Test_Source\Account.db',Table_Name='Account')

SQL.Create_Table('CREATE TABLE IF NOT EXISTS Account(id INTEGER PRIMARY KEY,email VARCHAR(50),password VARCHAR(15))')

SQL.Insert_Into_Replace(1,'test1@gmail.com','test_password')

SQL.Select_From('id','email')

SQL.Insert_Into_Replace(2,'test2@gmail.com','test_password')

SQL.DELETE('email','test1@gmail.com')

SQL.Insert_Into_Replace(3,'test3@gmail.com','test_password')

SQL.Select_Distinct('email')

SQL.Select_Where('email','email','test3@gmail.com')

SQL.Close()



