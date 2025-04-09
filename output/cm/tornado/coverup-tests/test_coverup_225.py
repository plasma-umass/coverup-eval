# file tornado/queues.py:153-166
# lines [155, 158]
# branches ['154->155', '157->158']

import pytest
from tornado.queues import Queue

def test_queue_init_maxsize_none():
    with pytest.raises(TypeError) as exc_info:
        Queue(maxsize=None)
    assert "maxsize can't be None" in str(exc_info.value)

def test_queue_init_maxsize_negative():
    with pytest.raises(ValueError) as exc_info:
        Queue(maxsize=-1)
    assert "maxsize can't be negative" in str(exc_info.value)
