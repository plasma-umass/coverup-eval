# file: tornado/locks.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}
# gained: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}

import pytest
from tornado.locks import Condition
from collections import deque

class TestCondition:
    def test_condition_repr_no_waiters(self):
        condition = Condition()
        assert repr(condition) == "<Condition>"

    def test_condition_repr_with_waiters(self):
        condition = Condition()
        condition._waiters = deque([1, 2, 3])
        assert repr(condition) == "<Condition waiters[3]>"
