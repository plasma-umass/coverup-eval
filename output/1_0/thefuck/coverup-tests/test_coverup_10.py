# file thefuck/rules/cd_parent.py:11-12
# lines [11, 12]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.cd_parent import match

def test_match():
    # Test the case where the script is exactly 'cd..'
    command = Command('cd..', '')
    assert match(command)

    # Test the case where the script is not 'cd..'
    command = Command('cd ../', '')
    assert not match(command)
