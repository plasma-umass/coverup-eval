# file: tornado/queues.py:317-320
# asked: {"lines": [317, 318, 319, 320], "branches": []}
# gained: {"lines": [317], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_put_internal():
    q = Queue(maxsize=2)
    
    # Mock methods to track calls
    q._put = pytest.mock.Mock()
    q._finished.clear = pytest.mock.Mock()
    
    # Call the internal method
    q._Queue__put_internal(1)
    
    # Assertions to verify the internal state changes
    assert q._unfinished_tasks == 1
    q._finished.clear.assert_called_once()
    q._put.assert_called_once_with(1)
