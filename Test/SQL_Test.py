from Core.SQLite_Core import SQLite_Core

a=SQLite_Core(r'..\Test_Source\test.db')

a.Create_Table('hello','name VARCHAR(10)')

a.Insert_Into_Replace('hello','(id,name)','(1,"小明")')

a.Select_From("id,name","hello")

a.Select_Where('*','hello','name="小明"')

a.UPDATE('hello','name="大紅"','id=1')

a.Select_From("id,name","hello")

a.Insert_Into_Replace('hello','(id,name)','(2,"小明")')

a.Select_From("id,name","hello")

a.DELETE('hello','id=2')

a.Select_From("id,name","hello")

a.Close()



