from .string_utils import StringUtils
import pytest

utils = StringUtils

#==================================================================================================================ПОЗИТИВНЫЕ========================================================================================================================================

@pytest.mark.parametrize("input_str, expected", [
    ("apple", "Apple"),
    ("111", "111"),
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("   apple", "apple"),
    ("   111", "111"),
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
])
def test_to_list(input_str, delimiter, expected):
    assert utils.to_list(input_str, delimiter) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
])
def test_contains(input_str, char, expected):
    assert utils.contains(input_str, char) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
])
def test_delete_symbol(input_str, char, expected):
    assert utils.delete_symbol(input_str, char) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
])
def test_starts_with(input_str, char, expected):
    assert utils.starts_with(input_str, char) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
])
def test_end_with(input_str, char, expected):
    assert utils.end_with(input_str, char) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("", True),
    (" ", True),
    ("SkyPro", False),
])
def test_is_empty(input_str, expected):
    assert utils.is_empty(input_str) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 4], "1, 2, 3, 4"),
    (["Sky", "Pro"], "Sky, Pro"),
    (["Sky", "Pro"], "Sky-Pro", "-"),
])
def test_list_to_string(input_list, expected, delimiter=None):
    assert utils.list_to_string(input_list, delimiter) == expected

#==================================================================================================================Негативные========================================================================================================================================

@pytest.mark.parametrize("input_str, expected", [
    ("apple pie", "Apple Pie"),
    ("123", "1234"),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) != expected

@pytest.mark.parametrize("input_str, expected", [
    ("   apple", " apple"),
    ("apple   ", "apple  "),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) != expected

@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("a,b,c,d", ",", ["a", "b", "c", "d", "e"]),
    ("1:2:3", ":", ["1", "2"]),
])
def test_to_list_negative(input_str, delimiter, expected):
    assert utils.to_list(input_str, delimiter) != expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "X", False),
    ("SkyPro", "P", False),
])
def test_contains_negative(input_str, char, expected):
    assert utils.contains(input_str, char) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", "SkyPro"),
    ("SkyPro", "Sky", "Pro"),
])
def test_delete_symbol_negative(input_str, char, expected):
    assert utils.delete_symbol(input_str, char) != expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "k", False),
    ("SkyPro", "S", False),
])
def test_starts_with_negative(input_str, char, expected):
    assert utils.starts_with(input_str, char) == expected

@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "x", False),
    ("SkyPro", "o", False),
])
def test_end_with_negative(input_str, char, expected):
    assert utils.end_with(input_str, char) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro ", False),
    ("  ", False),
])
def test_is_empty_negative(input_str, expected):
    assert utils.is_empty(input_str) == expected

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3], "1, 2, 3, 4"),
    (["Sky", "Pro"], "Sky-Pro"),
])
def test_list_to_string_negative(input_list, expected):
    assert utils.list_to_string(input_list) != expected
