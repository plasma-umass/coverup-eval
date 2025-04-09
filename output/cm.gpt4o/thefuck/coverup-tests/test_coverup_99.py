# file thefuck/shells/generic.py:76-77
# lines [76, 77]
# branches []

import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_or_single_command(generic):
    result = generic.or_('echo "Hello"')
    assert result == 'echo "Hello"'

def test_or_multiple_commands(generic):
    result = generic.or_('echo "Hello"', 'echo "World"')
    assert result == 'echo "Hello" || echo "World"'

def test_or_no_commands(generic):
    result = generic.or_()
    assert result == ''
