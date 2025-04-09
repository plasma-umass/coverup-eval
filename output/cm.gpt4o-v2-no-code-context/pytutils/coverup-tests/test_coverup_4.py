# file: pytutils/props.py:40-52
# asked: {"lines": [40, 44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}
# gained: {"lines": [40, 44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}

import pytest
from pytutils.props import lazyclassproperty

class TestLazyClassProperty:
    def test_lazyclassproperty(self):
        class MyClass:
            @lazyclassproperty
            def my_prop(cls):
                return 'computed_value'
        
        # Ensure the property is computed and cached
        assert MyClass.my_prop == 'computed_value'
        assert MyClass._lazy_my_prop == 'computed_value'
        
        # Ensure the property is not recomputed
        MyClass._lazy_my_prop = 'new_value'
        assert MyClass.my_prop == 'new_value'
