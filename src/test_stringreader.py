from stringreader import StringReader


def test_string_reader_empty_string():
    reader = StringReader('')
    assert reader.read_line() == ''


def test_string_reader_single_line_string():
    reader = StringReader('hello world')
    assert reader.read_line() == 'hello world'


def test_string_reader_multi_line_string():
    reader = StringReader('hello\nworld\n!')
    assert reader.read_line() == 'hello\n'
    assert reader.read_line() == 'world\n'
    assert reader.read_line() == '!'
