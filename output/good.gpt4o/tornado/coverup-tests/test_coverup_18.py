# file tornado/util.py:271-289
# lines [271, 272, 273, 274, 275, 276, 277, 279, 280, 281, 283, 284, 288, 289]
# branches ['274->275', '274->279', '276->277', '276->280', '281->283', '281->284']

import pytest
from unittest import mock

# Assuming the Configurable class is imported from tornado.util
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    @classmethod
    def configured_class(cls):
        return TestConfigurableImpl

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class TestConfigurableImpl(TestConfigurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

@pytest.fixture
def mock_configurable_class(mocker):
    mocker.patch.object(TestConfigurable, 'configured_class', return_value=TestConfigurableImpl)
    return TestConfigurable

def test_configurable_new(mock_configurable_class):
    instance = mock_configurable_class(1, 2, key='value')
    assert isinstance(instance, TestConfigurableImpl)
    assert instance.args == (1, 2)
    assert instance.kwargs == {'key': 'value'}

def test_configurable_new_base_class(mocker):
    mocker.patch.object(TestConfigurable, 'configured_class', return_value=TestConfigurable)
    instance = TestConfigurable(3, 4, key='another_value')
    assert isinstance(instance, TestConfigurable)
    assert instance.args == (3, 4)
    assert instance.kwargs == {'key': 'another_value'}
