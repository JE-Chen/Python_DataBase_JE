import datetime

from JEDatabase.Models.Sqlite_Control import Sqlite_Control


class SQLite_Core():

    def __init__(self, DB_Name='test.db', Table_Name='Test'):

        try:

            self.Sqlite_Control = Sqlite_Control(DB_Name, Table_Name)

        except Exception as Errr:
            print(datetime.datetime.now(), 'I JE-Database Error', sep=' ')
            raise Errr

        self.Table_Name = Table_Name
        self.SQLite_Cursor = self.Sqlite_Control.cursor
        self.SQLite_Connect = self.Sqlite_Control.connect

        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')

    # ----------------------------------------------------------------------------------------------

    def Set_Table_Name(self, Table_Name):
        self.Table_Name = Table_Name

    def Set_Value_Count(self, Value_Count):
        self.Value_Count = Value_Count
        self.Sqlite_Control.Value_Count=Value_Count
    # ----------------------------------------------------------------------------------------------
    def ValueError_Log(self, Print):
        print(datetime.datetime.now(), 'I JE-Database Error', sep=' ')
        raise ValueError(Print)

    # ----------------------------------------------------------------------------------------------

    # 創造一表
    def Create_Table(self, SQL_Command):
        self.Sqlite_Control.Create_Table(SQL_Command)

    # ----------------------------------------------------------------------------------------------

    # 插入語句是insert into 加表名(欄位名,欄位名) values(值,值)
    def Insert_Into(self, *args, Field=None):

        if Field == None:
            if len(args) == 1 :
                SQL_Command = '''INSERT INTO ''' + self.Table_Name + ''' VALUES (?)'''
            else:
                SQL_Command = '''INSERT INTO ''' + self.Table_Name + ''' VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''
        else:
            if len(args) == 1:
                SQL_Command = '''INSERT INTO ''' + self.Table_Name + '''(''' + Field + ''') VALUES (?)'''
            else:
                SQL_Command = '''INSERT INTO ''' + self.Table_Name + '''(''' + Field + ''') VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''

        self.Sqlite_Control.Insert_Into(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------

    # 如果有會忽略
    def Insert_Into_Ignore(self, *args, Field=None):

        if Field == None:
            if len(args) == 1:
                SQL_Command = '''INSERT OR IGNORE INTO ''' + self.Table_Name + ''' VALUES (?)'''
            else:
                SQL_Command = '''INSERT OR IGNORE INTO ''' + self.Table_Name + ''' VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''
        else:
            if len(args) == 1:
                SQL_Command = '''INSERT OR IGNORE INTO ''' + self.Table_Name + '''(''' + Field + ''') VALUES (?)'''
            else:
                SQL_Command = '''INSERT OR IGNORE INTO ''' + self.Table_Name + '''(''' + Field + ''') VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''

        self.Sqlite_Control.Insert_Into_Ignore(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------
    # 如果有會取代掉
    def Insert_Into_Replace(self, *args, Field=None):
        if Field == None:
            if len(args) == 1:
                SQL_Command = '''REPLACE INTO ''' + self.Table_Name + ''' VALUES (?)'''
            else:
                SQL_Command = '''REPLACE INTO ''' + self.Table_Name + ''' VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''
        else:
            if len(args) == 1:
                SQL_Command = '''REPLACE INTO ''' + self.Table_Name + '''(''' + Field + ''')VALUES (?)'''
            else:
                SQL_Command = '''REPLACE INTO ''' + self.Table_Name + '''(''' + Field + ''') VALUES (''' + '?,' * (len(args)-1) + '?' + ''')'''

        self.Sqlite_Control.Insert_Into_Replace(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------
    # 更新資料庫語句
    def UPDATE(self, *args, Field, Where_What=None):
        SQL_Command = '''UPDATE ''' + self.Table_Name + ''' SET ''' + Field + '''=? WHERE ''' + Where_What + '''=?'''
        self.Sqlite_Control.UPDATE(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------
    # 刪除語句   delete from 表名 where 範圍，不加where將會刪除整個表但是表的結構還存在就是相當於回到了剛剛建立表的時候
    # SQL_Command= """DELETE FROM student WHERE id = 1;"""
    def DELETE(self, Field, *args):
        SQL_Command = '''DELETE FROM ''' + self.Table_Name + ''' WHERE ''' + Field + ''' =? '''
        self.Sqlite_Control.DELETE(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------
    # 查詢語句select 加欄位名 查詢表中欄位的資訊 加* 查詢所有的資訊 from 表名
    # SQL_Command="""SELECT id,name from student;"""
    def Select_From(self, *args):
        if len(args) == 1:
            SQL_Command = '''SELECT ? FROM ''' + self.Table_Name
            return self.Sqlite_Control.Select_From(SQL_Command, args)
        else:
            SQL_Command = '''SELECT ''' + '?,' * (len(args)-1) + '?' + ''' FROM ''' + self.Table_Name
            return self.Sqlite_Control.Select_From(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------
    # 找出表格不同的值
    def Select_Distinct(self, *args):
        if len(args) == 1:
            SQL_Command = '''SELECT DISTINCT ? FROM ''' + self.Table_Name
            return self.Sqlite_Control.Select_Distinct(SQL_Command, args)
        else:
            SQL_Command = '''SELECT DISTINCT''' + '?,' * (len(args)-1) + '?' + ''' FROM ''' + self.Table_Name
            return self.Sqlite_Control.Select_Distinct(SQL_Command, args)

    # ----------------------------------------------------------------------------------------------

    # select * from  表名 where   加上條件，不加的話就是查詢所有
    # SQL_Command= """SELECT * FROM student WHERE name="小明";"""
    def Select_Where(self, Field, *args):
        if len(args) == 1:
            SQL_Command = '''SELECT ? FROM ''' + self.Table_Name + ''' WHERE ''' + Field + '''=?'''
            return self.Sqlite_Control.Select_Where(Field, SQL_Command, args)
        else:
            SQL_Command = '''SELECT ''' + '?,' * (len(args)-2) + '?' + ''' FROM ''' + self.Table_Name + ''' WHERE ''' + Field + '''=?'''
            return self.Sqlite_Control.Select_Where(Field, SQL_Command, args)

    # ----------------------------------------------------------------------------------------------

    # 回滾到上一次commit
    def Rollback(self):
        self.Sqlite_Control.Rollback()

    # ----------------------------------------------------------------------------------------------

    # 丟棄表
    # SQL_Command="""DROP TABLE student;"""
    def Drop(self):
        SQL_Command = '''DROP TABLE ''' + self.Table_Name + '''=?'''  # 丟棄表（此操作比delete更加嚴重，會刪除表的結構）drop table 加上表名
        self.Sqlite_Control.Drop(SQL_Command, self.Table_Name)

    # ----------------------------------------------------------------------------------------------

    # 關閉
    def Close(self):
        self.Sqlite_Control.Close()
