import datetime

from JELogSystem.Log_System import Log_System

from JEDatabase.Models.SqliteControl import SqliteControl


class SQLiteCore:

    def __init__(self, db_name: str = 'test.sqlite', table_name: str = 'Test'):
        """
        :type db_name: str
        :type table_name: str
        """
        try:
            self.SqliteControl = SqliteControl(db_name, table_name)
            log = Log_System()
            log.Set_BoardCast_Lv(3)
        except Exception as Errors:
            print(datetime.datetime.now(), 'I JE-Database Error', sep=' ')
            raise Errors

        self.table_name = table_name
        self.value_count = 2
        self.SQLite_Cursor = self.SqliteControl.cursor
        self.SQLite_Connect = self.SqliteControl.connect

        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')

    # ----------------------------------------------------------------------------------------------

    def set_table_name(self, table_name):
        self.table_name = table_name

    def set_value_count(self, value_count):
        self.value_count = value_count
        self.SqliteControl.Value_Count = value_count

    # ----------------------------------------------------------------------------------------------

    # 創造一表
    def create_table(self, sql_command):
        self.SqliteControl.create_table(sql_command)

    # ----------------------------------------------------------------------------------------------

    # 插入語句是insert into 加表名(欄位名,欄位名) values(值,值)
    def insert_into(self, *args, field=None):

        if field is None:
            if len(args) == 1:
                sql_command = '''INSERT INTO ''' + self.table_name + ''' VALUES (?)'''
            else:
                sql_command = '''INSERT INTO ''' + self.table_name + ''' VALUES (''' + '?,' * (
                        len(args) - 1) + '?' + ''')'''
        else:
            if len(args) == 1:
                sql_command = '''INSERT INTO ''' + self.table_name + '''(''' + field + ''') VALUES (?)'''
            else:
                sql_command = '''INSERT INTO ''' + self.table_name + '''(''' + field + ''') VALUES (''' + '?,' * (
                        len(args) - 1) + '?' + ''')'''

        self.SqliteControl.insert_into(sql_command, args)

    # ----------------------------------------------------------------------------------------------

    # 如果有會忽略
    def insert_into_ignore(self, *args, field=None):

        if field is None:
            if len(args) == 1:
                sql_command = '''INSERT OR IGNORE INTO ''' + self.table_name + ''' VALUES (?)'''
            else:
                sql_command = '''INSERT OR IGNORE INTO ''' + self.table_name + ''' VALUES (''' + '?,' * (
                        len(args) - 1) + '?' + ''')'''
        else:
            if len(args) == 1:
                sql_command = '''INSERT OR IGNORE INTO ''' + self.table_name + '''(''' + field + ''') VALUES (?)'''
            else:
                sql_command = '''INSERT OR IGNORE INTO ''' + \
                              self.table_name + '''(''' + field + ''') VALUES (''' + '?,' * \
                              (len(args) - 1) + '?' + ''')'''

        self.SqliteControl.insert_into_ignore(sql_command, args)

    # ----------------------------------------------------------------------------------------------
    # 如果有會取代掉
    def insert_into_replace(self, *args, field=None):
        if field is None:
            if len(args) == 1:
                sql_command = '''REPLACE INTO ''' + self.table_name + ''' VALUES (?)'''
            else:
                sql_command = '''REPLACE INTO ''' + self.table_name + ''' VALUES (''' + '?,' * (
                        len(args) - 1) + '?' + ''')'''
        else:
            if len(args) == 1:
                sql_command = '''REPLACE INTO ''' + self.table_name + '''(''' + field + ''')VALUES (?)'''
            else:
                sql_command = '''REPLACE INTO ''' + self.table_name + '''(''' + field + ''') VALUES (''' + '?,' * (
                        len(args) - 1) + '?' + ''')'''

        self.SqliteControl.insert_into_replace(sql_command, args)

    # ----------------------------------------------------------------------------------------------
    # 更新資料庫語句
    def update(self, *args, field, where_what=None):
        sql_command = '''UPDATE ''' + self.table_name + ''' SET ''' + field + '''=? WHERE ''' + where_what + '''=?'''
        self.SqliteControl.update(sql_command, args)

    # ----------------------------------------------------------------------------------------------
    # 刪除語句   delete from 表名 where 範圍，不加where將會刪除整個表但是表的結構還存在就是相當於回到了剛剛建立表的時候
    # SQL_Command= """DELETE FROM student WHERE id = 1;"""
    def delete(self, field, *args):
        sql_command = '''DELETE FROM ''' + self.table_name + ''' WHERE ''' + field + ''' =? '''
        self.SqliteControl.delete(sql_command, args)

    # ----------------------------------------------------------------------------------------------
    # 查詢語句select 加欄位名 查詢表中欄位的資訊 加* 查詢所有的資訊 from 表名
    # SQL_Command="""SELECT id,name from student;"""
    def select_form(self, *args):
        if len(args) == 1:
            sql_command = '''SELECT ? FROM ''' + self.table_name
            return self.SqliteControl.select_from(sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (len(args) - 1) + '?' + ''' FROM ''' + self.table_name
            return self.SqliteControl.select_from(sql_command, args)

    # ----------------------------------------------------------------------------------------------
    # 找出表格不同的值
    def select_distinct(self, *args):
        if len(args) == 1:
            sql_command = '''SELECT DISTINCT ? FROM ''' + self.table_name
            return self.SqliteControl.select_distinct(sql_command, args)
        else:
            sql_command = '''SELECT DISTINCT''' + '?,' * (len(args) - 1) + '?' + ''' FROM ''' + self.table_name
            return self.SqliteControl.select_distinct(sql_command, args)

    # ----------------------------------------------------------------------------------------------

    # select * from  表名 where   加上條件，不加的話就是查詢所有
    # SQL_Command= """SELECT * FROM student WHERE name="小明";"""
    def select_where(self, field, *args):
        if len(args) == 1:
            sql_command = '''SELECT ? FROM ''' + self.table_name + ''' WHERE ''' + field + '''=?'''
            return self.SqliteControl.select_where(field, sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (
                    len(args) - 2) + '?' + ''' FROM ''' + self.table_name + ''' WHERE ''' + field + '''=?'''
            return self.SqliteControl.select_where(field, sql_command, args)

    # ----------------------------------------------------------------------------------------------

    # 回滾到上一次commit
    def rollback(self):
        self.SqliteControl.rollback()

    # ----------------------------------------------------------------------------------------------

    # 丟棄表
    # SQL_Command="""DROP TABLE student;"""
    def drop(self):
        sql_command = '''DROP TABLE ''' + self.table_name + '''=?'''  # 丟棄表（此操作比delete更加嚴重，會刪除表的結構）drop table 加上表名
        self.SqliteControl.drop(sql_command, self.table_name)

    # ----------------------------------------------------------------------------------------------

    # 關閉
    def close(self):
        self.SqliteControl.close()
