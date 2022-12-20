from stringbuilder import StringBuilder


def test_string_builder_performance_append(benchmark):
    sb = StringBuilder("Hello")

    benchmark(sb.append, " World!")


def test_string_builder_performance_append_line(benchmark):
    sb = StringBuilder("Hello")
    benchmark(sb.append_line, " How are you doing?")


def test_string_builder_performance_clear(benchmark):
    sb = StringBuilder("Hello")
    benchmark(sb.clear)
