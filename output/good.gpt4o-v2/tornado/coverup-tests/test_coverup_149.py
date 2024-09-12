# file: tornado/queues.py:292-300
# asked: {"lines": [292, 293, 300], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
import datetime
from tornado.queues import Queue
from tornado.util import TimeoutError

@pytest.mark.gen_test
async def test_queue_join_with_timeout():
    queue = Queue()
    queue._finished = pytest.mock.Mock()
    queue._finished.wait = pytest.mock.AsyncMock()

    timeout = datetime.timedelta(seconds=1)
    await queue.join(timeout=timeout)
    queue._finished.wait.assert_called_once_with(timeout)

@pytest.mark.gen_test
async def test_queue_join_without_timeout():
    queue = Queue()
    queue._finished = pytest.mock.Mock()
    queue._finished.wait = pytest.mock.AsyncMock()

    await queue.join()
    queue._finished.wait.assert_called_once_with(None)

@pytest.mark.gen_test
async def test_queue_join_timeout_error():
    queue = Queue()
    queue._finished = pytest.mock.Mock()
    queue._finished.wait = pytest.mock.AsyncMock(side_effect=TimeoutError)

    with pytest.raises(TimeoutError):
        await queue.join(timeout=1)
