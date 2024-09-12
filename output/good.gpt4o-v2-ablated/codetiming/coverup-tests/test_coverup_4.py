# file: codetiming/_timers.py:56-58
# asked: {"lines": [58], "branches": []}
# gained: {"lines": [58], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_min_with_values(timers, mocker):
    mocker.patch.object(timers, 'apply', return_value=1.0)
    result = timers.min('test_timer')
    assert result == 1.0
    timers.apply.assert_called_once_with(mocker.ANY, name='test_timer')

def test_min_with_no_values(timers, mocker):
    mocker.patch.object(timers, 'apply', return_value=0.0)
    result = timers.min('test_timer')
    assert result == 0.0
    timers.apply.assert_called_once_with(mocker.ANY, name='test_timer')
