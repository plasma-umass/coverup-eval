# file lib/ansible/utils/collection_loader/_collection_config.py:85-88
# lines [85, 86, 87, 88]
# branches ['87->exit', '87->88']

import pytest
from ansible.utils.collection_loader import _collection_config

class MockedAnsibleCollectionConfig(metaclass=_collection_config._AnsibleCollectionConfig):
    _on_collection_load = None

def test_on_collection_load_setter_raises_value_error():
    with pytest.raises(ValueError) as excinfo:
        MockedAnsibleCollectionConfig.on_collection_load = 'new_value'
    
    assert str(excinfo.value) == 'on_collection_load is not directly settable (use +=)'
