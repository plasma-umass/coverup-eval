# file pysnooper/variables.py:20-50
# lines [39]
# branches []

import pytest
from pysnooper.variables import BaseVariable
from unittest.mock import MagicMock

class ConcreteVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return super()._items(key, normalize)

def test_base_variable_items_not_implemented(mocker):
    mocker.patch('pysnooper.variables.needs_parentheses', return_value=False)
    base_var = ConcreteVariable('x')
    frame = MagicMock()
    frame.f_globals = {}
    frame.f_locals = {'x': 1}
    
    with pytest.raises(NotImplementedError):
        base_var.items(frame)

    assert base_var.source == 'x'
    assert base_var.exclude == ()
    assert base_var.unambiguous_source == 'x'
