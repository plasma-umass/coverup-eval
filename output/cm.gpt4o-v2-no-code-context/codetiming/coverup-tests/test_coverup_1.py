# file: codetiming/_timers.py:48-50
# asked: {"lines": [48, 50], "branches": []}
# gained: {"lines": [48, 50], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_timers_count(timers, mocker):
    mock_apply = mocker.patch.object(timers, 'apply', return_value=3)
    result = timers.count('test_timer')
    mock_apply.assert_called_once_with(len, name='test_timer')
    assert result == 3
