import unittest

from JEDatabase.Core.SQLiteCore import SQLiteCore


class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.SQL = SQLiteCore(r'TestAccount.sqlite', table_name='Account')
        self.SQL.create_table(
            'CREATE TABLE IF NOT EXISTS Account(id PRIMARY KEY ,email VARCHAR(50),password VARCHAR(15))')

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
        self.SQL.update('new_test@gmail.com', 'test2@gmail.com', field='email', where_what='email')

    def testSelectAccount(self):
        self.SQL.select_account('new_test@gmail.com', 'test_password')


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestDatabase))
    unittest.TextTestRunner(verbosity=2).run(suite)
