# file: tornado/util.py:271-289
# asked: {"lines": [271, 272, 273, 274, 275, 276, 277, 279, 280, 281, 283, 284, 288, 289], "branches": [[274, 275], [274, 279], [276, 277], [276, 280], [281, 283], [281, 284]]}
# gained: {"lines": [271, 272, 273, 274, 275, 276, 279, 280, 281, 284, 288, 289], "branches": [[274, 275], [274, 279], [276, 280], [281, 284]]}

import pytest
from unittest.mock import patch

from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return TestConfigurable

    @classmethod
    def configured_class(cls):
        return TestConfigurable

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def test_configurable_new_base_class():
    with patch.object(TestConfigurable, 'configurable_base', return_value=TestConfigurable), \
         patch.object(TestConfigurable, 'configured_class', return_value=TestConfigurable):
        instance = TestConfigurable()
        assert isinstance(instance, TestConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {}

def test_configurable_new_different_class():
    class DifferentConfigurable(TestConfigurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

    with patch.object(DifferentConfigurable, 'configurable_base', return_value=TestConfigurable):
        instance = DifferentConfigurable()
        assert isinstance(instance, DifferentConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {}

def test_configurable_new_with_kwargs():
    with patch.object(TestConfigurable, 'configurable_base', return_value=TestConfigurable), \
         patch.object(TestConfigurable, 'configured_class', return_value=TestConfigurable):
        instance = TestConfigurable(foo='bar')
        assert isinstance(instance, TestConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {'foo': 'bar'}

def test_configurable_new_recursive():
    class RecursiveConfigurable(TestConfigurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configured_class(cls):
            return RecursiveConfigurable

    with patch.object(RecursiveConfigurable, 'configurable_base', return_value=TestConfigurable), \
         patch.object(RecursiveConfigurable, 'configured_class', return_value=RecursiveConfigurable):
        instance = RecursiveConfigurable()
        assert isinstance(instance, RecursiveConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {}
