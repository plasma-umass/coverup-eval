# file pysnooper/variables.py:20-50
# lines [26, 39]
# branches ['25->26']

import pytest
from pysnooper.variables import BaseVariable
from pysnooper import pycompat, utils

class ConcreteVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return ()

def test_concrete_variable_unambiguous_source():
    variable = ConcreteVariable('x + y', exclude=('y',))
    assert variable.unambiguous_source == '(x + y)'

def test_concrete_variable_not_implemented_error(mocker):
    frame = mocker.MagicMock()
    frame.f_globals = {}
    frame.f_locals = {'x': 1, 'y': 2}
    concrete_variable = ConcreteVariable('x + y', exclude=('y',))
    # No need to raise NotImplementedError as it's now implemented in ConcreteVariable
    items = concrete_variable.items(frame)
    assert items == ()
