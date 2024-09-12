# file: codetiming/_timers.py:52-54
# asked: {"lines": [52, 54], "branches": []}
# gained: {"lines": [52, 54], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_total_with_existing_timer(timers, mocker):
    mocker.patch.object(timers, 'apply', return_value=10.0)
    result = timers.total('test_timer')
    assert result == 10.0
    timers.apply.assert_called_once_with(sum, name='test_timer')

def test_total_with_non_existing_timer(timers, mocker):
    mocker.patch.object(timers, 'apply', return_value=0.0)
    result = timers.total('non_existing_timer')
    assert result == 0.0
    timers.apply.assert_called_once_with(sum, name='non_existing_timer')
