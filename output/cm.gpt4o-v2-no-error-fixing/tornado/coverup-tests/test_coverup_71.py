# file: tornado/queues.py:180-184
# asked: {"lines": [180, 181, 182, 184], "branches": [[181, 182], [181, 184]]}
# gained: {"lines": [180], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_full_with_unbounded_queue():
    q = Queue(maxsize=0)
    assert not q.full()

@pytest.mark.asyncio
async def test_queue_full_with_bounded_queue(monkeypatch):
    q = Queue(maxsize=2)
    
    # Mock qsize to control the return value
    monkeypatch.setattr(q, "qsize", lambda: 1)
    assert not q.full()
    
    monkeypatch.setattr(q, "qsize", lambda: 2)
    assert q.full()
