from sql_project.filter_users import read, parse
from unittest.mock import patch, mock_open


def test_read():
    read_data = "1 | t | Vasia\n" "2 | f | tania@test.ru<mailto:tania@test.ru> | Tania"
    with patch("builtins.open", mock_open(read_data=read_data)):
        lines = read("foobar")
    assert lines[0] == "1 | t | Vasia\n"


def test_parse():
    lines = ["1 | t | vasia@test.ru<mailto:vasia@test.ru> | Vasia\n"]
    table = parse(lines)
    assert table[0][2] == "vasia@test.ru<mailto:vasia@test.ru>"
