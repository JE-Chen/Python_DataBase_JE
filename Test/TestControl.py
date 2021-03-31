from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'Employee.sqlite', table_name='DEPT_LOCATION')

SQL.insert_into_replace('1112233554', 'TestLocation')

SQL.select_prefix = "*"

SQL.select_form()

SQL.close()
