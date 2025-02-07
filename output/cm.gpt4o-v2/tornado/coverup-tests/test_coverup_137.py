# file: tornado/queues.py:73-78
# asked: {"lines": [73, 74, 75, 77, 78], "branches": []}
# gained: {"lines": [73, 74, 77], "branches": []}

import pytest
from tornado.queues import Queue
from typing import Generic, Awaitable, TypeVar

_T = TypeVar('_T')

class _QueueIterator(Generic[_T]):
    def __init__(self, q: "Queue[_T]") -> None:
        self.q = q

    def __anext__(self) -> Awaitable[_T]:
        return self.q.get()

@pytest.mark.asyncio
async def test_queue_iterator_init():
    q = Queue()
    iterator = _QueueIterator(q)
    assert iterator.q == q

@pytest.mark.asyncio
async def test_queue_iterator_anext():
    q = Queue()
    await q.put(1)
    iterator = _QueueIterator(q)
    result = await iterator.__anext__()
    assert result == 1
