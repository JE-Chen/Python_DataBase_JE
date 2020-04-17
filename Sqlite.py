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
'''


class Sqlite():

    def __init__(self,DB_Name='test.db'):
        self.connect = sqlite3.connect(DB_Name)  # 這裡是連線上一個資料庫“test.db”如果沒有這個資料庫的話就會建立一個
        self.cursor = self.connect.cursor()  # 獲取遊標cursor

# ----------------------------------------------------------------------------------------------
    #創造一格
    def Create_Table(self,SQL_Command="""CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name VARCHAR(10));"""):
        SQL = SQL_Command
        self.cursor.execute(SQL)
        self.connect.commit()  # 進行資料庫語句的提交操作，不提交則無法生效，每次執行後都要提交

# ----------------------------------------------------------------------------------------------
    # 插入語句是insert into 加表名 （欄位名， 欄位名）values （對應的值， 對應的值）因為id是主鍵自增，所以就沒有新增他的值
    def Insert_Into(self,SQL_Command="""INSERT INTO student (name) VALUES ( "小明");""" ):
        SQL = SQL_Command
        self.cursor.execute(SQL)  # 執行sql 語句，連線資料庫和提交關閉資料庫的操作都是一樣的，這裡就不再做說明
        self.connect.commit()

    # 如果有會忽略
    def Insert_Into_Ignore(self,SQL_Command="""INSERT or IGNORE INTO student (name) VALUES ( "小明");""" ):
        SQL = SQL_Command
        self.cursor.execute(SQL)  # 執行sql 語句，連線資料庫和提交關閉資料庫的操作都是一樣的，這裡就不再做說明
        self.connect.commit()

    # 如果有會取代掉
    def Insert_Into_Replace(self,SQL_Command="""INSERT or REPLACE INTO student (name) VALUES ( "小明");""" ):
        SQL = SQL_Command
        self.cursor.execute(SQL)  # 執行sql 語句，連線資料庫和提交關閉資料庫的操作都是一樣的，這裡就不再做說明
        self.connect.commit()

# ----------------------------------------------------------------------------------------------
    # 查詢語句select 加欄位名 查詢表中欄位的資訊 加* 查詢所有的資訊   from 表名
    def Select_From(self,SQL_Command="""SELECT id,name from student;"""):
        SQL = SQL_Command
        self.cursor.execute(SQL)
        student_list = self.cursor.fetchall()  # 用一個變數來接受fetchall（）查詢所有這個函式返回的值。
        print(student_list)  # 打印出查詢的結果

# ----------------------------------------------------------------------------------------------
    # select * from  表名 where   加上條件，不加的話就是查詢所有
    def Select_Where(self,SQL_Command= """SELECT * FROM student WHERE name="小明";""" ):
        SQL= SQL_Command
        self.cursor.execute(SQL)
        student = self.cursor.fetchone()  # fetchone ()是查詢一個，只有一個結果和fetchall有區別
        print(student)

# ----------------------------------------------------------------------------------------------
    # 更新資料庫語句 update 加表名 set 欄位名=要更新的值  where 限定條件 ，如果不加where 和後面的條件，將會全部生效
    def UPDATE(self,SQL_Command="""UPDATE student SET name="大紅" WHERE id=1;""" ):
        SQL=SQL_Command
        self.cursor.execute(SQL)
        self.connect.commit()

# ----------------------------------------------------------------------------------------------
    # 刪除語句   delete from 表名 where 範圍，不加where將會刪除整個表但是表的結構還存在就是相當於回到了剛剛建立表的時候
    def DELETE(self,SQL_Command= """DELETE FROM student WHERE id = 1;"""  ):
        SQL = SQL_Command
        self.cursor.execute(SQL)
        self.connect.commit()

# ----------------------------------------------------------------------------------------------
    #丟棄表
    def Drop(self,SQL_Command= """DROP TABLE student;""" ):
        SQL = SQL_Command # 丟棄表（此操作比delete更加嚴重，會刪除表的結構）drop table 加上表名
        self.cursor.execute(SQL)
        self.connect.commit()

# ----------------------------------------------------------------------------------------------

    #關閉
    def Close(self):
        self.cursor.close()  # 關閉遊標
        self.connect.close()  # 關閉資料庫連線，在進行完操作之後需要將遊標和連線關閉

