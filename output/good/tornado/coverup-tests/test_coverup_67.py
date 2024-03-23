# file tornado/queues.py:322-328
# lines [322, 324, 325, 327, 328]
# branches ['324->325', '324->327', '327->exit', '327->328']

import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen
from unittest.mock import Mock

@pytest.fixture
def mock_ioloop():
    loop = Mock(spec=IOLoop)
    loop.time = Mock(return_value=0)
    return loop

@pytest.mark.gen_test
def test_consume_expired(mock_ioloop):
    q = Queue(maxsize=1)

    # Mock the IOLoop's time to simulate a timeout
    q._ioloop = mock_ioloop

    # Add a done putter
    done_putter = (Mock(), Mock(done=lambda: True))
    q._putters.append(done_putter)

    # Add a done getter
    done_getter = Mock(done=lambda: True)
    q._getters.append(done_getter)

    # Add a not done putter
    not_done_putter = (Mock(), Mock(done=lambda: False))
    q._putters.append(not_done_putter)

    # Add a not done getter
    not_done_getter = Mock(done=lambda: False)
    q._getters.append(not_done_getter)

    # Call the method under test
    q._consume_expired()

    # Assert that done putters and getters are removed
    assert done_putter not in q._putters
    assert done_getter not in q._getters

    # Assert that not done putters and getters are not removed
    assert not_done_putter in q._putters
    assert not_done_getter in q._getters
