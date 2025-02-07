# file: string_utils/manipulation.py:405-430
# asked: {"lines": [429, 430], "branches": []}
# gained: {"lines": [429, 430], "branches": []}

import pytest
from string_utils.manipulation import prettify

def test_prettify():
    # Test case to cover the lines 429-430
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\' s awesome! '
    expected_output = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    
    result = prettify(input_string)
    
    assert result == expected_output
