import sqlite3
from collections import namedtuple

DATABASE = ":memory:"

NAMEDTUPLE_FIELDS = ["table_name", "file", "fields",]
Users, Purchases = namedtuple("Users", NAMEDTUPLE_FIELDS), namedtuple("Purchases", NAMEDTUPLE_FIELDS)
USERS = Users("users", "users.txt", "(id INT, confirmed TEXT, email VARCHAR(320), name VARCHAR(320))",)
PURCHASES = Purchases("purchases", "purchases.txt", "(id INT, user_id INT, date TEXT, sum INT, item_id INT)",)


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
    field_template = '({})'.format(','.join(['?']*field_count))
    con.executemany("INSERT INTO {} VALUES {}".format(table_name, field_template), table)


def prepare_db_tables(con, *table_obj_seq):
    for table_obj in table_obj_seq:
        lines = read(table_obj.file)
        table = parse(lines)
        create_db_table(con, table_name=table_obj.table_name, table_fields=table_obj.fields)
        insert_many(con, table_name=table_obj.table_name, table=table)





def select_join(con):
    """Вывести email, имя и сумму всех покупок подтвержденных пользователей за 2 и 3 сентября"""
    con_cursor = con.cursor()
    con_cursor.execute(
        "SELECT users.email, users.name, purchases.sum FROM users "
        "INNER JOIN purchases ON users.id = purchases.user_id "
        "WHERE purchases.date LIKE '2017-09-02%' OR purchases.date LIKE '2017-09-03%' "
        "AND users.confirmed='t'"
    )
    return con_cursor.fetchall()


def display(query):
    for obj in query:
        print(obj)


if __name__ == "__main__":
    con = create_db_connection()
    with con:
        prepare_db_tables(con, USERS, PURCHASES)
        # select_check(con, field="name", value="Vasia", table_name=USERS.table_name)
        # select_check(con, field="item_id", value="1345", table_name=PURCHASES.table_name)
        join_result = select_join(con)
    display(join_result)
