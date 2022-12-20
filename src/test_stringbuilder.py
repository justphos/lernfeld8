from stringbuilder import StringBuilder


def test_string_builder_init():
    sb = StringBuilder("initial value")
    assert sb._file_str.getvalue() == "initial value"

    sb = StringBuilder()
    assert sb._file_str.getvalue() == ""


def test_string_builder_append():
    sb = StringBuilder("initial value")
    sb.append("appended value")
    assert sb._file_str.getvalue() == "initial valueappended value"


def test_string_builder_append_line():
    sb = StringBuilder("initial value")
    sb.append_line("appended value")
    assert sb._file_str.getvalue() == "initial valueappended value\n"


def test_string_builder_clear():
    sb = StringBuilder("initial value")
    sb.clear()
    assert sb._file_str.getvalue() == ""


def test_string_builder_str():
    sb = StringBuilder("initial value")
    assert str(sb) == "initial value"
