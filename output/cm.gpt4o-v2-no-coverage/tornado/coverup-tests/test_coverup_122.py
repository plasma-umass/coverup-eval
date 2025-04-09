# file: tornado/locks.py:113-115
# asked: {"lines": [113, 114, 115], "branches": []}
# gained: {"lines": [113, 114, 115], "branches": []}

import pytest
from tornado import ioloop
from tornado.locks import Condition

@pytest.fixture
def setup_and_teardown():
    # Setup: Create a new IOLoop instance and set it as the current instance
    loop = ioloop.IOLoop()
    ioloop.IOLoop.clear_current()
    loop.make_current()
    yield
    # Teardown: Clear the current IOLoop instance and close the loop
    ioloop.IOLoop.clear_current()
    loop.close()

def test_condition_init(setup_and_teardown):
    condition = Condition()
    assert condition.io_loop is ioloop.IOLoop.current()
