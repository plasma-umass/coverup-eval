# file thefuck/shells/generic.py:73-74
# lines [73, 74]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_and_method():
    shell = Generic()
    commands = ['echo "Hello"', 'echo "World"']
    expected_result = 'echo "Hello" && echo "World"'
    assert shell.and_(*commands) == expected_result
