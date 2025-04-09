# file thefuck/shells/generic.py:19-20
# lines [19, 20]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_aliases():
    generic_shell = Generic()
    aliases = generic_shell.get_aliases()
    assert isinstance(aliases, dict)
    assert aliases == {}
