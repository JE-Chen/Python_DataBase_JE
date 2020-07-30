import datetime
import sqlite3

'''
1.整數
整數：常用INT INTEGER 佔4個位元組，2**32，可以表示常用範圍整數。
（不常用）TINYINT（1位元組） SMALLINT（2位元組） MEDIUMINT（3位元組）
BIGINT（8位元組） 適用身份證號、VIP號碼比較長的編號。

2.浮點數
常用 FLOAT(4位元組) 單精度小數 。 即使是單精度，範圍也不小。
DOUBLE(8位元組) 雙精度小數。
場景 金錢計算，軌道計算。

3.字串
CHAR char(10) 可以儲存長度（位元組長度）不超過10的字串。例如"hello"。但由於長度按照位元組判斷，存unicode編碼的中文只能存3個。
常用 VARCHAR 0-65535位元組，variable char 可變字串。VARCHAR(5) 可以儲存5箇中文或5個英文字母。場景 使用者名稱、家庭住址。
TEXT TINYTEXT medium longtext ， 場景 大文字儲存，書籍文章、使用者反饋。
BLOB medium longblob ，二進位制檔案， 場景 圖片、視訊。但一般不在資料庫中儲存圖片和視訊，因為會增加資料庫的計算壓力和頻寬傳輸壓力和備份還原的難度和使用者資訊靜態資源耦合到一起，解決方案是 圖片視訊存到普通檔案目錄下，資料庫中儲存檔案路徑。

4.日期
DATE 日期， 形如"2018-11-08"
常用 DATETIME 日期時間， “2018-11-08 16:52:30” “2018-11-08 16:52:30.123” “2018-11-08 16:52:30 GTM+8”
常用 TIMESTAMP 時間戳, 1541667270 1541667270.7252207 1541667270725

1 sqlite3.connect（數據庫[，timeout，其他可選參數]）

該API：一個到SQLite數據庫文件數據庫的鏈接。您可以使用“：memory：”來在RAM中打開一個到數據庫的數據庫連接，而不是在磁盤上打開。如果數據庫成功打開，則返回一個連接對象。

當一個數據庫被多個連接訪問，並且其中一個修改過的數據庫，此時SQLite數據庫被鎖定，直到事務提交。timeout參數表示連接等待鎖定的持續時間，直到發生異常中斷連接。timeout參數最小為5.0（ 5秒）。

如果給定的數據庫名稱filename不存在，則該調用將創建一個數據庫。如果您不想在當前目錄中創建數據庫，那麼您可以指定帶有路徑的文件名，這樣您就可以在任意地方創建數據庫。

2 connection.cursor（[cursorClass]）

該方法接受一個單一的可選的參數cursorClass。如果提供了該參數，則它必須是一個擴展自sqlite3.Cursor的自定義的光標類。 

3 cursor.execute（sql [，可選參數]）

該例程執行一個SQL語句。該SQL語句可以被參數化（即使用佔位符代替SQL文本）。sqlite3模塊支持兩種類型的佔位符：問號和命名佔位符（命名樣式）。

例如：cursor.execute（“插入人的價值觀（？，？）”，（who，age））

4 connection.execute（sql [，可選參數]）

該例程是上面執行的由光標（cursor）對象提供的方法的快捷方式，它通過調用光標（cursor）方法創建了一個中間的光標對象，然後通過給定的參數光標光標的執行方法。

5 cursor.executemany（sql，seq_of_parameters）

該例程對seq_of_parameters中的所有參數或映射執行一個SQL命令。

6 connection.executemany（sql [，參數]）

該例程是一個由調用光標（cursor）方法創建的中間的光標對象的快捷方式，然後通過給定的參數調用光標的executemany方法。

7 cursor.executescript（sql_script）

該例程重新接收到腳本，會執行多個SQL語句。它首先執行COMMIT語句，然後執行作為參數指令的SQL腳本。所有的SQL語句應該用分號；分隔。

8 connection.executescript（sql_script）

該例程是一個由調用光標（cursor）方法創建的中間的光標對象的快捷方式，然後通過給定的參數調用光標的executescript方法。

9 connection.total_changes（）

該例程返回自數據庫連接打開以來被修改，插入或刪除的數據庫總行數。

10 connection.commit（）

該方法提交當前的事務。如果您未調用該方法，那麼自您上一次調用commit（）以來進行的任何動作對其他數據庫連接來說是不可見的。

11 connection.rollback（）

該方法回滾自上一次調用commit（）以來對數據庫維護的更改。

12 connection.close（）

該方法關閉數據庫連接。請注意，這不會自動調用commit（）。如果您之前未調用commit（）方法，就直接關閉數據庫連接，您所做的所有更改將全部丟失！

13 cursor.fetchone（）

該方法獲取查詢結果集中的下一行，返回一個單一的序列，當沒有更多可用的數據時，則返回None。

14 cursor.fetchmany（[size = cursor.arraysize]）

該方法獲取查詢結果集中的下一行組，返回一個列表。當沒有更多的可用的行時，則返回一個空的列表。該方法嘗試獲取由大小參數指定的可用多行。

15 cursor.fetchall（）

該例程獲取查詢結果集中所有（剩餘）的行，返回一個列表。當沒有可用的行時，則返回一個空的列表。
'''


