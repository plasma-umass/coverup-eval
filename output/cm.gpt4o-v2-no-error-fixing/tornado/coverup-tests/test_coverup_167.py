# file: tornado/locks.py:446-452
# asked: {"lines": [452], "branches": []}
# gained: {"lines": [452], "branches": []}

import pytest
from tornado.locks import Semaphore

def test_semaphore_exit_calls_enter(monkeypatch):
    sem = Semaphore()

    def mock_enter(self):
        raise RuntimeError("Mocked __enter__ called")

    monkeypatch.setattr(Semaphore, "__enter__", mock_enter)

    with pytest.raises(RuntimeError, match="Mocked __enter__ called"):
        sem.__exit__(None, None, None)

    # Ensure no state pollution
    assert len(sem._waiters) == 0
    assert sem._timeouts == 0
