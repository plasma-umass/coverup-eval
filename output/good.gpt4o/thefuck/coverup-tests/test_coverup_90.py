# file thefuck/shells/generic.py:113-114
# lines [113, 114]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_script_from_history():
    generic = Generic()
    line = "echo 'Hello, World!'"
    result = generic._script_from_history(line)
    assert result == line

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
