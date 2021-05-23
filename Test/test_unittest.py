import unittest

from je_database.core.sqlite_core import sqlite_core


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.SQL = sqlite_core(r'TestAccount.sqlite', table_name='Account')
        self.SQL.create_table(
            'CREATE TABLE IF NOT EXISTS Account(id VARCHAR(20),email VARCHAR(50),password VARCHAR(15))')

    def tearDown(self) -> None:
        self.SQL.close()

    def testInsert(self):
        self.SQL.insert_into_ignore(1, 'test1@gmail.com', 'test_password')
        self.SQL.insert_into_ignore(2, 'test2@gmail.com', 'test_password')
        self.SQL.insert_into_ignore(3, 'test3@gmail.com', 'test_password')

    def testDelete(self):
        self.SQL.delete('email', 'test1@gmail.com')

    def testSelect(self):
        self.SQL.select_form()
        self.SQL.select_distinct()

    def testUpdate(self):
        self.SQL.update('email', 'email', 'new_test@gmail.com', 'test_password')

    def testSelectAccount(self):
        self.SQL.select_prefix = '*'
        self.SQL.table_name = 'Account'
        self.SQL.select_account('email', 'password', 'new_test@gmail.com', 'test_password')


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestDatabase))
    unittest.TextTestRunner(verbosity=2).run(suite)
