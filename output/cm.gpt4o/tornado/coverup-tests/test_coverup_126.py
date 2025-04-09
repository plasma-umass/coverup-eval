# file tornado/concurrent.py:233-237
# lines [233, 234, 237]
# branches []

import pytest
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback():
    def callback(future):
        assert future.done()
        assert future.result() == 42

    future = futures.Future()
    future_add_done_callback(future, callback)
    future.set_result(42)

    assert future.done()
    assert future.result() == 42
