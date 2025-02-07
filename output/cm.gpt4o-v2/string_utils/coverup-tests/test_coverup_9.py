# file: string_utils/manipulation.py:433-459
# asked: {"lines": [433, 447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}
# gained: {"lines": [433, 447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}

import pytest
from string_utils.manipulation import asciify
from string_utils.errors import InvalidInputError

def test_asciify_with_non_string_input():
    with pytest.raises(InvalidInputError) as excinfo:
        asciify(12345)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_asciify_with_string_input():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output
