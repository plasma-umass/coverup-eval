# file lib/ansible/module_utils/common/collections.py:14-15
# lines [14, 15]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict():
    # Create an instance of ImmutableDict
    immutable = ImmutableDict({'key1': 'value1', 'key2': 'value2'})

    # Test that the dictionary returns the correct items
    assert immutable['key1'] == 'value1'
    assert immutable['key2'] == 'value2'

    # Test that the dictionary is indeed immutable by attempting to set an item
    with pytest.raises(TypeError):
        immutable['key3'] = 'value3'

    # Test that the dictionary is indeed immutable by attempting to delete an item
    with pytest.raises(TypeError):
        del immutable['key1']

    # Test that the dictionary is indeed immutable by attempting to update it
    with pytest.raises(AttributeError):
        immutable.update({'key3': 'value3'})

    # Test that the dictionary is indeed immutable by attempting to clear it
    with pytest.raises(AttributeError):
        immutable.clear()

    # Test that the dictionary is indeed immutable by attempting to pop an item
    with pytest.raises(AttributeError):
        immutable.pop('key1')

    # Test that the dictionary is indeed immutable by attempting to pop an item with a default value
    with pytest.raises(AttributeError):
        immutable.pop('key1', 'default')

    # Test that the dictionary is indeed immutable by attempting to pop an item from the end
    with pytest.raises(AttributeError):
        immutable.popitem()

    # Test that the dictionary is indeed immutable by attempting to set a default value
    with pytest.raises(AttributeError):
        immutable.setdefault('key3', 'value3')

    # Test the len function
    assert len(immutable) == 2

    # Test the iter function
    assert set(iter(immutable)) == {'key1', 'key2'}

    # Test the repr function
    assert repr(immutable) == "ImmutableDict({'key1': 'value1', 'key2': 'value2'})"

    # Test the hash function (it should not raise an exception)
    assert isinstance(hash(immutable), int)

    # Test the keys, values, and items functions
    assert set(immutable.keys()) == {'key1', 'key2'}
    assert set(immutable.values()) == {'value1', 'value2'}
    assert set(immutable.items()) == {('key1', 'value1'), ('key2', 'value2')}
