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
        except Exception as Errors:
            print(datetime.datetime.now(), 'I JE-Database Error', sep=' ')
            raise Errors

        self.table_name = table_name
        self.value_count = 2
        self.SQLite_Cursor = self.SqliteControl.cursor
        self.SQLite_Connect = self.SqliteControl.connect

        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')

    def set_table_name(self, table_name):
        self.table_name = table_name

    def set_value_count(self, value_count):
        self.value_count = value_count
        self.SqliteControl.Value_Count = value_count

    def create_table(self, sql_command):
        self.log.Debug()
        self.SqliteControl.create_table(sql_command)

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

    def update(self, *args, field, where_what=None):
        sql_command = '''UPDATE ''' + self.table_name + ''' SET ''' + field + '''=? WHERE ''' + where_what + '''=?'''
        self.SqliteControl.update(sql_command, args)

    def delete(self, field, *args):
        sql_command = '''DELETE FROM ''' + self.table_name + ''' WHERE ''' + field + ''' =? '''
        self.SqliteControl.delete(sql_command, args)

    def select_form(self, *args):
        if len(args) == 1:
            sql_command = '''SELECT''' + '?' + '''FROM ''' + self.table_name
            return self.SqliteControl.select_from(sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (len(args) - 1) + '?' + ''' FROM ''' + self.table_name
            return self.SqliteControl.select_from(sql_command, args)

    def select_distinct(self, *args):
        if len(args) == 1:
            sql_command = '''SELECT DISTINCT ? FROM ''' + self.table_name
            return self.SqliteControl.select_distinct(sql_command, args)
        else:
            sql_command = '''SELECT DISTINCT''' + '?,' * (len(args) - 1) + '?' + ''' FROM ''' + self.table_name
            return self.SqliteControl.select_distinct(sql_command, args)

    def select_where(self, field, *args):
        if len(args) == 1:
            sql_command = '''SELECT ? FROM ''' + self.table_name + ''' WHERE ''' + field + '''=?'''
            return self.SqliteControl.select_where(field, sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (
                    len(args) - 2) + '?' + ''' FROM ''' + self.table_name + ''' WHERE ''' + field + '''=?'''
            return self.SqliteControl.select_where(field, sql_command, args)

    def select_where_like(self, field, *args):
        if len(args) == 1:
            sql_command = '''SELECT ? FROM ''' + self.table_name + ''' WHERE ''' + field + ''' LIKE ?'''
            return self.SqliteControl.select_where_like(field, sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (
                    len(args) - 2) + '?' + ''' FROM ''' + self.table_name + ''' WHERE ''' + field + ''' LIKE ?'''
            return self.SqliteControl.select_where_like(field, sql_command, args)

    def select_where_any(self, *args):
        if len(args) == 1:
            sql_command = '''SELECT ? FROM ''' + self.table_name + ''' WHERE ''' + '''?'''
            return self.SqliteControl.select_where_any(sql_command, args)
        else:
            sql_command = '''SELECT ''' + '?,' * (
                    len(args) - 2) + '?' + ''' FROM ''' + self.table_name + ''' WHERE ''' + '''?'''
            return self.SqliteControl.select_where_any(sql_command, args)

    def rollback(self):
        self.SqliteControl.rollback()

    def drop(self):
        sql_command = '''DROP TABLE ''' + self.table_name + '''=?'''  # 丟棄表（此操作比delete更加嚴重，會刪除表的結構）drop table 加上表名
        self.SqliteControl.drop(sql_command, self.table_name)

    def close(self):
        self.SqliteControl.close()
