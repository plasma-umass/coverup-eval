# file tornado/util.py:271-289
# lines [283]
# branches ['281->283']

import pytest
from tornado.util import Configurable

class BaseConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return BaseConfigurable

    @classmethod
    def configured_class(cls):
        return DerivedConfigurable

    def initialize(self, *args, **kwargs):
        pass

class DerivedConfigurable(BaseConfigurable):
    @classmethod
    def configurable_base(cls):
        return DerivedConfigurable

    def initialize(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def test_configurable_new_with_recursive_configurable():
    # This test is designed to cover the missing line 283
    # by creating a situation where the `impl` is itself configurable.
    args = (1, 2)
    kwargs = {'a': 3, 'b': 4}
    obj = BaseConfigurable(*args, **kwargs)
    
    # Assertions to verify postconditions
    assert isinstance(obj, DerivedConfigurable)
    assert obj.args == args
    assert obj.kwargs == kwargs
