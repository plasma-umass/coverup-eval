# file thefuck/shells/generic.py:19-20
# lines [19, 20]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_aliases(mocker):
    mocker.patch('thefuck.shells.generic.Generic.get_aliases', return_value={})
    shell = Generic()
    aliases = shell.get_aliases()
    assert aliases == {}
