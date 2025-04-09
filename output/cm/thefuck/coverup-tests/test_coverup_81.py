# file thefuck/shells/generic.py:16-18
# lines [16, 17]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_generic_shell_friendly_name():
    shell = Generic()
    assert shell.friendly_name == 'Generic Shell'
