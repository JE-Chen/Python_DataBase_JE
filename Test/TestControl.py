from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'EMPLOYEE.sqlite', table_name='Employee')

SQL.table_name = 'DEPT_LOCATION'

SQL.insert_into_replace('1112233554', 'TestLocation')

SQL.select_prefix = "*"

SQL.table_name = 'DEPT_LOCATION'

SQL.close()
