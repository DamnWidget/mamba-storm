import os

from storm.database import create_database

from tests.store.base import StoreTest
from tests.helper import TestHelper


class MySQLStoreTest(TestHelper, StoreTest):

    def setUp(self):
        TestHelper.setUp(self)
        StoreTest.setUp(self)

    def tearDown(self):
        TestHelper.tearDown(self)
        StoreTest.tearDown(self)

    def is_supported(self):
        return bool(os.environ.get("STORM_MYSQL_URI"))

    def create_database(self):
        self.database = create_database(os.environ["STORM_MYSQL_URI"])

    def create_tables(self):
        connection = self.database.connect()
        connection.execute("CREATE TABLE test "
                           "(id INT PRIMARY KEY AUTO_INCREMENT,"
                           " title VARCHAR(50) DEFAULT 'Default Title') "
                           "TYPE=InnoDB")
        connection.execute("CREATE TABLE other "
                           "(id INT PRIMARY KEY AUTO_INCREMENT,"
                           " test_id INTEGER, other_title VARCHAR(50)) "
                           "TYPE=InnoDB")
        connection.execute("CREATE TABLE bin "
                           "(id INT PRIMARY KEY AUTO_INCREMENT,"
                           " bin BLOB) "
                           "TYPE=InnoDB")
        connection.execute("CREATE TABLE link "
                           "(test_id INTEGER, other_id INTEGER) "
                           "TYPE=InnoDB")
        connection.commit()