import sqlite3
from collections import namedtuple

DATABASE = ":memory:"

NAMEDTUPLE_FIELDS = ["tablename", "file", "fields", "fields_template"]
Users, Purchases = namedtuple("Users", NAMEDTUPLE_FIELDS), namedtuple("Purchases", NAMEDTUPLE_FIELDS)
USERS = Users(
    "users", "users.txt", "(id INT, confirmed TEXT, email VARCHAR(320), name VARCHAR(320))", "(?, ?, ?, ?)",
)
PURCHASES = Purchases(
    "purchases", "purchases.txt", "(id INT, user_id INT, date TEXT, sum INT, item_id INT)", "(?, ?, ?, ?, ?)",
)


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


def insert_many(con, table_name: str, field_template: str, table: [(str)]):
    con.executemany("INSERT INTO {} VALUES {}".format(table_name, field_template), table)


def prepare_db_tables(con, *table_data_seq):
    for table_data in table_data_seq:
        lines = read(table_data.file)
        table = parse(lines)
        create_db_table(con, table_name=table_data.tablename, table_fields=table_data.fields)
        insert_many(con, table_name=table_data.tablename, field_template=table_data.fields_template, table=table)


def select_check(con, field: str, value: str, table_name: str):
    con_cursor = con.cursor()
    t = (value,)
    con_cursor.execute("SELECT * FROM {} WHERE {}=?".format(table_name, field), t)
    print(con_cursor.fetchone())


def select_join(con):
    """Вывести email, имя и сумму всех покупок подтвержденных пользователей за 2 и 3 сентября"""
    con_cursor = con.cursor()
    t = ('t',)
    con_cursor.execute("SELECT users.id FROM users INNER JOIN purchases ON users.id = purchases.user_id")
    view_data = con_cursor.fetchall()
    print(view_data)


if __name__ == "__main__":
    con = create_db_connection()
    with con:
        prepare_db_tables(con, USERS, PURCHASES)
        select_check(con, field="name", value="Vasia", table_name=USERS.tablename)
        select_check(con, field="item_id", value="1345", table_name=PURCHASES.tablename)
        select_join(con)
