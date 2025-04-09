# file: tornado/util.py:338-352
# asked: {"lines": [338, 339, 342, 346, 347, 348, 349, 352], "branches": [[346, 347], [346, 348], [348, 349], [348, 352]]}
# gained: {"lines": [338, 339, 342, 346, 347, 348, 349, 352], "branches": [[346, 347], [348, 349], [348, 352]]}

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

def test_configured_class_with_default():
    class TestConfigurableWithDefault(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return TestConfigurableWithDefault

    assert TestConfigurableWithDefault.configured_class() == TestConfigurableWithDefault

def test_configured_class_without_default():
    class TestConfigurableWithoutDefault(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return None

    with pytest.raises(ValueError, match="configured class not found"):
        TestConfigurableWithoutDefault.configured_class()

def test_configured_class_with_mocked_base(mocker):
    class TestConfigurableWithMockedBase(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return None

    mock_base = mocker.patch.object(TestConfigurableWithMockedBase, 'configurable_base', return_value=TestConfigurableWithMockedBase)
    mock_impl_class = mocker.patch.object(TestConfigurableWithMockedBase, '_Configurable__impl_class', None, create=True)

    with pytest.raises(ValueError, match="configured class not found"):
        TestConfigurableWithMockedBase.configured_class()
