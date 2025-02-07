# file: tornado/locks.py:415-441
# asked: {"lines": [423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [429, 441], [432, 433], [432, 434]]}
# gained: {"lines": [423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [432, 433]]}

import pytest
import datetime
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.testing import AsyncTestCase, gen_test
from unittest.mock import patch
from tornado.locks import Semaphore, _ReleasingContextManager, _TimeoutGarbageCollector

class TestSemaphore(AsyncTestCase):
    
    @gen_test
    async def test_acquire_no_timeout(self):
        sem = Semaphore(1)
        result = await sem.acquire()
        assert isinstance(result, _ReleasingContextManager)
        assert sem._value == 0

    @gen_test
    async def test_acquire_with_timeout(self):
        sem = Semaphore(0)
        timeout = datetime.timedelta(seconds=1)
        
        with patch.object(sem, '_garbage_collect') as mock_gc:
            future = sem.acquire(timeout)
            await gen.sleep(1.1)  # Sleep to ensure timeout occurs
            with pytest.raises(gen.TimeoutError):
                await future
            mock_gc.assert_called_once()
    
    @gen_test
    async def test_acquire_with_timeout_cancel(self):
        sem = Semaphore(0)
        timeout = datetime.timedelta(seconds=1)
        
        future = sem.acquire(timeout)
        io_loop = ioloop.IOLoop.current()
        
        def cancel_future():
            future.set_result(_ReleasingContextManager(sem))
        
        io_loop.add_timeout(datetime.timedelta(seconds=0.5), cancel_future)
        result = await future
        assert isinstance(result, _ReleasingContextManager)
        assert not future.done() or not future.exception()
