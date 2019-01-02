import sqlite3
from collections import namedtuple
from unittest.mock import patch, mock_open

import pytest

from sql_problem.join_users_purchases import read, parse, prepare_db_tables


@pytest.fixture()
def users_table():
    return "1 | t | vasia@test.ru<mailto:vasia@test.ru> | Vasia\n" \
           "2 | f | tania@test.ru<mailto:tania@test.ru> | Tania"


@pytest.fixture()
def users_purchases():
    namedtuple_fields = ["table_name", "file", "fields", ]
    Users, Purchases = namedtuple("Users", namedtuple_fields), namedtuple("Purchases", namedtuple_fields)
    users = Users("users", "users.txt", "(id INT, confirmed TEXT, email VARCHAR(320), name VARCHAR(320))", )
    purchases = Purchases("purchases", "purchases.txt", "(id INT, user_id INT, date TEXT, sum INT, item_id INT)", )
    return users, purchases


@pytest.fixture()
def in_memory_db_connection():
    return sqlite3.connect(":memory:")


def test_read():
    read_data = "1 | t | Vasia\n" "2 | f | tania@test.ru<mailto:tania@test.ru> | Tania"
    with patch("builtins.open", mock_open(read_data=read_data)):
        lines = read("foobar")
    assert lines[0] == "1 | t | Vasia\n"


def test_parse():
    lines = ["1 | t | vasia@test.ru<mailto:vasia@test.ru> | Vasia\n"]
    table = parse(lines)
    assert table[0][2] == "vasia@test.ru<mailto:vasia@test.ru>"


def test_prepare_db_tables(in_memory_db_connection, users_purchases, users_table):
    users, purchases = users_purchases
    with in_memory_db_connection as con:
        with patch("builtins.open", mock_open(read_data=users_table)):
            prepare_db_tables(con, users)
        con_cursor = con.cursor()
        t = ("Tania",)
        con_cursor.execute("SELECT * FROM {} WHERE {}=?".format("users", "name"), t)
    assert con_cursor.fetchone() == (2, 'f', 'tania@test.ru<mailto:tania@test.ru>', 'Tania')
