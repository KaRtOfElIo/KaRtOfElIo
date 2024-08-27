from .string_utils import StringUtils
import pytest
utils=StringUtils
#==================================================================================================================ПОЗИТИВНЫЕ========================================================================================================================================
def test_capitalize():
    assert utils.capitalize ("apple") == "Apple"
    assert utils.capitalize ("111") == "111"
def test_trim():
    assert utils.trim ("   apple") == "apple"
    assert utils.trim ("   111") == "111"
def test_to_list():
    assert utils.to_list ("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list ("1:2:3", ":") ==  ["1" , "2", "3"]
def test_contains():
    assert utils.contains ("SkyPro", "S") == "True"
    assert utils.contains ("SkyPro", "U") == "False"
def test_delete_symbol():
    assert utils.delete_symbol ("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol ("SkyPro", "Pro") == "Sky"
def test_starts_with():
    assert utils.starts_with ("SkyPro", "S") == "True"
    assert utils.starts_with ("SkyPro", "P") == "False"
def test_end_with():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("SkyPro", "y") == False

def test_is_empty():
    utils = StringUtils()
    assert utils.is_empty("") == True
    assert utils.is_empty(" ") == True
    assert utils.is_empty("SkyPro") == False

def test_list_to_string():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
#==================================================================================================================Негативные========================================================================================================================================
def test_capitalize_negative():
    utils = StringUtils()
    assert utils.capitalize("apple pie") != "Apple Pie"
    assert utils.capitalize("123") != "1234"

def test_trim_negative():
    utils = StringUtils()
    assert utils.trim("   apple") != " apple"
    assert utils.trim("apple   ") != "apple  "

def test_to_list_negative():
    utils = StringUtils()
    assert utils.to_list("a,b,c,d") != ["a", "b", "c", "d", "e"]
    assert utils.to_list("1:2:3", ":") != ["1", "2"]

def test_contains_negative():
    utils = StringUtils()
    assert utils.contains("SkyPro", "X") == False
    assert utils.contains("SkyPro", "P") == False

def test_delete_symbol_negative():
    utils = StringUtils()
    assert utils.delete_symbol("SkyPro", "S") != "SkyPro"
    assert utils.delete_symbol("SkyPro", "Sky") != "Pro"

def test_starts_with_negative():
    utils = StringUtils()
    assert utils.starts_with("SkyPro", "k") == False
    assert utils.starts_with("SkyPro", "S") == False

def test_end_with_negative():
    utils = StringUtils()
    assert utils.end_with("SkyPro", "x") == False
    assert utils.end_with("SkyPro", "o") == False

def test_is_empty_negative():
    utils = StringUtils()
    assert utils.is_empty("SkyPro ") == False
    assert utils.is_empty("  ") == False

def test_list_to_string_negative():
    utils = StringUtils()
    assert utils.list_to_string([1, 2, 3]) != "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) != "Sky-Pro"
