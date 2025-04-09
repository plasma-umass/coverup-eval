# file: tornado/queues.py:322-328
# asked: {"lines": [322, 324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [322], "branches": []}

import pytest
from tornado.queues import Queue
from tornado.concurrent import Future

@pytest.mark.asyncio
async def test_consume_expired():
    q = Queue()

    # Create mock futures and add them to the queue's _putters and _getters
    putter_future_1 = Future()
    putter_future_1.set_result(None)
    putter_future_2 = Future()
    putter_future_2.set_result(None)
    q._putters.append((None, putter_future_1))
    q._putters.append((None, putter_future_2))

    getter_future_1 = Future()
    getter_future_1.set_result(None)
    getter_future_2 = Future()
    getter_future_2.set_result(None)
    q._getters.append(getter_future_1)
    q._getters.append(getter_future_2)

    # Call the method to be tested
    q._consume_expired()

    # Assert that the _putters and _getters queues are empty
    assert len(q._putters) == 0
    assert len(q._getters) == 0
