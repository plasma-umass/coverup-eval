# file pysnooper/utils.py:67-78
# lines [71, 72, 75]
# branches ['74->75']

import pytest
from pysnooper.utils import get_shortish_repr

def test_get_shortish_repr_exception(mocker):
    class CustomObject:
        def __repr__(self):
            raise Exception("Intentional Exception for Testing")

    mocker.patch('pysnooper.utils.get_repr_function', return_value=CustomObject.__repr__)

    result = get_shortish_repr(CustomObject())
    assert result == 'REPR FAILED'

def test_get_shortish_repr_normalize(mocker):
    def fake_normalize_repr(value):
        return "normalized"

    mocker.patch('pysnooper.utils.normalize_repr', side_effect=fake_normalize_repr)

    result = get_shortish_repr("test", normalize=True)
    assert result == "normalized"
