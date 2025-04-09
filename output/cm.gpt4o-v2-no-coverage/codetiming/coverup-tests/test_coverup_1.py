# file: codetiming/_timers.py:52-54
# asked: {"lines": [52, 54], "branches": []}
# gained: {"lines": [52, 54], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_total(timers, mocker):
    mocker.patch.object(timers, 'apply', return_value=10.0)
    result = timers.total('test_timer')
    assert result == 10.0
    timers.apply.assert_called_once_with(sum, name='test_timer')
