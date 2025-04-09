# file: tornado/locks.py:262-283
# asked: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}
# gained: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}

import pytest
from unittest.mock import Mock

from tornado.locks import _ReleasingContextManager

class Test_ReleasingContextManager:
    def test_enter(self):
        mock_obj = Mock()
        context_manager = _ReleasingContextManager(mock_obj)
        assert context_manager.__enter__() is None

    def test_exit(self):
        mock_obj = Mock()
        context_manager = _ReleasingContextManager(mock_obj)
        context_manager.__exit__(None, None, None)
        mock_obj.release.assert_called_once()

    def test_exit_with_exception(self):
        mock_obj = Mock()
        context_manager = _ReleasingContextManager(mock_obj)
        exc_type = Exception
        exc_val = Exception("Test exception")
        exc_tb = None
        context_manager.__exit__(exc_type, exc_val, exc_tb)
        mock_obj.release.assert_called_once()