class Sqlite_Control():

    def __init__(self, DB_Name='test.db', Table_Name='Test'):
        self.DB_Name = DB_Name
        self.Table_Name = Table_Name
        self.Valute_Count = 1
        self.connect = sqlite3.connect(DB_Name, check_same_thread=False)  # 這裡是連線上一個資料庫如果沒有這個資料庫的話就會建立一個
        self.cursor = self.connect.cursor()  # 獲取遊標cursor

    # ----------------------------------------------------------------------------------------------
    # 創造一表
    # """CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name VARCHAR(10));"""
    def Create_Table(self, SQL_Command):
        print('I JE-Database exec', 'Sqlite_Control - Create_Table : ', SQL_Command, ' in ', datetime.datetime.now(),
              ' \n', sep='  ')
        self.cursor.execute(SQL_Command)
        self.connect.commit()  # 進行資料庫語句的提交操作，不提交則無法生效，每次執行後都要提交

    # ----------------------------------------------------------------------------------------------
    # 插入語句是insert into 加表名 （欄位名， 欄位名）values （對應的值， 對應的值）因為id是主鍵自增，所以就沒有新增他的值
    # SQL_Command="""INSERT INTO student(name) VALUES ("小明");"""
    def Insert_Into(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - Insert_Into : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------

    # 如果有會忽略
    # SQL_Command="""INSERT OR IGNORE INTO student(name) VALUES ("小明");"""
    def Insert_Into_Ignore(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - Insert_Into_Ignore : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------

    # 如果有會取代掉
    # SQL_Command="""INSERT OR REPLACE INTO student(name) VALUES ("小明");"""
    def Insert_Into_Replace(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - Insert_Into_Replace : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------
    # 查詢語句select 加欄位名 查詢表中欄位的資訊 加* 查詢所有的資訊   from 表名
    # SQL_Command="""SELECT id,name from student;"""
    def Select_From(self, SQL_Command, args):
        Result_List = []
        print('I JE-Database exec', 'Sqlite_Control - Select_From : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        Str_List = self.cursor.fetchall()
        Format_String = str(Str_List[0]).replace(r"(", "").replace(r")", "").replace(r"'", "")
        if Format_String.endswith(","): Format_String = Format_String[:-1]
        Result_List += self.cursor.execute('SELECT ' + Format_String + ' FROM ' + self.Table_Name).fetchall()
        print('Sqlite_Control - Select_From Result_List : ', Result_List, '\n')
        return Result_List  # 查詢的結果

    # ----------------------------------------------------------------------------------------------
    # 找出表格不同的值
    def Select_Distinct(self, SQL_Command, args):
        Result_List, Result_Format = [], []
        print('I JE-Database exec', 'Sqlite_Control - Select_Distinct : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        Str_List = self.cursor.fetchall()  # 用一個變數來接受fetchall（）查詢所有這個函式返回的值。
        Format_String = str(Str_List[0]).replace(r"(", "").replace(r")", "").replace(r"'", "")
        if Format_String.endswith(","): Format_String = Format_String[:-1]
        Result_List += self.cursor.execute('SELECT Distinct ' + Format_String + ' FROM ' + self.Table_Name).fetchall()
        print('Sqlite_Control - Select_Distinct Result_List : ', Result_List, '\n')
        return Result_List

    # ----------------------------------------------------------------------------------------------

    # select * from  表名 where   加上條件，不加的話就是查詢所有
    # SQL_Command= """SELECT * FROM student WHERE name="小明";"""
    def Select_Where(self, Field, SQL_Command, args):
        Result_List = []
        print('I JE-Database exec', 'Sqlite_Control - Select_Where : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        Str_List = self.cursor.fetchall()  # 用一個變數來接受fetchall（）查詢所有這個函式返回的值。
        Format_String = str(Str_List[0]).replace(r"(", "").replace(r")", "").replace(r"'", "")
        if Format_String.endswith(","):
            Format_String = Format_String[:-1]
        else:
            Format_String.split(',')
        print(Format_String, 'Format_String')
        Result_List += self.cursor.execute(
                'SELECT ' + Format_String + ' FROM ' + self.Table_Name + ''' WHERE ''' + Format_String + '''="''' + str(
                args[len(args)-self.Valute_Count])+'''"''').fetchall()
        print('Sqlite_Control - Select_Where Result_List : ', Result_List, '\n')
        return Result_List

    # ----------------------------------------------------------------------------------------------
    # 更新資料庫語句 update 加表名 set 欄位名=要更新的值  where 限定條件 ，如果不加where 和後面的條件，將會全部生效
    # SQL_Command="""UPDATE student SET name="大紅" WHERE id=1;"""
    def UPDATE(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - UPDATE : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------
    # 刪除語句   delete from 表名 where 範圍，不加where將會刪除整個表但是表的結構還存在就是相當於回到了剛剛建立表的時候
    # SQL_Command= """DELETE FROM student WHERE id = 1;"""
    def DELETE(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - DELETE : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command, args)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------
    # 丟棄表
    # SQL_Command="""DROP TABLE student;"""
    def Drop(self, SQL_Command, args):
        print('I JE-Database exec', 'Sqlite_Control - Drop : ', SQL_Command, 'args=', args, ' in ',
              datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.execute(SQL_Command)
        self.connect.commit()

    # ----------------------------------------------------------------------------------------------
    # 回滾
    # 回復到上一次commit 以來的 改變
    def Rollback(self):
        print('I JE-Database exec', 'Sqlite_Control - Rollback : ', ' in ', datetime.datetime.now(), ' \n', sep='  ')
        self.connect.rollback()

    # ----------------------------------------------------------------------------------------------
    # 關閉
    def Close(self):
        print('I JE-Database exec', 'Sqlite_Control - Close : ', ' in ', datetime.datetime.now(), ' \n', sep='  ')
        self.cursor.close()  # 關閉遊標
        self.connect.close()  # 關閉資料庫連線，在進行完操作之後需要將遊標和連線關閉
