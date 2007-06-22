from storm.databases.sqlite import SQLite
from storm.uri import URI

from tests.store.base import StoreTest, EmptyResultSetTest
from tests.helper import TestHelper, MakePath


class SQLiteStoreTest(TestHelper, StoreTest):

    helpers = [MakePath]

    def setUp(self):
        TestHelper.setUp(self)
        StoreTest.setUp(self)

    def tearDown(self):
        TestHelper.tearDown(self)
        StoreTest.tearDown(self)

    def create_database(self):
        self.database = SQLite(URI("sqlite:" + self.make_path()))

    def create_tables(self):
        connection = self.database.connect()
        connection.execute("CREATE TABLE foo "
                           "(id INTEGER PRIMARY KEY,"
                           " title VARCHAR DEFAULT 'Default Title')")
        connection.execute("CREATE TABLE bar "
                           "(id INTEGER PRIMARY KEY,"
                           " foo_id INTEGER, title VARCHAR)")
        connection.execute("CREATE TABLE bin "
                           "(id INTEGER PRIMARY KEY, bin BLOB)")
        connection.execute("CREATE TABLE link "
                           "(foo_id INTEGER, bar_id INTEGER)")
        connection.commit()

    def drop_tables(self):
        pass


class SQLiteEmptyResultSetTest(TestHelper, EmptyResultSetTest):

    helpers = [MakePath]

    def setUp(self):
        TestHelper.setUp(self)
        EmptyResultSetTest.setUp(self)

    def tearDown(self):
        TestHelper.tearDown(self)
        EmptyResultSetTest.tearDown(self)

    def create_database(self):
        self.database = SQLite(URI("sqlite:" + self.make_path()))

    def create_tables(self):
        connection = self.database.connect()
        connection.execute("CREATE TABLE foo "
                           "(id INTEGER PRIMARY KEY,"
                           " title VARCHAR DEFAULT 'Default Title')")
        connection.commit()

    def drop_tables(self):
        pass
