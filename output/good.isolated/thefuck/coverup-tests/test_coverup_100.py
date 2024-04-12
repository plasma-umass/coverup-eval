# file thefuck/shells/generic.py:113-114
# lines [113, 114]
# branches []

import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic_shell():
    return Generic()

def test_script_from_history(generic_shell):
    line = 'echo "Hello, World!"'
    assert generic_shell._script_from_history(line) == line
