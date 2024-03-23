# file mimesis/providers/choice.py:28-88
# lines [60, 69, 78, 79, 80, 81, 84, 85, 86, 87, 88]
# branches ['59->60', '68->69', '75->78', '78->79', '78->84', '80->78', '80->81', '84->85', '84->86', '86->87', '86->88']

import pytest
from mimesis.providers.choice import Choice
from unittest.mock import Mock

def test_choice_exceptions():
    choice = Choice()
    choice.random = Mock()

    # Test for non-integer length
    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length='1')

    # Test for negative length
    with pytest.raises(ValueError):
        choice(items=['a', 'b', 'c'], length=-1)

    # Test for unique with insufficient unique elements
    with pytest.raises(ValueError):
        choice(items=['a', 'b', 'c'], length=4, unique=True)

    # Test for unique with sufficient unique elements
    choice.random.choice.side_effect = ['a', 'b', 'c']
    result = choice(items=['a', 'b', 'c'], length=3, unique=True)
    assert result == ['a', 'b', 'c']
    assert choice.random.choice.call_count == 3
    choice.random.choice.reset_mock()

    # Test for non-unique with sufficient elements
    choice.random.choice.side_effect = ['a', 'b', 'a', 'c']
    result = choice(items=['a', 'b', 'c'], length=4, unique=False)
    assert result == ['a', 'b', 'a', 'c']
    assert choice.random.choice.call_count == 4

    # Test for list return type
    choice.random.choice.side_effect = ['a', 'b', 'c']
    result = choice(items=['a', 'b', 'c'], length=3)
    assert isinstance(result, list)

    # Test for tuple return type
    choice.random.choice.side_effect = ['a', 'b', 'c']
    result = choice(items=('a', 'b', 'c'), length=3)
    assert isinstance(result, tuple)

    # Test for string return type
    choice.random.choice.side_effect = ['a', 'b', 'c']
    result = choice(items='abc', length=3)
    assert isinstance(result, str)
