# file: tornado/concurrent.py:74-134
# asked: {"lines": [74, 116, 117, 119, 120, 121, 122, 123, 124, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[128, 129], [128, 130], [130, 131], [130, 132], [132, 133], [132, 134]]}
# gained: {"lines": [74, 116, 117, 119, 120, 126, 128, 129, 130, 131, 132, 133, 134], "branches": [[128, 129], [128, 130], [130, 131], [130, 132], [132, 133], [132, 134]]}

import pytest
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
from tornado.concurrent import Future, chain_future
import asyncio

class TestClass:
    executor = ThreadPoolExecutor(max_workers=1)

    @run_on_executor
    def foo(self, x):
        return x * 2

    @run_on_executor(executor='custom_executor')
    def bar(self, x):
        return x * 3

    custom_executor = ThreadPoolExecutor(max_workers=1)

@pytest.mark.asyncio
async def test_run_on_executor_decorator():
    obj = TestClass()
    future = obj.foo(5)
    assert isinstance(future, Future)
    result = await future
    assert result == 10

@pytest.mark.asyncio
async def test_run_on_executor_decorator_with_custom_executor():
    obj = TestClass()
    future = obj.bar(5)
    assert isinstance(future, Future)
    result = await future
    assert result == 15

def test_run_on_executor_decorator_invalid_args():
    with pytest.raises(ValueError, match="cannot combine positional and keyword args"):
        @run_on_executor(1, executor='custom_executor')
        def invalid_fn(self):
            pass

def test_run_on_executor_decorator_invalid_args_length():
    with pytest.raises(ValueError, match="expected 1 argument, got"):
        @run_on_executor(1, 2)
        def invalid_fn(self):
            pass
