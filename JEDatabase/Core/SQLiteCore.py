import datetime

from JEDatabase.Models.SqliteControl import SqliteControl


class SQLiteCore:

    def __init__(self, db_name: str = 'test.sqlite', table_name: str = 'Test', select_prefix: str = '*'):
        """
        :type db_name: str
        :type table_name: str
        """
        try:
            self.SqliteControl = SqliteControl(db_name, table_name)
            self.table_name = table_name
            self.select_prefix = select_prefix
            self.value_count = 2
            self.SQLite_Cursor = self.SqliteControl.cursor
            self.SQLite_Connect = self.SqliteControl.connect
            print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
        except Exception as Errors:
            print(datetime.datetime.now(), 'SQLiteCore Error', sep=' ')
            raise Errors

    # set now use table name
    def set_table_name(self, table_name) -> None:
        self.table_name = table_name

    # set select prefix
    def set_name(self, name) -> None:
        self.select_prefix = name

    # set value count -> how many col
    def set_value_count(self, value_count) -> None:
        self.value_count = value_count
        self.SqliteControl.Value_Count = value_count

    # call sql control to create table
    def create_table(self, sql_command) -> None:
        self.SqliteControl.create_table(sql_command)

    # call sql control to insert into
    def insert_into(self, *args) -> None:
        if len(args) == 1:
            sql_command = '''INSERT INTO ''' + self.table_name + \
                          ''' VALUES (?)'''
        else:
            sql_command = '''INSERT INTO ''' + self.table_name + \
                          ''' VALUES (''' + '?,' * (
                                  len(args) - 1) + '?' + ''')'''
        self.SqliteControl.insert_into(sql_command, args)

    # call sql control to insert into ignore
    def insert_into_ignore(self, *args) -> None:
        if len(args) == 1:
            sql_command = '''INSERT OR IGNORE INTO ''' + self.table_name + \
                          ''' VALUES (?)'''
        else:
            sql_command = '''INSERT OR IGNORE INTO ''' + self.table_name + \
                          ''' VALUES (''' + '?,' * (
                                  len(args) - 1) + '?' + ''')'''
        self.SqliteControl.insert_into_ignore(sql_command, args)

    # call sql control to insert into replace
    def insert_into_replace(self, *args) -> None:
        if len(args) == 1:
            sql_command = '''REPLACE INTO ''' + self.table_name + \
                          ''' VALUES (?)'''
        else:
            sql_command = '''REPLACE INTO ''' + self.table_name + \
                          ''' VALUES (''' + '?,' * (
                                  len(args) - 1) + '?' + ''')'''
        self.SqliteControl.insert_into_replace(sql_command, args)

    # call sql control to update
    def update(self, field, where_what, *args) -> None:
        sql_command = '''UPDATE ''' + self.table_name + \
                      ''' SET ''' + field + '''=? ''' + \
                      '''WHERE ''' + where_what + '''=?'''
        self.SqliteControl.update(sql_command, args)

    # call sql control to update two col
    def update_two(self, field1, field2, where_what, *args) -> None:
        sql_command = '''UPDATE ''' + self.table_name + \
                      ''' SET ''' + field1 + '''=?,''' + field2 + '''=? ''' + \
                      '''WHERE ''' + where_what + '''=?'''
        self.SqliteControl.update(sql_command, args)

    # call sql control to update and
    def update_and(self, field, where_what1, where_what2, *args) -> None:
        sql_command = '''UPDATE ''' + self.table_name + \
                      ''' SET ''' + field + '''=? ''' + \
                      '''WHERE ''' + where_what1 + '''=?''' + \
                      ''' AND ''' + where_what2 + '''=?'''
        self.SqliteControl.update(sql_command, args)

    # call sql control to update and two col
    def update_and_two(self, field1, field2, where_what1, where_what2, *args) -> None:
        sql_command = '''UPDATE ''' + self.table_name + \
                      ''' SET ''' + field1 + '''=?,''' + field2 + '''=? ''' + \
                      '''WHERE ''' + where_what1 + '''=?''' + \
                      ''' AND ''' + where_what2 + '''=?'''
        self.SqliteControl.update(sql_command, args)

    # call sql control to delete
    def delete(self, where1, *args) -> None:
        sql_command = '''DELETE FROM ''' + self.table_name + \
                      ''' WHERE ''' + where1 + ''' =? '''
        self.SqliteControl.delete(sql_command, args)

    # call sql control to select form
    def select_form(self, *args) -> list:
        sql_command = '''SELECT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name
        return self.SqliteControl.select_from(sql_command, args)

    # call sql control to select where
    def select_where(self, where1, *args) -> list:
        sql_command = '''SELECT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name + \
                      ''' WHERE ''' + where1 + '''=?'''
        return self.SqliteControl.select_where(sql_command, args)

    # call sql control to select where and
    def select_where_and(self, where1, where2, *args) -> list:
        sql_command = '''SELECT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name + \
                      ''' WHERE ''' + where1 + '''=?''' + \
                      ''' AND ''' + where2 + '''=?'''
        return self.SqliteControl.select_where(sql_command, args)

    # call sql control to select distinct
    def select_distinct(self, *args):
        sql_command = '''SELECT DISTINCT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name
        return self.SqliteControl.select_distinct(sql_command, args)

    # call sql control to select account
    def select_account(self, where1, where2, *args):
        sql_command = '''SELECT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name + \
                      ''' WHERE ''' + where1 + ''' = ? ''' + \
                      '''AND + ''' + where2 + ''' = ? LIMIT 1'''
        return self.SqliteControl.select_account(sql_command, args)

    # call sql control to inner join distinct
    def inner_join_distinct(self, inner_join_name, inner_join_field1, inner_join_field2, no_arg=None):
        sql_command = '''SELECT DISTINCT ''' + self.select_prefix + \
                      ''' FROM ''' + self.table_name + \
                      ''' INNER JOIN ''' + inner_join_name + \
                      ''' on ''' + inner_join_field1 + ''' = ''' + inner_join_field2
        return self.SqliteControl.inner_join_distinct(sql_command, no_arg)

    # call sql control to inner inner join distinct
    def inner_inner_join_distinct(self, inner_join_name1, inner_join_field1, inner_join_field2,
                                  inner_join_name2, inner_join_field3, inner_join_field4, no_arg=None):
        sql_command = \
            '''SELECT DISTINCT ''' + self.select_prefix + \
            ''' FROM ''' + self.table_name + \
            ''' INNER JOIN ''' + inner_join_name1 + \
            ''' on ''' + inner_join_field1 + ''' = ''' + inner_join_field2 + \
            ''' INNER JOIN ''' + inner_join_name2 + \
            ''' on ''' + inner_join_field3 + ''' = ''' + inner_join_field4
        return self.SqliteControl.inner_inner_join_distinct(sql_command, no_arg)

    # call sql control to inner join where
    def inner_join_where(self, inner_join_name, where1, where2, no_arg=None):
        sql_command = \
            '''SELECT ''' + self.select_prefix + \
            ''' FROM ''' + self.table_name + \
            ''' INNER JOIN ''' + inner_join_name + \
            ''' WHERE ''' + where1 + ''' = ''' + where2
        return self.SqliteControl.inner_join_where(sql_command, no_arg)

    # call sql control to inner join where and
    def inner_join_where_and(self, inner_join_name, where1, where2, and1, and2, no_arg=None):
        sql_command = \
            '''SELECT ''' + self.select_prefix + \
            ''' FROM ''' + self.table_name + \
            ''' INNER JOIN ''' + inner_join_name + \
            ''' WHERE ''' + where1 + ''' = ''' + where2 + \
            ''' AND ''' + and1 + ''' = ''' + and2
        return self.SqliteControl.inner_join_where_and(sql_command, no_arg)

    # call sql control to inner join where distinct
    def inner_join_where_distinct(self, inner_join_name, inner_join_field1, inner_join_field2, where1, where2,
                                  no_arg=None):
        sql_command = \
            '''SELECT DISTINCT ''' + self.select_prefix + \
            ''' FROM ''' + self.table_name + \
            ''' INNER JOIN ''' + inner_join_name + \
            ''' on ''' + inner_join_field1 + ''' = ''' + inner_join_field2 + \
            ''' WHERE ''' + where1 + ''' = ''' + where2
        return self.SqliteControl.inner_join_where_distinct(sql_command, no_arg)

    # call sql control to inner inner join where distinct
    def inner_inner_join_where_distinct(self, inner_join_name1, inner_join_field1, inner_join_field2,
                                        inner_join_name2, inner_join_field3, inner_join_field4, where1, where2,
                                        no_arg=None):
        sql_command = \
            '''SELECT DISTINCT ''' + self.select_prefix + \
            ''' FROM ''' + self.table_name + \
            ''' INNER JOIN ''' + inner_join_name1 + \
            ''' on ''' + inner_join_field1 + ''' = ''' + inner_join_field2 + \
            ''' INNER JOIN ''' + inner_join_name2 + \
            ''' on ''' + inner_join_field3 + ''' = ''' + inner_join_field4 + \
            ''' WHERE ''' + where1 + ''' = ''' + "'" + where2 + "'"
        return self.SqliteControl.inner_inner_join_where_distinct(sql_command, no_arg)

    # call sql control to rollback
    def rollback(self):
        self.SqliteControl.rollback()

    # call sql control to drop
    def drop(self):
        sql_command = '''DROP TABLE ''' + self.table_name
        self.SqliteControl.drop(sql_command)

    # call sql control to close
    def close(self):
        self.SqliteControl.close()

    # call sql control to test
    def test_sql(self, sql_command):
        self.SqliteControl.test_sql(sql_command)
