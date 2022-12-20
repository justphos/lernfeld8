from stringbuilder import StringBuilder

from pytest_benchmark import benchmark


def test_string_builder_performance(benchmark):
    sb = StringBuilder("Hello")

    benchmark(sb.append, " World!")

    assert str(sb) == "Hello World!"

    benchmark(sb.append_line, " How are you doing?")

    assert str(sb) == "Hello World!\nHow are you doing?"

    benchmark(sb.clear)

    assert str(sb) == ""
