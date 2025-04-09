# file tornado/locks.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from tornado import ioloop, locks

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.Mock(spec=ioloop.IOLoop)
    mocker.patch.object(ioloop.IOLoop, 'current', return_value=mock_loop)
    return mock_loop

def test_condition_init_uses_current_ioloop(mock_ioloop):
    condition = locks.Condition()
    assert condition.io_loop is mock_ioloop
