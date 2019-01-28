import sqlite3
from collections import namedtuple
from prettytable import PrettyTable

DATABASE = ":memory:"

META_FIELDS = ["table_name", "file", "fields", ]
Users, Purchases = namedtuple("Users", META_FIELDS), namedtuple("Purchases", META_FIELDS)
USERS_META = Users("users", "users.txt", "(id INT, confirmed TEXT, email VARCHAR(320), name VARCHAR(320))", )
PURCHASES_META = Purchases("purchases", "purchases.txt", "(id INT, user_id INT, date TEXT, sum INT, item_id INT)", )


def read(txt_file):
    with open(txt_file) as f:
        return f.readlines()


def parse(lines):
    table = []
    for line in lines:
        line = line.strip("\n").split("|")
        values = tuple(value.strip() for value in line if value != "")
        table.append(values)
    return table


def create_db_connection(database=DATABASE):
    return sqlite3.connect(database)


def create_db_table(con, table_name: str, table_fields: str):
    con.execute("create table {} {}".format(table_name, table_fields))


def insert_many(con, table_name: str, table: [(str)]):
    con_cursor = con.cursor()
    con_cursor.execute("PRAGMA table_info({})".format(table_name))
    field_count = len(con_cursor.fetchall())
    field_template = '({})'.format(','.join(['?'] * field_count))
    con.executemany("INSERT INTO {} VALUES {}".format(table_name, field_template), table)


def prepare_db_tables(con, *table_obj_seq):
    for table_obj in table_obj_seq:
        lines = read(table_obj.file)
        table = parse(lines)
        create_db_table(con, table_name=table_obj.table_name, table_fields=table_obj.fields)
        insert_many(con, table_name=table_obj.table_name, table=table)


def cursor_execute(con, query: str):
    con_cursor = con.cursor()
    con_cursor.execute(query)
    return con_cursor


def display(con_cursor, fetch_method="fetchall"):
    field_names = list(map(lambda x: x[0], con_cursor.description))
    query_result = getattr(con_cursor, fetch_method)()

    x = PrettyTable()
    x.field_names = field_names
    for obj in query_result:
        x.add_row(list(obj))
    print(x)


if __name__ == "__main__":
    JOIN_QUERY = """\
    SELECT name, email, SUM(sum) as total FROM purchases \
    INNER JOIN users ON users.id = purchases.user_id \
    WHERE confirmed='t' \
    AND purchases.date LIKE '2017-09-02%' OR purchases.date LIKE '2017-09-03%' \
    GROUP BY name"""
    con = create_db_connection()
    with con:
        prepare_db_tables(con, USERS_META, PURCHASES_META)
        join_result = cursor_execute(con, query=JOIN_QUERY)
    display(join_result)
