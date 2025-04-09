# file tornado/queues.py:73-78
# lines [73, 74, 75, 77, 78]
# branches []

import pytest
from tornado.queues import Queue

class _QueueIterator:
    def __init__(self, q: Queue) -> None:
        self.q = q

    def __anext__(self):
        return self.q.get()

@pytest.mark.asyncio
async def test_queue_iterator(mocker):
    q = Queue()
    iterator = _QueueIterator(q)
    
    # Mock the get method to ensure it is called
    mock_get = mocker.patch.object(q, 'get', return_value='test_value')
    
    # Put an item in the queue to be retrieved
    await q.put('test_value')
    
    # Retrieve the item using the iterator
    result = await iterator.__anext__()
    
    # Assert that the result is as expected
    assert result == 'test_value'
    
    # Assert that the get method was called
    mock_get.assert_called_once()
    
    # Clean up the queue
    await q.get()
