# file tornado/util.py:233-270
# lines [233, 234, 268, 269]
# branches []

import pytest
from unittest import mock

# Assuming the Configurable class is imported from tornado.util
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    @classmethod
    def configurable_default(cls):
        return TestConfigurable

    def initialize(self, **kwargs):
        self.kwargs = kwargs

def test_configurable():
    # Test the default implementation
    obj = TestConfigurable()
    assert isinstance(obj, TestConfigurable)
    
    # Test the configurable implementation
    class CustomConfigurable(TestConfigurable):
        def initialize(self, **kwargs):
            super().initialize(**kwargs)
            self.custom = True

    TestConfigurable.configure(CustomConfigurable, custom_arg='value')
    obj = TestConfigurable()
    assert isinstance(obj, CustomConfigurable)
    assert obj.custom is True
    assert obj.kwargs == {'custom_arg': 'value'}

    # Clean up by resetting the configuration
    TestConfigurable.configure(None)
    obj = TestConfigurable()
    assert isinstance(obj, TestConfigurable)
    assert not hasattr(obj, 'custom')
    assert obj.kwargs == {}

@pytest.fixture(autouse=True)
def reset_configurable():
    # Ensure that the configuration is reset before and after each test
    TestConfigurable.configure(None)
    yield
    TestConfigurable.configure(None)
