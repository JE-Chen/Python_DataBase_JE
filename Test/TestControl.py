from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(r'StudentSystemData.sqlite', table_name='StudentSystem')

SQL.table_name = 'Account'

SQL.insert_into_replace('410877027', 'test_password')

SQL.table_name = 'LessonContent'

SQL.insert_into_replace('A877', '87課', '8787878787878787878787878787878787878787', '109')

SQL.table_name = 'LessonDetail'

SQL.insert_into_replace('A877', '4108777027', '87課', '99', 'HCP', '必選修', '109')

SQL.table_name = 'LessonContent'

SQL.select_prefix = 'LessonDetail.LessonCode'

SQL.inner_join('LessonDetail', 'LessonContent.LessonCode', 'LessonDetail.LessonCode')

SQL.table_name = 'LessonGrade'

SQL.insert_into_replace('A877', '410877027', '999', '109', 'HCP')

SQL.table_name = 'Account'

SQL.select_prefix = '*'

SQL.inner_join('LessonGrade', 'Account.PersonnelNumber', 'LessonGrade.PersonnelNumber')

SQL.select_prefix = 'LessonCode'

SQL.inner_join('LessonDetail', 'LessonCode', 'LessonDetail.LessonCode')

SQL.close()
