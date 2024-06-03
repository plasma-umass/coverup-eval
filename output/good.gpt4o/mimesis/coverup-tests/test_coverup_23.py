# file mimesis/providers/choice.py:28-88
# lines [28, 29, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 76, 78, 79, 80, 81, 84, 85, 86, 87, 88]
# branches ['59->60', '59->62', '62->63', '62->65', '65->66', '65->68', '68->69', '68->71', '71->72', '71->74', '75->76', '75->78', '78->79', '78->84', '80->78', '80->81', '84->85', '84->86', '86->87', '86->88']

import pytest
from mimesis.providers.choice import Choice
import collections.abc

def test_choice_length_not_int():
    choice = Choice()
    with pytest.raises(TypeError, match=r'\*\*length\*\* must be integer\.'):
        choice(items=['a', 'b', 'c'], length='not_an_int')

def test_choice_items_not_sequence():
    choice = Choice()
    with pytest.raises(TypeError, match=r'\*\*items\*\* must be non-empty sequence\.'):
        choice(items=123, length=1)

def test_choice_items_empty():
    choice = Choice()
    with pytest.raises(ValueError, match=r'\*\*items\*\* must be a non-empty sequence\.'):
        choice(items=[], length=1)

def test_choice_length_negative():
    choice = Choice()
    with pytest.raises(ValueError, match=r'\*\*length\*\* should be a positive integer\.'):
        choice(items=['a', 'b', 'c'], length=-1)

def test_choice_unique_not_enough_elements():
    choice = Choice()
    with pytest.raises(ValueError, match=r'There are not enough unique elements in \*\*items\*\* to provide the specified \*\*number\*\*\.'):
        choice(items=['a', 'b'], length=3, unique=True)

def test_choice_length_zero():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'], length=0)
    assert result in ['a', 'b', 'c']

def test_choice_return_list():
    choice = Choice()
    result = choice(items=['a', 'b', 'c'], length=2)
    assert isinstance(result, list)
    assert len(result) == 2

def test_choice_return_tuple():
    choice = Choice()
    result = choice(items=('a', 'b', 'c'), length=2)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_choice_return_string():
    choice = Choice()
    result = choice(items='abc', length=2)
    assert isinstance(result, str)
    assert len(result) == 2

def test_choice_unique_elements():
    choice = Choice()
    result = choice(items='aabbcc', length=3, unique=True)
    assert len(result) == 3
    assert len(set(result)) == 3
