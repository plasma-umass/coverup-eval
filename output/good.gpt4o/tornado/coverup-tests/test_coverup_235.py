# file tornado/util.py:271-289
# lines [283]
# branches ['281->283']

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
        return TestConfigurableImplBase

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class TestConfigurableImplBase(TestConfigurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def test_configurable_recursion():
    with mock.patch.object(TestConfigurableImpl, 'configurable_base', return_value=TestConfigurableImplBase):
        instance = TestConfigurable()
        assert isinstance(instance, TestConfigurableImpl)
        assert instance.args == ()
        assert instance.kwargs == {}

        instance_with_args = TestConfigurable(1, 2, a=3)
        assert isinstance(instance_with_args, TestConfigurableImpl)
        assert instance_with_args.args == (1, 2)
        assert instance_with_args.kwargs == {'a': 3}
