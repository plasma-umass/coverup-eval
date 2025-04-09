# file: tornado/locks.py:113-115
# asked: {"lines": [113, 114, 115], "branches": []}
# gained: {"lines": [113, 114, 115], "branches": []}

import pytest
from tornado import ioloop
from tornado.locks import Condition

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.patch('tornado.ioloop.IOLoop.current', return_value='mock_loop')
    yield mock_loop
    mock_loop.stop()

def test_condition_init(mock_ioloop):
    cond = Condition()
    assert cond.io_loop == 'mock_loop'
