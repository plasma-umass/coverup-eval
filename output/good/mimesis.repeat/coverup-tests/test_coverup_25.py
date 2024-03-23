# file mimesis/providers/choice.py:28-88
# lines [28, 29, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 76, 78, 79, 80, 81, 84, 85, 86, 87, 88]
# branches ['59->60', '59->62', '62->63', '62->65', '65->66', '65->68', '68->69', '68->71', '71->72', '71->74', '75->76', '75->78', '78->79', '78->84', '80->78', '80->81', '84->85', '84->86', '86->87', '86->88']

import pytest
from mimesis.providers.choice import Choice
from unittest.mock import Mock

def test_choice_non_integer_length():
    choice = Choice()
    with pytest.raises(TypeError):
        choice(items=['a', 'b', 'c'], length='1')

def test_choice_non_sequence_items():
    choice = Choice()
    with pytest.raises(TypeError):
        choice(items=None)

def test_choice_empty_sequence_items():
    choice = Choice()
    with pytest.raises(ValueError):
        choice(items=[])

def test_choice_negative_length():
    choice = Choice()
    with pytest.raises(ValueError):
        choice(items=['a', 'b', 'c'], length=-1)

def test_choice_insufficient_unique_elements():
    choice = Choice()
    with pytest.raises(ValueError):
        choice(items=['a', 'b', 'c'], length=4, unique=True)

def test_choice_return_list():
    choice = Choice()
    mock_random = Mock()
    mock_random.choice = Mock(side_effect=['a', 'b', 'c'])
    choice.random = mock_random
    result = choice(items=['a', 'b', 'c'], length=3)
    assert result == ['a', 'b', 'c']
    assert isinstance(result, list)

def test_choice_return_tuple():
    choice = Choice()
    mock_random = Mock()
    mock_random.choice = Mock(side_effect=['a', 'b', 'c'])
    choice.random = mock_random
    result = choice(items=('a', 'b', 'c'), length=3)
    assert result == ('a', 'b', 'c')
    assert isinstance(result, tuple)

def test_choice_return_string():
    choice = Choice()
    mock_random = Mock()
    mock_random.choice = Mock(side_effect=['a', 'b', 'c'])
    choice.random = mock_random
    result = choice(items='abc', length=3)
    assert result == 'abc'
    assert isinstance(result, str)
