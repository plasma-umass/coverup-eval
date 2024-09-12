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

@pytest.fixture(autouse=True)
def cleanup_ioloop():
    yield
    ioloop.IOLoop.clear_instance()

def test_condition_init_creates_ioloop(monkeypatch):
    def mock_current():
        return "mocked_ioloop"
    
    monkeypatch.setattr(ioloop.IOLoop, "current", mock_current)
    condition = Condition()
    assert condition.io_loop == "mocked_ioloop"
