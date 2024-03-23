# file thefuck/shells/generic.py:49-50
# lines [50]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_history_line():
    shell = Generic()
    history_line = shell._get_history_line('ls')
    assert history_line == ''
