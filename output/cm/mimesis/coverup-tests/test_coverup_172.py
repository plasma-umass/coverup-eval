# file mimesis/providers/choice.py:28-88
# lines [60, 63, 69, 78, 79, 80, 81, 84, 85, 86, 87, 88]
# branches ['59->60', '62->63', '68->69', '75->78', '78->79', '78->84', '80->78', '80->81', '84->85', '84->86', '86->87', '86->88']

import pytest
from mimesis.providers.choice import Choice
from unittest.mock import Mock

def test_choice_coverage():
    choice_provider = Choice()
    choice_provider.random = Mock()

    # Test for TypeError on non-integer length
    with pytest.raises(TypeError):
        choice_provider(items=['a', 'b', 'c'], length='1')

    # Test for TypeError on non-sequence items
    with pytest.raises(TypeError):
        choice_provider(items=123, length=1)

    # Test for ValueError on negative length
    with pytest.raises(ValueError):
        choice_provider(items=['a', 'b', 'c'], length=-1)

    # Test for ValueError on empty items
    with pytest.raises(ValueError):
        choice_provider(items=[], length=1)

    # Test for ValueError on unique with insufficient unique elements
    with pytest.raises(ValueError):
        choice_provider(items=['a', 'a'], length=2, unique=True)

    # Test for unique path
    choice_provider.random.choice.side_effect = ['a', 'b', 'c']
    result = choice_provider(items=['a', 'b', 'c'], length=3, unique=True)
    assert result == ['a', 'b', 'c']

    # Test for non-unique path
    choice_provider.random.choice.side_effect = ['a', 'a', 'b']
    result = choice_provider(items=['a', 'b', 'c'], length=3, unique=False)
    assert result == ['a', 'a', 'b']

    # Test for returning a list
    choice_provider.random.choice.side_effect = ['a', 'b', 'c']
    result = choice_provider(items=['a', 'b', 'c'], length=3)
    assert result == ['a', 'b', 'c'] and isinstance(result, list)

    # Test for returning a tuple
    choice_provider.random.choice.side_effect = ['a', 'b', 'c']
    result = choice_provider(items=('a', 'b', 'c'), length=3)
    assert result == ('a', 'b', 'c') and isinstance(result, tuple)

    # Test for returning a string
    choice_provider.random.choice.side_effect = ['a', 'b', 'c']
    result = choice_provider(items='abc', length=3)
    assert result == 'abc' and isinstance(result, str)
