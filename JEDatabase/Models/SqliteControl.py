import datetime
import sqlite3
import sys
import threading

isImportJELogSystemSuccess = False

try:
    from JELogSystem import LogSystem
    isImportJELogSystemSuccess = True
except ImportError:
    print("Log is disable install JELogSystem to open", file=sys.stderr)

"""
Use SQLiteCore not this class
this class is a function class for SQLiteCore 
"""


class SqliteControl:

    def __init__(self, db_name: str = 'test.sqlite'):
        """
        :param db_name: Database's name
        """
        self.db_name = db_name
        # how many col
        self.value_count = 1
        self.connect = sqlite3.connect(db_name, check_same_thread=True)
        self.cursor = self.connect.cursor()
        # LogSystem https://github.com/JE-Chen/Python_LogSystem
        if isImportJELogSystemSuccess:
            self.LogSystem = LogSystem(threading.Lock)

    def __process_select_list(self, sql_command, args, what_select):
        """
        :param sql_command: sql command
        :param args: value
        :param what_select: select value
        :return: Select data
        """
        result_list = []
        for row in self.cursor.execute(sql_command, args).fetchall():
            result_list.append(row)
        # when you don't want to get multi list
        # import itertools
        # result_list = list(itertools.chain(*result_list))
        print('SqliteControl : ' + what_select, result_list, '\n')
        if self.LogSystem is not None:
            self.LogSystem.log_debug('SqliteControl : ' + what_select + ' ' + str(result_list) + ' \n')
        return result_list

    def __process_select_list_noargs(self, sql_command, what_select, no_arg):
        """
        :param sql_command: sql command
        :param what_select: select what
        :param no_arg: null value to get one list
        :return: Select data
        """
        result_list = []
        for row in self.cursor.execute(sql_command).fetchall():
            result_list.append(row)
        if no_arg is None:
            import itertools
            result_list = list(itertools.chain(*result_list))
        print('SqliteControl : ' + what_select, result_list, '\n')
        if self.LogSystem is not None:
            self.LogSystem.log_debug('SqliteControl : ' + what_select + ' ' + str(result_list) + ' \n')
        return result_list

    def __sql_log(self, sql_command_type, sql_command, args):
        """
        :param sql_command_type: what sql command
        :param sql_command: full sql command
        :param args: values to log
        """
        print(sql_command, args)
        print('SqliteControl : ', sql_command_type, ' in ', datetime.datetime.now(), '\n', sep=' ')
        if self.LogSystem is not None:
            self.LogSystem.log_debug('SqliteControl : ' + sql_command_type + ' in ' + str(datetime.datetime.now()) + ' \n')

    def create_table(self, sql_command):
        """
        :param sql_command: full sql command to create table
        """
        self.__sql_log('create_table', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()

    def insert_into(self, sql_command, args):
        """
        :param sql_command: sql_command: full sql command to insert into
        :param args: insert values
        """
        self.__sql_log('insert_into', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def insert_into_ignore(self, sql_command, args):
        """
        :param sql_command: full sql command to insert into ignore
        :param args: insert into ignore value
        """
        self.__sql_log('insert_into_ignore', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def insert_into_replace(self, sql_command, args):
        """
        :param sql_command: full sql command to insert into replace
        :param args: insert into replace value
        """
        self.__sql_log('insert_into_replace', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    def select_from(self, sql_command, args):
        """
        :param sql_command: full sql command to select from
        :param args: select from value
        """
        self.__sql_log('select_from', sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_from')

    def select_distinct(self, sql_command, args):
        """
        :param sql_command: full sql command to select distinct
        :param args: select distinct value
        """
        self.__sql_log('select_distinct', sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_distinct')

    def select_where(self, sql_command, args):
        """
        :param sql_command: full sql command to select where
        :param args: select where value
        """
        self.__sql_log('select_where', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where')

    def select_where_and(self, sql_command, args):
        """
        :param sql_command: full sql command to select where and
        :param args: select where and value
        """
        self.__sql_log('select_where_and', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where_and')

    def select_where_like(self, field, sql_command, args):
        """
        :param field: where field
        :param sql_command: full sql command to select where like
        :param args: select where like
        """
        print("field : " + field)
        self.__sql_log('select_where_like', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_where_like')

    def select_account(self, sql_command, args):
        """
        :param sql_command: full sql command to select account
        :param args: select account value
        """
        self.__sql_log('select_account', sql_command, args)
        self.cursor.execute(sql_command, args)
        return self.__process_select_list(sql_command, args, 'select_account')

    def inner_join_distinct(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner join distinct
        :param no_arg: inner join distinct value
        """
        self.__sql_log('inner_join_distinct', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join_distinct', no_arg)

    def inner_inner_join_distinct(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner inner join distinct
        :param no_arg: inner inner join distinct value
        """
        self.__sql_log('inner_inner_join_distinct', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_inner_join_distinct', no_arg)

    def inner_join_where(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner join where
        :param no_arg: inner join where value
        """
        self.__sql_log('inner_join_where', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join_where', no_arg)

    def inner_join_where_and(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner join where and
        :param no_arg: inner join where and value
        """
        self.__sql_log('inner_join_where_and', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join_where_and', no_arg)

    def inner_join_where_distinct(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner join where distinct
        :param no_arg: inner join where distinct value
        """
        self.__sql_log('inner_join_where_distinct', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_join_where_distinct', no_arg)

    def inner_inner_join_where_distinct(self, sql_command, no_arg):
        """
        :param sql_command: full sql command to inner inner join where distinct
        :param no_arg: inner inner join where distinct value
        """
        self.__sql_log('inner_inner_join_where_distinct', sql_command, args='')
        self.cursor.execute(sql_command)
        return self.__process_select_list_noargs(sql_command, 'inner_inner_join_where_distinct', no_arg)

    # update col
    def update(self, sql_command, args):
        self.__sql_log('update', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    # delete col
    def delete(self, sql_command, args):
        self.__sql_log('delete', sql_command, args)
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    # drop table
    def drop(self, sql_command):
        self.__sql_log('drop', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()

    # rollback database
    def rollback(self):
        self.__sql_log('rollback', 'rollback', '')
        self.connect.rollback()

    # close database
    def close(self):
        self.__sql_log('close', 'Close', '')
        self.cursor.close()
        self.connect.close()

    # test sql command
    def test_sql(self, sql_command):
        self.__sql_log('test_sql', sql_command, '')
        self.cursor.execute(sql_command)
        self.connect.commit()
