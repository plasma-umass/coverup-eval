# file thefuck/shells/generic.py:49-50
# lines [49, 50]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_history_line(mocker):
    mocker.patch.object(Generic, '_get_history_line', return_value='mocked_line')
    shell = Generic()
    result = shell._get_history_line('ls -la')
    assert result == 'mocked_line'
