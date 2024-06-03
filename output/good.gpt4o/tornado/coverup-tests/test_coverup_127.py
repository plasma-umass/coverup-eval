# file tornado/util.py:291-301
# lines [291, 292, 301]
# branches []

import pytest
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

def test_configurable_base_not_implemented():
    with pytest.raises(NotImplementedError):
        Configurable.configurable_base()

def test_configurable_base_implemented():
    assert TestConfigurable.configurable_base() is TestConfigurable
