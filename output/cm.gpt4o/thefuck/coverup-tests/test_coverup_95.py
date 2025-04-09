# file thefuck/shells/generic.py:79-80
# lines [79, 80]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_how_to_configure():
    shell = Generic()
    result = shell.how_to_configure()
    assert result is None
