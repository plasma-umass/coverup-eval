# file: tornado/util.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    @classmethod
    def configurable_default(cls):
        return TestConfigurable

def test_initialize():
    obj = TestConfigurable()
    assert obj.initialize() is None
