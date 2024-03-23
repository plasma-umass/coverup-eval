# file tornado/concurrent.py:240-244
# lines [240, 241, 244]
# branches []

import pytest
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

def test_future_add_done_callback():
    future = Future()
    callback_invoked = False

    def callback(f):
        nonlocal callback_invoked
        callback_invoked = True
        assert f is future

    future.add_done_callback(callback)
    
    # Run the IOLoop to allow the callback to be executed
    IOLoop.current().run_sync(lambda: future.set_result(None))

    assert callback_invoked, "Callback was not called"
