from JEDatabase.Core.SQLiteCore import SQLiteCore

SQL = SQLiteCore(db_name=r'StudentSystemData.sqlite', table_name='StudentSystem')

SQL.table_name = 'Account'

SQL.insert_into_replace('410877027', 'test_password')

SQL.insert_into_replace('410877099', 'test_password')

SQL.table_name = 'LessonContent'

SQL.insert_into_replace('A877', '87課', '8787878787878787878787878787878787878787', '109')

SQL.insert_into_replace('A87', '87課', '8787878787878787878787878787878787878787', '109')

SQL.table_name = 'LessonDetail'

SQL.insert_into_replace('A877', '410877027', '87課', '99', 'HCP', '必選修', '109')

SQL.insert_into_replace('A87', '410877027', '87課', '99', 'HCP', '必選修', '109')

SQL.table_name = 'LessonContent'

SQL.select_prefix = 'LessonDetail.LessonCode'

SQL.inner_join('LessonDetail', 'LessonContent.LessonCode', 'LessonDetail.LessonCode')

SQL.table_name = 'LessonGrade'

SQL.insert_into_replace('A877', '410877027', '999', '109', 'HCP')

SQL.insert_into_replace('A87', '410877027', '999', '109', 'HCP')

SQL.table_name = 'PersonnelAccess'

SQL.insert_into_replace('410877027', 'Super')

SQL.insert_into_replace('410877099', 'Super')

SQL.table_name = 'PersonnelDetail'

SQL.insert_into_replace('410877027', 'JE-Chen', '107')

SQL.insert_into_replace('410877099', 'JE-Chen', '107')

SQL.table_name = 'Account'

SQL.select_prefix = '*'

SQL.inner_join('LessonGrade', 'Account.PersonnelNumber', 'LessonGrade.PersonnelNumber')

SQL.table_name = 'LessonGrade'

SQL.inner_join('LessonDetail', 'LessonGrade.LessonCode', 'LessonDetail.LessonCode')

SQL.table_name = 'LessonDetail'

# SQL.inner_join('PersonnelAccess', 'LessonDetail.PersonnelNumber', 'PersonnelAccess.PersonnelNumber')

SQL.select_prefix = 'PersonnelAccess.Access'

SQL.inner_join_where('PersonnelAccess', 'LessonDetail.PersonnelNumber', 'PersonnelAccess.PersonnelNumber',
                     'PersonnelAccess.PersonnelNumber', "410877027")

SQL.table_name = 'PersonnelAccess'

SQL.inner_join('PersonnelDetail', 'PersonnelDetail.PersonnelNumber', 'PersonnelAccess.PersonnelNumber')

SQL.table_name = 'Account'

SQL.select_prefix = 'LessonContent.LessonCode'

'''
SQL.inner_inner_join(
    'LessonDetail', 'Account.PersonnelNumber', 'LessonDetail.PersonnelNumber',
    'LessonContent', 'LessonDetail.LessonCode', 'LessonContent.LessonCode')
'''

SQL.inner_inner_join_where(
    'LessonDetail', 'Account.PersonnelNumber', 'LessonDetail.PersonnelNumber',
    'LessonContent', 'LessonDetail.LessonCode', 'LessonContent.LessonCode',
    'LessonDetail.LessonName', "87課")

SQL.close()
