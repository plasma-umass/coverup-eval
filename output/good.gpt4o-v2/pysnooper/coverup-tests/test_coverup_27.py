# file: pysnooper/variables.py:20-50
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest
from unittest.mock import MagicMock
from pysnooper.variables import BaseVariable
import abc

class ConcreteVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return super()._items(key, normalize)

def test_not_implemented_error():
    source = "x"
    frame = MagicMock()
    frame.f_globals = {}
    frame.f_locals = {'x': 1}
    
    var = ConcreteVariable(source)
    
    with pytest.raises(NotImplementedError):
        var._items('key')

