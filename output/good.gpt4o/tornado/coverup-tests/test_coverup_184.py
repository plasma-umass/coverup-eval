# file tornado/queues.py:330-331
# lines [330, 331]
# branches []

import pytest
from tornado.queues import Queue

def test_queue_repr(mocker):
    # Create a mock for the _format method
    mock_format = mocker.patch.object(Queue, '_format', return_value='mocked_format')

    # Instantiate the Queue
    queue = Queue()

    # Call the __repr__ method
    repr_result = repr(queue)

    # Verify the result
    assert repr_result == f"<Queue at {hex(id(queue))} mocked_format>"

    # Ensure the _format method was called
    mock_format.assert_called_once()
