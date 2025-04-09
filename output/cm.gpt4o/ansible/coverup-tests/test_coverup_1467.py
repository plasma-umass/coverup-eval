# file lib/ansible/utils/collection_loader/_collection_config.py:85-88
# lines [88]
# branches ['87->88']

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_on_collection_load_setter_raises_value_error():
    class DummyClass(metaclass=_AnsibleCollectionConfig):
        _on_collection_load = None

    with pytest.raises(ValueError, match='on_collection_load is not directly settable \(use \+=\)'):
        DummyClass.on_collection_load = 'some_value'
