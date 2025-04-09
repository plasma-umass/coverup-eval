# file: tornado/concurrent.py:233-237
# asked: {"lines": [233, 234, 237], "branches": []}
# gained: {"lines": [233, 234], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback():
    def dummy_callback(fut):
        assert fut.done()

    future = futures.Future()
    future_add_done_callback(future, dummy_callback)
    future.set_result(None)
    assert future.done()
