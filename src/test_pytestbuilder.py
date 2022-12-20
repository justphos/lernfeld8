import pytest

from indent import Indent
from pytestbuilder import PytestBuilder


@pytest.fixture
def pytest_builder():
    return PytestBuilder()


def test_append_line(pytest_builder):
    indent = Indent()
    line = 'import pytest'
    pytest_builder.append_line(indent, line)
    assert str(pytest_builder) == 'import pytest\n'


def test_append(pytest_builder):
    content = 'def test_example():\n    assert 1 + 1 == 2\n'
    pytest_builder.append(content)
    assert str(pytest_builder) == 'def test_example():\n    assert 1 + 1 == 2\n'


def test_clear(pytest_builder):
    pytest_builder.append('some content')
    pytest_builder.clear()
    assert str(pytest_builder) == ''
