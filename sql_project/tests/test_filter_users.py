import sqlite3
from unittest.mock import patch, mock_open

import pytest

from sql_project.join_users_purchases import read, parse, prepare_db_tables


@pytest.fixture()
def users_table():

@pytest.fixture()
def select_check(con, field: str, value: str, table_name: str):
    con_cursor = con.cursor()
    t = (value,)
    con_cursor.execute("SELECT * FROM {} WHERE {}=?".format(table_name, field), t)
    return con_cursor.fetchone()

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


def test_prepare_db_tables(in_memory_db_connection):
    con = in_memory_db_connection()
    with con:
        prepare_db_tables(con, USERS, PURCHASES)
        select_result = select_check(con, field="name", value="Vasia", table_name=USERS.table_name)
