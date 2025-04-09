# file: flutils/namedtupleutils.py:141-177
# asked: {"lines": [169], "branches": [[156, 169], [163, 169]]}
# gained: {"lines": [169], "branches": [[156, 169]]}

import pytest
from collections import namedtuple
from typing import Sequence, NamedTuple, Union, List, Any, Tuple, cast

# Assuming the function _to_namedtuple is imported from flutils.namedtupleutils
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_namedtuple_no_fields():
    # Define a NamedTuple with no fields
    EmptyNamedTuple = namedtuple('EmptyNamedTuple', [])
    empty_named_tuple_instance = EmptyNamedTuple()

    # Call the function and assert the result
    result = _to_namedtuple(empty_named_tuple_instance)
    assert result == empty_named_tuple_instance

def test_to_namedtuple_with_namedtuple_with_fields():
    # Define a NamedTuple with fields
    Person = namedtuple('Person', ['name', 'age'])
    person_instance = Person(name='Alice', age=30)

    # Call the function and assert the result
    result = _to_namedtuple(person_instance)
    assert isinstance(result, tuple)
    assert result.name == 'Alice'
    assert result.age == 30

def test_to_namedtuple_with_list():
    # Define a list
    data = [1, 2, 3]

    # Call the function and assert the result
    result = _to_namedtuple(data)
    assert result == data

def test_to_namedtuple_with_tuple():
    # Define a tuple
    data = (1, 2, 3)

    # Call the function and assert the result
    result = _to_namedtuple(data)
    assert result == data

def test_to_namedtuple_with_string():
    # Define a string
    data = "test"

    # Call the function and assert the result
    with pytest.raises(TypeError):
        _to_namedtuple(data)

@pytest.fixture
def mock_namedtupleutils(monkeypatch):
    # Mock the _to_namedtuple function to avoid state pollution
    from flutils import namedtupleutils
    original_function = namedtupleutils._to_namedtuple
    monkeypatch.setattr(namedtupleutils, "_to_namedtuple", original_function)
    yield
    monkeypatch.undo()

@pytest.mark.usefixtures("mock_namedtupleutils")
def test_to_namedtuple_with_nested_namedtuple():
    # Define nested NamedTuples
    Address = namedtuple('Address', ['city', 'zipcode'])
    Person = namedtuple('Person', ['name', 'age', 'address'])
    address_instance = Address(city='Wonderland', zipcode='12345')
    person_instance = Person(name='Alice', age=30, address=address_instance)

    # Call the function and assert the result
    result = _to_namedtuple(person_instance)
    assert isinstance(result, tuple)
    assert result.name == 'Alice'
    assert result.age == 30
    assert isinstance(result.address, tuple)
    assert result.address.city == 'Wonderland'
    assert result.address.zipcode == '12345'
