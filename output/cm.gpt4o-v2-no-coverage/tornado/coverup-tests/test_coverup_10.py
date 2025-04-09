# file: tornado/locks.py:415-441
# asked: {"lines": [415, 416, 423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [429, 441], [432, 433], [432, 434]]}
# gained: {"lines": [415, 416], "branches": []}

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.locks import Semaphore
from unittest.mock import MagicMock

class TestSemaphore:
    @pytest.fixture
    def semaphore(self):
        return Semaphore(1)

    @pytest.mark.gen_test
    async def test_acquire_no_timeout(self, semaphore):
        result = await semaphore.acquire()
        assert isinstance(result, _ReleasingContextManager)
        assert semaphore._value == 0

    @pytest.mark.gen_test
    async def test_acquire_with_timeout(self, semaphore, monkeypatch):
        semaphore._value = 0
        mock_io_loop = MagicMock()
        monkeypatch.setattr(ioloop, 'IOLoop', MagicMock(current=MagicMock(return_value=mock_io_loop)))
        
        future = semaphore.acquire(timeout=1)
        assert isinstance(future, Future)
        assert len(semaphore._waiters) == 1

        # Simulate timeout
        on_timeout = mock_io_loop.add_timeout.call_args[0][1]
        on_timeout()
        
        with pytest.raises(gen.TimeoutError):
            await future

        assert len(semaphore._waiters) == 0

    @pytest.mark.gen_test
    async def test_acquire_with_timeout_no_trigger(self, semaphore, monkeypatch):
        semaphore._value = 0
        mock_io_loop = MagicMock()
        monkeypatch.setattr(ioloop, 'IOLoop', MagicMock(current=MagicMock(return_value=mock_io_loop)))
        
        future = semaphore.acquire(timeout=1)
        assert isinstance(future, Future)
        assert len(semaphore._waiters) == 1

        # Simulate release before timeout
        semaphore.release()
        result = await future
        assert isinstance(result, _ReleasingContextManager)
        assert len(semaphore._waiters) == 0
        assert semaphore._value == 0
