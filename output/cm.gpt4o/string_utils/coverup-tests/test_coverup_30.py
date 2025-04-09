# file string_utils/validation.py:308-342
# lines [308, 329, 330, 331, 332, 334, 335, 336, 337, 340, 342]
# branches ['329->330', '329->342']

import pytest
import re
from string_utils.validation import is_snake_case

# Mock dependencies
@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    global SNAKE_CASE_TEST_RE, SNAKE_CASE_TEST_DASH_RE, is_full_string
    SNAKE_CASE_TEST_RE = re.compile(r'([a-z]+\d*_[a-z\d_]*|_+[a-z\d]+[a-z\d_]*)', re.IGNORECASE)
    SNAKE_CASE_TEST_DASH_RE = re.compile(r'([a-z]+\d*-[a-z\d-]*|-+[a-z\d]+[a-z\d-]*)', re.IGNORECASE)
    is_full_string = mocker.patch('string_utils.validation.is_full_string', return_value=True)

def test_is_snake_case_with_underscore():
    assert is_snake_case('foo_bar_baz') == True
    assert is_snake_case('foo') == False
    assert is_snake_case('foo_bar') == True
    assert is_snake_case('foo_bar_123') == True
    assert is_snake_case('foo__bar') == True
    assert is_snake_case('fooBar') == False

def test_is_snake_case_with_dash():
    assert is_snake_case('foo-bar-baz', separator='-') == True
    assert is_snake_case('foo', separator='-') == False
    assert is_snake_case('foo-bar', separator='-') == True
    assert is_snake_case('foo-bar-123', separator='-') == True
    assert is_snake_case('foo--bar', separator='-') == True
    assert is_snake_case('fooBar', separator='-') == False

def test_is_snake_case_with_custom_separator():
    assert is_snake_case('foo*bar*baz', separator='*') == True
    assert is_snake_case('foo', separator='*') == False
    assert is_snake_case('foo*bar', separator='*') == True
    assert is_snake_case('foo*bar*123', separator='*') == True
    assert is_snake_case('foo**bar', separator='*') == True
    assert is_snake_case('fooBar', separator='*') == False

def test_is_snake_case_invalid_input():
    is_full_string.return_value = False
    assert is_snake_case('foo_bar_baz') == False
    assert is_snake_case('foo-bar-baz', separator='-') == False
    assert is_snake_case('foo*bar*baz', separator='*') == False
