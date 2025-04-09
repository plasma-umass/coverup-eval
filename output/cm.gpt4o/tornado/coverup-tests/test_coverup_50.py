# file tornado/util.py:338-352
# lines [338, 339, 342, 346, 347, 348, 349, 352]
# branches ['346->347', '346->348', '348->349', '348->352']

import pytest
from unittest import mock

# Assuming the Configurable class is imported from tornado.util
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

    @classmethod
    def configurable_default(cls):
        return TestConfigurable

def test_configured_class(mocker):
    # Mock the configurable_base and configurable_default methods
    mocker.patch.object(Configurable, 'configurable_base', return_value=TestConfigurable)
    mocker.patch.object(Configurable, 'configurable_default', return_value=TestConfigurable)

    # Test the configured_class method
    assert Configurable.configured_class() == TestConfigurable

    # Clean up by deleting the __impl_class attribute if it exists
    if hasattr(TestConfigurable, '_Configurable__impl_class'):
        del TestConfigurable._Configurable__impl_class

    # Test the case where __impl_class is None initially
    mocker.patch.object(Configurable, 'configurable_base', return_value=TestConfigurable)
    mocker.patch.object(Configurable, 'configurable_default', return_value=None)

    with pytest.raises(ValueError, match="configured class not found"):
        Configurable.configured_class()
