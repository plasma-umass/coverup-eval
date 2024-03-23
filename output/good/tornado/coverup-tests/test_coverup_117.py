# file tornado/util.py:233-270
# lines [233, 234, 268, 269]
# branches []

import pytest
from tornado.util import Configurable

class MyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return MyConfigurable

    @classmethod
    def configurable_default(cls):
        return MyConfigurable

    def initialize(self, *args, **kwargs):
        pass

def test_configurable_base_and_default():
    assert MyConfigurable.configurable_base() is MyConfigurable
    assert MyConfigurable.configurable_default() is MyConfigurable

def test_configurable_initialization():
    configurable_instance = MyConfigurable()
    assert isinstance(configurable_instance, MyConfigurable)

def test_configurable_configure():
    class MyConfigurableSubclass(MyConfigurable):
        def initialize(self, *args, **kwargs):
            super(MyConfigurableSubclass, self).initialize(*args, **kwargs)
            self.initialized = True

    MyConfigurable.configure(MyConfigurableSubclass)
    instance = MyConfigurable()
    assert isinstance(instance, MyConfigurableSubclass)
    assert instance.initialized

    # Clean up after the test to not affect other tests
    MyConfigurable.configure(None)

def test_configurable_configure_with_kwargs():
    class MyConfigurableSubclass(MyConfigurable):
        def initialize(self, *args, **kwargs):
            super(MyConfigurableSubclass, self).initialize(*args, **kwargs)
            self.value = kwargs.get('value', None)

    MyConfigurable.configure(MyConfigurableSubclass, value=42)
    instance = MyConfigurable()
    assert isinstance(instance, MyConfigurableSubclass)
    assert instance.value == 42

    # Clean up after the test to not affect other tests
    MyConfigurable.configure(None)
