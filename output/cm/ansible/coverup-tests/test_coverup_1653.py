# file lib/ansible/utils/context_objects.py:20-50
# lines [31, 39, 47]
# branches ['28->31', '36->39', '44->47']

import pytest
from ansible.utils.context_objects import _make_immutable
from collections.abc import Mapping, Set, Sequence, Container
from ansible.module_utils.six import text_type, binary_type
from ansible.module_utils.common.collections import ImmutableDict

class NonContainer:
    pass

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Teardown if necessary

def test_make_immutable_with_non_container_values(mocker):
    # Mocking the Container class to ensure isinstance check fails
    mocker.patch('ansible.utils.context_objects.Container', new=NonContainer)

    non_container_instance = NonContainer()

    # Test with a non-container value in a dict
    test_dict = {'key1': 'value1', 'key2': non_container_instance}
    immutable_dict = _make_immutable(test_dict)
    assert isinstance(immutable_dict, ImmutableDict)
    assert immutable_dict['key2'] == non_container_instance

    # Test with a non-container value in a set
    test_set = {'value1', non_container_instance}
    immutable_set = _make_immutable(test_set)
    assert isinstance(immutable_set, frozenset)
    assert non_container_instance in immutable_set

    # Test with a non-container value in a list
    test_list = ['value1', non_container_instance]
    immutable_list = _make_immutable(test_list)
    assert isinstance(immutable_list, tuple)
    assert non_container_instance in immutable_list
