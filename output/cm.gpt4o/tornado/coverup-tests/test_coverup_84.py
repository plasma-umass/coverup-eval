# file tornado/concurrent.py:247-263
# lines [247, 260, 261, 263]
# branches ['260->261', '260->263']

import pytest
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback(mocker):
    # Test when future is already done
    future = futures.Future()
    future.set_result("done")
    callback = mocker.Mock()
    
    future_add_done_callback(future, callback)
    
    callback.assert_called_once_with(future)
    
    # Test when future is not done
    future = futures.Future()
    callback = mocker.Mock()
    
    future_add_done_callback(future, callback)
    
    assert not callback.called
    
    future.set_result("done")
    
    callback.assert_called_once_with(future)
