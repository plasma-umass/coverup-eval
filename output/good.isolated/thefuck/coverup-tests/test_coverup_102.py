# file thefuck/shells/generic.py:136-138
# lines [136, 138]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_generic_get_version():
    generic_shell = Generic()
    assert generic_shell._get_version() == ''
