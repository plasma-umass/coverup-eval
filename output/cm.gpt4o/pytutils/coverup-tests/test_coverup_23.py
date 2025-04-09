# file pytutils/props.py:1-10
# lines [1, 2, 6, 7, 9, 10]
# branches []

import pytest
from pytutils.props import roclassproperty

class TestRoClassProperty:
    def test_roclassproperty(self):
        class MyClass:
            @roclassproperty
            def my_prop(cls):
                return "class property value"
        
        # Assert that the class property is accessible and correct
        assert MyClass.my_prop == "class property value"
        
        # Ensure that the property is read-only by checking if it has no setter
        with pytest.raises(AttributeError):
            MyClass.__dict__['my_prop'].__set__(MyClass, "new value")
