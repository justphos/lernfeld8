from sqlite3typeconverter import SQLite3TypeConverter
import pytest


def test_convert():
    converter = SQLite3TypeConverter()

    assert converter.convert("NULL") == "None"

    assert converter.convert("INTEGER") == "int"

    assert converter.convert("REAL") == "float"

    assert converter.convert("TEXT") == "str"

    assert converter.convert("BLOB") == "bytes"


def test_convert_raises_error_on_unknown_type():
    converter = SQLite3TypeConverter()

    with pytest.raises(NotImplementedError):
        converter.convert("UNKNOWN")
