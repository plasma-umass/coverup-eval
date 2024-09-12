# file: codetiming/_timers.py:52-54
# asked: {"lines": [52, 54], "branches": []}
# gained: {"lines": [52, 54], "branches": []}

import pytest
from codetiming._timers import Timers

@pytest.fixture
def timers():
    return Timers()

def test_total(timers, mocker):
    # Arrange
    mocker.patch.object(timers, 'apply', return_value=10.0)
    timers._timings['test_timer'] = [1.0, 2.0, 3.0, 4.0]

    # Act
    total_time = timers.total('test_timer')

    # Assert
    timers.apply.assert_called_once_with(sum, name='test_timer')
    assert total_time == 10.0
