# file: tornado/locks.py:113-115
# asked: {"lines": [113, 114, 115], "branches": []}
# gained: {"lines": [113, 114, 115], "branches": []}

import pytest
from tornado import ioloop
from tornado.locks import Condition

@pytest.fixture
def condition_instance():
    return Condition()

def test_condition_init(condition_instance):
    assert isinstance(condition_instance.io_loop, ioloop.IOLoop)
