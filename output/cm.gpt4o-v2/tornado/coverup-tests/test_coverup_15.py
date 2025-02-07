# file: tornado/concurrent.py:140-170
# asked: {"lines": [140, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164, 165, 168, 170], "branches": [[155, 156], [155, 157], [157, 158], [157, 159], [159, 160], [159, 162], [164, 165], [164, 168]]}
# gained: {"lines": [140, 153, 164, 165], "branches": [[164, 165]]}

import pytest
from tornado.concurrent import Future, chain_future
from tornado.ioloop import IOLoop

@pytest.mark.gen_test
async def test_chain_future_result():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    await b
    assert b.result() == 42

@pytest.mark.gen_test
async def test_chain_future_exception():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_exception(ValueError("error"))
    with pytest.raises(ValueError):
        await b

def test_chain_future_done():
    a = Future()
    b = Future()
    b.set_result(24)
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 24

@pytest.mark.gen_test
async def test_chain_future_concurrent_future(mocker):
    from concurrent.futures import Future as ConcurrentFuture
    a = ConcurrentFuture()
    b = ConcurrentFuture()
    mock_ioloop = mocker.patch('tornado.ioloop.IOLoop.current')
    mock_loop = mock_ioloop.return_value
    chain_future(a, b)
    a.set_result(42)
    callback = mock_loop.add_future.call_args[0][1]
    callback(a)
    await b
    assert b.result() == 42

@pytest.mark.gen_test
async def test_chain_future_exception_info(mocker):
    a = Future()
    b = Future()
    mock_exc_info = mocker.patch.object(a, 'exc_info', return_value=(None, ValueError("error"), None))
    chain_future(a, b)
    a.set_result(42)
    with pytest.raises(ValueError):
        await b
