# file lib/ansible/module_utils/common/collections.py:16-17
# lines [16, 17]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_initialization():
    # Test initialization with positional arguments
    data = (('key1', 'value1'), ('key2', 'value2'))
    imm_dict = ImmutableDict(data)
    assert imm_dict._store == dict(data)

    # Test initialization with keyword arguments
    imm_dict = ImmutableDict(key1='value1', key2='value2')
    assert imm_dict._store == {'key1': 'value1', 'key2': 'value2'}

    # Test initialization with both positional and keyword arguments
    imm_dict = ImmutableDict({'key1': 'value1'}, key2='value2')
    assert imm_dict._store == {'key1': 'value1', 'key2': 'value2'}

    # Test initialization with no arguments
    imm_dict = ImmutableDict()
    assert imm_dict._store == {}

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
