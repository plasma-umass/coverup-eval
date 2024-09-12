# file: tornado/concurrent.py:247-263
# asked: {"lines": [261], "branches": [[260, 261]]}
# gained: {"lines": [261], "branches": [[260, 261]]}

import pytest
import asyncio
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback_with_done_future():
    future = asyncio.Future()
    future.set_result("done")
    
    def callback(fut):
        assert fut.result() == "done"
    
    future_add_done_callback(future, callback)

def test_future_add_done_callback_with_pending_future():
    future = asyncio.Future()
    
    def callback(fut):
        assert fut.result() == "done"
    
    future_add_done_callback(future, callback)
    future.set_result("done")
