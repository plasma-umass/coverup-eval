# file: tornado/util.py:271-289
# asked: {"lines": [271, 272, 273, 274, 275, 276, 277, 279, 280, 281, 283, 284, 288, 289], "branches": [[274, 275], [274, 279], [276, 277], [276, 280], [281, 283], [281, 284]]}
# gained: {"lines": [271, 272, 273, 274, 275, 276, 280, 281, 284, 288, 289], "branches": [[274, 275], [276, 280], [281, 284]]}

import pytest
from unittest.mock import patch

from tornado.util import Configurable

class MyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return MyConfigurable

    @classmethod
    def configured_class(cls):
        return MyConfigurable

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def test_configurable_new_base_class():
    with patch.object(MyConfigurable, 'configurable_base', return_value=MyConfigurable):
        instance = MyConfigurable()
        assert isinstance(instance, MyConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {}

def test_configurable_new_different_class():
    class AnotherConfigurable(MyConfigurable):
        pass

    with patch.object(MyConfigurable, 'configurable_base', return_value=MyConfigurable):
        with patch.object(MyConfigurable, 'configured_class', return_value=AnotherConfigurable):
            instance = MyConfigurable()
            assert isinstance(instance, AnotherConfigurable)
            assert instance.args == ()
            assert instance.kwargs == {}

def test_configurable_new_with_kwargs():
    with patch.object(MyConfigurable, 'configurable_base', return_value=MyConfigurable):
        instance = MyConfigurable(foo='bar')
        assert isinstance(instance, MyConfigurable)
        assert instance.args == ()
        assert instance.kwargs == {'foo': 'bar'}

def test_configurable_new_recursive():
    class RecursiveConfigurable(MyConfigurable):
        @classmethod
        def configurable_base(cls):
            return MyConfigurable

    with patch.object(MyConfigurable, 'configurable_base', return_value=MyConfigurable):
        with patch.object(MyConfigurable, 'configured_class', return_value=RecursiveConfigurable):
            instance = MyConfigurable()
            assert isinstance(instance, RecursiveConfigurable)
            assert instance.args == ()
            assert instance.kwargs == {}
