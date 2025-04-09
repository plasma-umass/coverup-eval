# file tornado/locks.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from tornado import ioloop
from tornado.locks import _TimeoutGarbageCollector

class Condition(_TimeoutGarbageCollector):
    def __init__(self) -> None:
        super().__init__()
        self.io_loop = ioloop.IOLoop.current()

def test_condition_initialization(mocker):
    mock_ioloop = mocker.patch('tornado.ioloop.IOLoop.current', return_value='mocked_ioloop')
    
    condition = Condition()
    
    assert condition.io_loop == 'mocked_ioloop'
    mock_ioloop.assert_called_once()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    ioloop.IOLoop.clear_instance()
