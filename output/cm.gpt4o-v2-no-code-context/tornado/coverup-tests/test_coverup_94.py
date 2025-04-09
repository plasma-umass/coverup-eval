# file: tornado/queues.py:317-320
# asked: {"lines": [317, 318, 319, 320], "branches": []}
# gained: {"lines": [317, 318, 319, 320], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_put_internal_increases_unfinished_tasks(queue, mocker):
    initial_unfinished_tasks = queue._unfinished_tasks
    mocker.patch.object(queue, '_put', autospec=True)
    mocker.patch.object(queue._finished, 'clear', autospec=True)
    
    queue._Queue__put_internal('test_item')
    
    assert queue._unfinished_tasks == initial_unfinished_tasks + 1
    queue._put.assert_called_once_with('test_item')
    queue._finished.clear.assert_called_once()

def test_put_internal_clears_finished(queue, mocker):
    mocker.patch.object(queue, '_put', autospec=True)
    mocker.patch.object(queue._finished, 'clear', autospec=True)
    
    queue._Queue__put_internal('test_item')
    
    queue._finished.clear.assert_called_once()
    queue._put.assert_called_once_with('test_item')
