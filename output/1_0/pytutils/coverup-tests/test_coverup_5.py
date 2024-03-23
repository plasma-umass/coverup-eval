# file pytutils/meth.py:1-20
# lines [1, 20]
# branches []

import pytest
from pytutils.meth import bind

class TestBind:
    def test_bind_method_to_instance(self):
        class Dummy:
            pass

        instance = Dummy()
        def func(self):
            return 'mocked_return_value'
        bind(instance, func, 'new_method')

        assert hasattr(instance, 'new_method'), "Method was not bound to the instance."
        assert instance.new_method() == 'mocked_return_value', "Bound method did not return the expected value."
