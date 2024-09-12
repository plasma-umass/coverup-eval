# file: string_utils/validation.py:308-342
# asked: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342], "branches": [[329, 330], [329, 342]]}
# gained: {"lines": [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342], "branches": [[329, 330], [329, 342]]}

import pytest
from string_utils.validation import is_snake_case

def test_is_snake_case_with_underscore():
    assert is_snake_case('foo_bar_baz') is True
    assert is_snake_case('foo') is False
    assert is_snake_case('foo_bar_123') is True
    assert is_snake_case('foo__bar') is True
    assert is_snake_case('Foo_Bar') is True
    assert is_snake_case('fooBar') is False
    assert is_snake_case('_foo_bar') is True
    assert is_snake_case('foo_bar_') is True
    assert is_snake_case('foo__bar__baz') is True
    assert is_snake_case('foo123_bar456') is True
    assert is_snake_case('123foo_bar') is False

def test_is_snake_case_with_dash():
    assert is_snake_case('foo-bar-baz', separator='-') is True
    assert is_snake_case('foo', separator='-') is False
    assert is_snake_case('foo-bar-123', separator='-') is True
    assert is_snake_case('foo--bar', separator='-') is True
    assert is_snake_case('Foo-Bar', separator='-') is True
    assert is_snake_case('fooBar', separator='-') is False
    assert is_snake_case('-foo-bar', separator='-') is True
    assert is_snake_case('foo-bar-', separator='-') is True
    assert is_snake_case('foo--bar--baz', separator='-') is True
    assert is_snake_case('foo123-bar456', separator='-') is True
    assert is_snake_case('123foo-bar', separator='-') is False

def test_is_snake_case_with_custom_separator():
    assert is_snake_case('foo*bar*baz', separator='*') is True
    assert is_snake_case('foo', separator='*') is False
    assert is_snake_case('foo*bar*123', separator='*') is True
    assert is_snake_case('foo**bar', separator='*') is True
    assert is_snake_case('Foo*Bar', separator='*') is True
    assert is_snake_case('fooBar', separator='*') is False
    assert is_snake_case('*foo*bar', separator='*') is True
    assert is_snake_case('foo*bar*', separator='*') is True
    assert is_snake_case('foo**bar**baz', separator='*') is True
    assert is_snake_case('foo123*bar456', separator='*') is True
    assert is_snake_case('123foo*bar', separator='*') is False

def test_is_snake_case_with_non_string_input():
    assert is_snake_case(None) is False
    assert is_snake_case(123) is False
    assert is_snake_case(['foo', 'bar']) is False
    assert is_snake_case({'foo': 'bar'}) is False
