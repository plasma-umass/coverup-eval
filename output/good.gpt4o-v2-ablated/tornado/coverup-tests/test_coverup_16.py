# file: tornado/queues.py:153-166
# asked: {"lines": [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import pytest
from tornado.queues import Queue
from tornado.concurrent import Future
from tornado.locks import Event
import collections
from typing import Deque, Tuple, Generic, TypeVar

_T = TypeVar("_T")

class TestQueue:
    def test_queue_init_default(self):
        q = Queue()
        assert q._maxsize == 0
        assert isinstance(q._getters, collections.deque)
        assert isinstance(q._putters, collections.deque)
        assert q._unfinished_tasks == 0
        assert isinstance(q._finished, Event)
        assert q._finished.is_set()

    def test_queue_init_maxsize(self):
        q = Queue(10)
        assert q._maxsize == 10

    def test_queue_init_maxsize_none(self):
        with pytest.raises(TypeError, match="maxsize can't be None"):
            Queue(None)

    def test_queue_init_maxsize_negative(self):
        with pytest.raises(ValueError, match="maxsize can't be negative"):
            Queue(-1)
