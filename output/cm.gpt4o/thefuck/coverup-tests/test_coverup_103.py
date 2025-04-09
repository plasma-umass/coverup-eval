# file thefuck/shells/generic.py:136-138
# lines [136, 138]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_version():
    shell = Generic()
    version = shell._get_version()
    assert version == '', "Expected version to be an empty string"

