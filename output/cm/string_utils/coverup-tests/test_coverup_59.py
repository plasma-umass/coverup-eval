# file string_utils/validation.py:308-342
# lines [329, 330, 331, 332, 334, 335, 336, 337, 340, 342]
# branches ['329->330', '329->342']

import pytest
from string_utils.validation import is_snake_case

@pytest.fixture
def clean_up():
    # Fixture to clean up any state after tests, if necessary
    yield
    # Here you can add any teardown code if needed

def test_is_snake_case_with_custom_separator(clean_up):
    assert is_snake_case('foo-bar-baz', separator='-') == True
    assert is_snake_case('foo--bar--baz', separator='-') == True
    assert is_snake_case('foo-bar', separator='-') == True
    assert is_snake_case('foo_bar', separator='-') == False
    assert is_snake_case('1foo-bar', separator='-') == False
    assert is_snake_case('foo1-bar', separator='-') == True
    assert is_snake_case('foo1-2bar', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9', separator='-') == True
    assert is_snake_case('foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-', separator='-') == True
    assert is_snake_case('-foo1-2bar-baz3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9', separator='-') == True
