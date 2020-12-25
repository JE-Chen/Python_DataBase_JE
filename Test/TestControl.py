from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'StudentSystemData.sqlite', table_name='StudentSystem')

SQL.table_name = 'Account'

SQL.insert_into_replace('410877027', 'test_password')

SQL.table_name = 'LessonContent'

SQL.insert_into_replace('A001', '測試課程', '測試內容', '109')

SQL.table_name = 'LessonDetail'

SQL.insert_into_replace('A001', '測試課程', '3', 'HCP', '必修')

SQL.table_name = 'LessonGrade'

SQL.insert_into_replace('A001', '410877027', '100', '109', 'HCP')

SQL.table_name = 'PersonnelAccess'

SQL.insert_into_replace('410877027', 'Super')

SQL.table_name = 'PersonnelDetail'

SQL.insert_into_replace('410877027', 'JE-Chen', '107')

SQL.table_name = 'PersonnelDetail'

SQL.insert_into_replace('A001', 'JE-Chen', '109')

SQL.select_prefix = "*"

SQL.table_name = 'Account'

SQL.select_form()

SQL.select_where('Password', 'test_password')

SQL.select_account('PersonnelNumber', 'Password', '410877027', 'test_password')

SQL.update('password', 'password', 'test_password', 'new_password')

SQL.select_form()

SQL.close()
