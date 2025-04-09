# file: string_utils/validation.py:308-342
# asked: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342], "branches": [[329, 330], [329, 342]]}
# gained: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342], "branches": [[329, 330], [329, 342]]}

import pytest
from string_utils.validation import is_snake_case
from string_utils._regex import SNAKE_CASE_TEST_RE, SNAKE_CASE_TEST_DASH_RE
from string_utils.validation import is_full_string
import re

def test_is_snake_case_with_underscore():
    assert is_snake_case('foo_bar_baz') == True
    assert is_snake_case('foo') == False
    assert is_snake_case('foo_bar1_baz2') == True
    assert is_snake_case('_foo_bar') == True
    assert is_snake_case('foo__bar') == True
    assert is_snake_case('foo_bar_') == True
    assert is_snake_case('fooBar') == False
    assert is_snake_case('foo-bar') == False
    assert is_snake_case('123_foo') == False

def test_is_snake_case_with_dash():
    assert is_snake_case('foo-bar-baz', separator='-') == True
    assert is_snake_case('foo', separator='-') == False
    assert is_snake_case('foo-bar1-baz2', separator='-') == True
    assert is_snake_case('-foo-bar', separator='-') == True
    assert is_snake_case('foo--bar', separator='-') == True
    assert is_snake_case('foo-bar-', separator='-') == True
    assert is_snake_case('fooBar', separator='-') == False
    assert is_snake_case('foo_bar', separator='-') == False
    assert is_snake_case('123-foo', separator='-') == False

def test_is_snake_case_with_custom_separator():
    custom_separator = '*'
    custom_re = re.compile(r'([a-z]+\d*\*[a-z\d\*]*|\*+[a-z\d]+[a-z\d\*]*)', re.IGNORECASE)
    assert is_snake_case('foo*bar*baz', separator=custom_separator) == True
    assert is_snake_case('foo', separator=custom_separator) == False
    assert is_snake_case('foo*bar1*baz2', separator=custom_separator) == True
    assert is_snake_case('*foo*bar', separator=custom_separator) == True
    assert is_snake_case('foo**bar', separator=custom_separator) == True
    assert is_snake_case('foo*bar*', separator=custom_separator) == True
    assert is_snake_case('fooBar', separator=custom_separator) == False
    assert is_snake_case('foo-bar', separator=custom_separator) == False
    assert is_snake_case('123*foo', separator=custom_separator) == False

def test_is_snake_case_invalid_input():
    assert is_snake_case(None) == False
    assert is_snake_case('') == False
    assert is_snake_case(' ') == False
    assert is_snake_case(123) == False
    assert is_snake_case([]) == False
    assert is_snake_case({}) == False
