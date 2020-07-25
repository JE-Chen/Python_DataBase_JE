from Models.Sqlite_Control import Sqlite_Control
from Models.SQLite_Secure import SQLite_Secure

class SQLite_Core():

    def __init__(self,DB_Name='test'):
        try:
            self.Sqlite_Control=Sqlite_Control(DB_Name)
            self.SQLite_Secure=SQLite_Secure()
        except Exception as Errr:
            raise Errr
        print('SQLite_Core Ready','\n')

        self.SQLite_Cursor = self.Sqlite_Control.cursor
        self.SQLite_Connect = self.Sqlite_Control.connect

# ----------------------------------------------------------------------------------------------
    # 創造一表
    # """CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name VARCHAR(10));"""
    def Create_Table(self,*args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """CREATE TABLE IF NOT EXISTS """ + Table_Name + """(id INTEGER PRIMARY KEY,name VARCHAR(10));"""
        else:
            Table_Name = args[0]
            Field = args[1]
            SQL_Command = """CREATE TABLE IF NOT EXISTS """ + Table_Name + """(id INTEGER PRIMARY KEY,""" + Field + """);"""
        self.Sqlite_Control.Create_Table(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
    # 插入語句是insert into 加表名 （欄位名， 欄位名）values （對應的值， 對應的值）因為id是主鍵自增，所以就沒有新增他的值
    # SQL_Command="""INSERT INTO student(name) VALUES ("小明");"""
    def Insert_Into(self,*args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """INSERT INTO """ + Table_Name + """ (name) VALUES ("小明");"""
        else:
            Table_Name = args[0]
            Table_Field_Name = args[1]
            Value = args[2]
            SQL_Command = """INSERT INTO """ + Table_Name + ' ' + Table_Field_Name + """ VALUES """ + Value + """;"""
        self.Sqlite_Control.Insert_Into(self.SQLite_Secure.Check(SQL_Command))

    # 如果有會忽略
    # SQL_Command="""INSERT OR IGNORE INTO student(name) VALUES ("小明");"""
    def Insert_Into_Ignore(self, *args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """IGNORE INTO """ + Table_Name + """ (name) VALUES ("小明");"""
        else:
            Table_Name = args[0]
            Table_Field_Name = args[1]
            Value = args[2]
            SQL_Command = """IGNORE INTO """ + Table_Name + ' ' + Table_Field_Name + """ VALUES """ + Value + """;"""
        self.Sqlite_Control.Insert_Into_Ignore(self.SQLite_Secure.Check(SQL_Command))

    # 如果有會取代掉
    # SQL_Command="""INSERT OR REPLACE INTO student(name) VALUES ("小明");"""
    def Insert_Into_Replace(self, *args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """REPLACE INTO """ + Table_Name + """ (name) VALUES ("小明");"""
        else:
            Table_Name = args[0]
            Table_Field_Name = args[1]
            Value = args[2]
            SQL_Command = """REPLACE INTO """ + Table_Name + ' ' + Table_Field_Name + """ VALUES """ + Value + """ ;"""
        self.Sqlite_Control.Insert_Into_Replace(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
    # 查詢語句select 加欄位名 查詢表中欄位的資訊 加* 查詢所有的資訊   from 表名
    # SQL_Command="""SELECT id,name from student;"""
    def Select_From(self, *args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """SELECT id,name from """ + Table_Name + """;"""
        else:
            Search_Option = args[0]
            Table_Name = args[1]
            SQL_Command = """SELECT """ + Search_Option + """ from """ + Table_Name + """;"""
        return self.Sqlite_Control.Select_From(self.SQLite_Secure.Check(SQL_Command))

    # select * from  表名 where   加上條件，不加的話就是查詢所有
    # SQL_Command= """SELECT * FROM student WHERE name="小明";"""
    def Select_Where(self, *args):
        if len(args) == 1:
            Select_Thing = args[0]
            SQL_Command = """SELECT """ + Select_Thing + """FROM hello WHERE name="小明";"""
        else:
            Select_Thing = args[0]
            Select_Table = args[1]
            Select_Where = args[2]
            SQL_Command = """SELECT """ + Select_Thing + """ FROM """ + Select_Table + """ WHERE """ + Select_Where + """;"""
        return self.Sqlite_Control.Select_Where(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
    # 更新資料庫語句 update 加表名 set 欄位名=要更新的值  where 限定條件 ，如果不加where 和後面的條件，將會全部生效
    # SQL_Command="""UPDATE student SET name="大紅" WHERE id=1;"""
    def UPDATE(self, *args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """UPDATE """ + Table_Name + """ SET name="大紅 WHERE id=1;"""
        else:
            Table_Name = args[0]
            Update_Thing = args[1]
            Update_Where = args[2]
            SQL_Command = """UPDATE """ + Table_Name + """ SET """ + Update_Thing + """ WHERE """ + Update_Where + """;"""
        self.Sqlite_Control.UPDATE(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
  # 刪除語句   delete from 表名 where 範圍，不加where將會刪除整個表但是表的結構還存在就是相當於回到了剛剛建立表的時候
    # SQL_Command= """DELETE FROM student WHERE id = 1;"""
    def DELETE(self, *args):
        if len(args) == 1:
            Table_Name = args[0]
            SQL_Command = """DELETE FROM """ + Table_Name + """ WHERE id = 1;"""
        else:
            Table_Name = args[0]
            Delete_Where = args[1]
            SQL_Command = """DELETE FROM """ + Table_Name + """ WHERE """ + Delete_Where + """;"""
        self.Sqlite_Control.DELETE(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
    # 丟棄表
    # SQL_Command="""DROP TABLE student;"""
    def Drop(self, Table_Name):
        SQL_Command = """DROP TABLE """ + Table_Name + """;""" # 丟棄表（此操作比delete更加嚴重，會刪除表的結構）drop table 加上表名
        self.Sqlite_Control.Drop(self.SQLite_Secure.Check(SQL_Command))
# ----------------------------------------------------------------------------------------------
    # 關閉
    def Close(self):
        self.Sqlite_Control.Close()