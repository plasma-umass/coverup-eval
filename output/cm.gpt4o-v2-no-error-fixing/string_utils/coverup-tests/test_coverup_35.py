# file: string_utils/validation.py:308-342
# asked: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342], "branches": [[329, 330], [329, 342]]}
# gained: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340], "branches": [[329, 330]]}

import pytest
import re
from string_utils.validation import is_snake_case
from string_utils._regex import SNAKE_CASE_TEST_RE, SNAKE_CASE_TEST_DASH_RE

def test_is_snake_case_with_underscore():
    assert is_snake_case('foo_bar_baz') is True
    assert is_snake_case('foo') is False
    assert is_snake_case('foo_bar_123') is True
    assert is_snake_case('_foo_bar') is True
    assert is_snake_case('foo__bar') is True
    assert is_snake_case('Foo_Bar') is True
    assert is_snake_case('fooBar') is False
    assert is_snake_case('foo-bar') is False
    assert is_snake_case('123_foo') is False

def test_is_snake_case_with_dash():
    assert is_snake_case('foo-bar-baz', separator='-') is True
    assert is_snake_case('foo', separator='-') is False
    assert is_snake_case('foo-bar-123', separator='-') is True
    assert is_snake_case('-foo-bar', separator='-') is True
    assert is_snake_case('foo--bar', separator='-') is True
    assert is_snake_case('Foo-Bar', separator='-') is True
    assert is_snake_case('fooBar', separator='-') is False
    assert is_snake_case('foo_bar', separator='-') is False
    assert is_snake_case('123-foo', separator='-') is False

def test_is_snake_case_with_custom_separator():
    custom_separator = '*'
    custom_re = re.compile(r'([a-z]+\d*\*[a-z\d\*]*|\*+[a-z\d]+[a-z\d\*]*)', re.IGNORECASE)
    assert is_snake_case('foo*bar*baz', separator=custom_separator) is True
    assert is_snake_case('foo', separator=custom_separator) is False
    assert is_snake_case('foo*bar*123', separator=custom_separator) is True
    assert is_snake_case('*foo*bar', separator=custom_separator) is True
    assert is_snake_case('foo**bar', separator=custom_separator) is True
    assert is_snake_case('Foo*Bar', separator=custom_separator) is True
    assert is_snake_case('fooBar', separator=custom_separator) is False
    assert is_snake_case('foo_bar', separator=custom_separator) is False
    assert is_snake_case('123*foo', separator=custom_separator) is False
