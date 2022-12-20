from indent import Indent

import pytest


@pytest.fixture
def indent():
    return Indent()


def test_increment(indent):
    indent.increment()
    assert indent.level == 1


def test_decrement(indent):
    indent.level = 1
    indent.decrement()
    assert indent.level == 0


def test_decrement_lower_bound(indent):
    indent.level = 0
    indent.decrement()
    assert indent.level == 0


def test_reset(indent):
    indent.level = 1
    indent.reset()
    assert indent.level == 0


def test_str(indent):
    indent.level = 1
    assert str(indent) == '    '
