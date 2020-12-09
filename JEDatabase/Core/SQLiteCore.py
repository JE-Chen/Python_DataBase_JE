import datetime

from JEDatabase.Models.SqliteControl import SqliteControl


class SQLiteCore:

    def __init__(self, db_name: str = 'test.sqlite', table_name: str = 'Test', name: str = '*'):
        """
        :type db_name: str
        :type table_name: str
        """
        try:
            self.SqliteControl = SqliteControl(db_name, table_name)
            self.table_name = table_name
            self.name = name
            self.value_count = 2
            self.SQLite_Cursor = self.SqliteControl.cursor
            self.SQLite_Connect = self.SqliteControl.connect
            print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
        except Exception as Errors:
            print(datetime.datetime.now(), 'SQLiteCore Error', sep=' ')
            raise Errors

    def set_table_name(self, table_name) -> None:
        self.table_name = table_name

    def set_name(self, name) -> None:
        self.name = name

    def set_value_count(self, value_count) -> None:
        self.value_count = value_count
        self.SqliteControl.Value_Count = value_count

    def create_table(self, sql_command) -> None:
        self.SqliteControl.create_table(sql_command)

    def insert_into(self, *args, field=None) -> None:

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

    def insert_into_ignore(self, *args, field=None) -> None:

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

    def insert_into_replace(self, *args, field=None) -> None:
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

    def update(self, *args, field, where_what=None) -> None:
        sql_command = '''UPDATE ''' + self.table_name + ''' SET ''' + field + '''=? WHERE ''' + where_what + '''=?'''
        self.SqliteControl.update(sql_command, args)

    def delete(self, field, *args) -> None:
        sql_command = '''DELETE FROM ''' + self.table_name + ''' WHERE ''' + field + ''' =? '''
        self.SqliteControl.delete(sql_command, args)

    def select_form(self, *args) -> list:
        sql_command = '''SELECT ''' + self.name + ''' FROM ''' + self.table_name
        return self.SqliteControl.select_from(sql_command, args)

    def select_distinct(self, *args):
        sql_command = '''SELECT DISTINCT ''' + self.name + ''' FROM ''' + self.table_name
        return self.SqliteControl.select_distinct(sql_command, args)

    def select_account(self, *args):
        sql_command = '''SELECT ''' + self.name + ''' FROM ''' + self.table_name + ''' WHERE email = ? AND password = ? LIMIT 1'''
        return self.SqliteControl.select_account(sql_command, args)

    def rollback(self):
        self.SqliteControl.rollback()

    def drop(self):
        sql_command = '''DROP TABLE ''' + self.table_name
        self.SqliteControl.drop(sql_command)

    def close(self):
        self.SqliteControl.close()
