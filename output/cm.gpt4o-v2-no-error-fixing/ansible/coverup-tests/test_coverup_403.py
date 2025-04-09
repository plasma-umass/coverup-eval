# file: lib/ansible/utils/collection_loader/_collection_config.py:85-88
# asked: {"lines": [85, 86, 87, 88], "branches": [[87, 0], [87, 88]]}
# gained: {"lines": [85, 86, 87, 88], "branches": [[87, 88]]}

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig, _EventSource

def test_on_collection_load_setter_raises_value_error():
    class TestClass(metaclass=_AnsibleCollectionConfig):
        pass

    with pytest.raises(ValueError, match='on_collection_load is not directly settable \(use \+=\)'):
        TestClass.on_collection_load = _EventSource()

def test_on_collection_load_setter_no_raise():
    class TestClass(metaclass=_AnsibleCollectionConfig):
        pass

    original_event_source = TestClass._on_collection_load
    TestClass._on_collection_load = _EventSource()
    assert TestClass._on_collection_load is not original_event_source
