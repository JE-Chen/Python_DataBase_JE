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


class sqlite_control:

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

    def process_select_list(self, sql_command, args, what_select):
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

    def process_select_list_noargs(self, sql_command, what_select, no_arg):
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

    def exec_sql_with_log(self, sql_command_type, sql_command, args):
        """
        :param sql_command_type: what sql command
        :param sql_command: full sql command
        :param args: values to log
        """
        print(sql_command, args)
        print('SqliteControl : ', sql_command_type, ' in ', datetime.datetime.now(), '\n', sep=' ')
        if self.LogSystem is not None:
            self.LogSystem.log_debug(
                'SqliteControl : ' + sql_command_type + ' in ' + str(datetime.datetime.now()) + ' \n')
        self.cursor.execute(sql_command, args)
        self.connect.commit()

    # rollback database
    def rollback(self):
        self.connect.rollback()

    # close database
    def close(self):
        self.cursor.close()
        self.connect.close()

