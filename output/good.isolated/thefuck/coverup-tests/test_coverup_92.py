# file thefuck/shells/generic.py:79-80
# lines [79, 80]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_how_to_configure(mocker):
    generic_shell = Generic()
    assert generic_shell.how_to_configure() is None
