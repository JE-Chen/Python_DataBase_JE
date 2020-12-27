import datetime
import sqlite3

from JELogSystem import LogSystem


class SqliteControl:

    def __init__(self, db_name: str = 'test.sqlite', table_name: str = 'Test'):
        self.db_name = db_name
        self.table_name = table_name
        self.value_count = 1
        self.connect = sqlite3.connect(db_name, check_same_thread=False)  # 這裡是連線上一個資料庫如果沒有這個資料庫的話就會建立一個
        self.cursor = self.connect.cursor()  # 獲取遊標cursor
        self.LogSystem = LogSystem()

    def __process_select_list(self, sql_command, args, what_select):
        result_list = []
        for row in self.cursor.execute(sql_command, args).fetchall():
            result_list.append(row)
        # import itertools
        # result_list = list(itertools.chain(*result_list))
        print('SqliteControl : ' + what_select, result_list, '\n')
        self.LogSystem.warning('SqliteControl : ' + what_select + ' ' + str(result_list) + ' \n')
        return result_list

    def __process_select_list_noargs(self, sql_command, what_select):
        result_list = []
        for row in self.cursor.execute(sql_command).fetchall():
            result_list.append(row)
        import itertools
        result_list = list(itertools.chain(*result_list))
        print('SqliteControl : ' + what_select, result_list, '\n')
        self.LogSystem.warning('SqliteControl : ' + what_select + ' ' + str(result_list) + ' \n')
        return result_list

    @staticmethod
    def __sql_log(sql_command_type, sql_command, args):
        print(sql_command, args)
        print('SqliteControl : ', sql_command_type, ' in ', datetime.datetime.now(), '\n', sep=' ')
        LogSystem().warning('SqliteControl : ' + sql_command_type + ' in ' + str(datetime.datetime.now()) + ' \n')

    def create_table(self, sql_command):
        self.__sql_log('create_table', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()

    def insert_into(self, sql_command, args):
        self.__sql_log('insert_into', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def insert_into_ignore(self, sql_command, args):
        self.__sql_log('insert_into_ignore', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def insert_into_replace(self, sql_command, args):
        self.__sql_log('insert_into_replace', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def select_from(self, sql_command, args):
        self.__sql_log('select_from', sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_from')

    def select_distinct(self, sql_command, args):
        self.__sql_log('select_distinct', sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_distinct')

    def select_where(self, sql_command, args):
        self.__sql_log('select_where', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where')

    def select_where_and(self, sql_command, args):
        self.__sql_log('select_where_and', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where_and')

    def select_where_like(self, field, sql_command, args):
        print("field : " + field)
        self.__sql_log('select_where_like', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where_like')

    def select_account(self, sql_command, args):
        self.__sql_log('select_account', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_account')

    def inner_join(self, sql_command):
        self.__sql_log('inner_join', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join')

    def inner_inner_join(self, sql_command):
        self.__sql_log('inner_inner_join', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_inner_join')

    def inner_join_where(self, sql_command):
        self.__sql_log('inner_join_where', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join_where')

    def inner_inner_join_where(self, sql_command):
        self.__sql_log('inner_inner_join_where', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_inner_join_where')

    def update(self, sql_command, args):
        self.__sql_log('update', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def delete(self, sql_command, args):
        self.__sql_log('delete', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def drop(self, sql_command):
        self.__sql_log('drop', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()

    def rollback(self):
        self.__sql_log('rollback', 'rollback', '')
        self.connect.rollback()

    def close(self):
        self.__sql_log('close', 'Close', '')
        self.cursor.close()
        self.connect.close()

    def test_sql(self, sql_command):
        self.__sql_log('test_sql', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()
