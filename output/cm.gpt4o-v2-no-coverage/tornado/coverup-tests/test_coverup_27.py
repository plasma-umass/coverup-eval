# file: tornado/concurrent.py:140-170
# asked: {"lines": [140, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164, 165, 168, 170], "branches": [[155, 156], [155, 157], [157, 158], [157, 159], [159, 160], [159, 162], [164, 165], [164, 168]]}
# gained: {"lines": [140], "branches": []}

import pytest
import asyncio
from tornado.concurrent import chain_future, future_set_exc_info, future_add_done_callback
from tornado.ioloop import IOLoop
from unittest.mock import Mock

@pytest.mark.asyncio
async def test_chain_future_success():
    a = asyncio.Future()
    b = asyncio.Future()
    chain_future(a, b)
    a.set_result(42)
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    assert b.result() == 42

@pytest.mark.asyncio
async def test_chain_future_exception():
    a = asyncio.Future()
    b = asyncio.Future()
    chain_future(a, b)
    a.set_exception(ValueError("error"))
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    with pytest.raises(ValueError):
        b.result()

@pytest.mark.asyncio
async def test_chain_future_b_already_done():
    a = asyncio.Future()
    b = asyncio.Future()
    b.set_result(24)
    chain_future(a, b)
    a.set_result(42)
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    assert b.result() == 24

@pytest.mark.asyncio
async def test_chain_future_concurrent_future():
    from concurrent.futures import Future as ConcurrentFuture
    a = ConcurrentFuture()
    b = asyncio.Future()
    chain_future(a, b)
    a.set_result(42)
    await asyncio.wrap_future(a)  # Ensure the concurrent future completes
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    assert b.result() == 42

@pytest.mark.asyncio
async def test_chain_future_concurrent_future_exception():
    from concurrent.futures import Future as ConcurrentFuture
    a = ConcurrentFuture()
    b = asyncio.Future()
    chain_future(a, b)
    a.set_exception(ValueError("error"))
    await asyncio.wrap_future(a)  # Ensure the concurrent future completes
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    with pytest.raises(ValueError):
        b.result()

@pytest.mark.asyncio
async def test_chain_future_with_exc_info(monkeypatch):
    a = asyncio.Future()
    b = asyncio.Future()
    exc_info = (ValueError, ValueError("error"), None)
    monkeypatch.setattr(a, 'exc_info', Mock(return_value=exc_info))
    chain_future(a, b)
    a.set_result(None)
    await asyncio.sleep(0)  # Yield control to allow callbacks to run
    with pytest.raises(ValueError):
        b.result()
