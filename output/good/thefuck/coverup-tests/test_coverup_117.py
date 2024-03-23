# file thefuck/shells/generic.py:19-20
# lines [20]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_aliases(mocker):
    shell = Generic()
    aliases = shell.get_aliases()
    assert aliases == {}, "Expected get_aliases to return an empty dictionary"
