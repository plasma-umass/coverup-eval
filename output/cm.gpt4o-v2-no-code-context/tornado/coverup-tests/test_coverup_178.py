# file: tornado/util.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from tornado.util import Configurable

def test_configurable_initialize():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def _initialize(self):
            self.initialized = True

    obj = TestConfigurable()
    obj._initialize()
    assert hasattr(obj, 'initialized')
    assert obj.initialized is True
