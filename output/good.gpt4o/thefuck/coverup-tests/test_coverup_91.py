# file thefuck/shells/generic.py:46-47
# lines [46, 47]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_history_file_name():
    shell = Generic()
    history_file_name = shell._get_history_file_name()
    assert history_file_name == ''
