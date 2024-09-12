# file: lib/ansible/utils/collection_loader/_collection_config.py:85-88
# asked: {"lines": [85, 86, 87, 88], "branches": [[87, 0], [87, 88]]}
# gained: {"lines": [85, 86, 87, 88], "branches": [[87, 88]]}

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig

def test_on_collection_load_setter_raises_value_error():
    class DummyEventSource:
        pass

    class TestConfig(metaclass=_AnsibleCollectionConfig):
        pass

    dummy_event_source = DummyEventSource()

    with pytest.raises(ValueError, match='on_collection_load is not directly settable \(use \+=\)'):
        TestConfig.on_collection_load = dummy_event_source

    assert TestConfig.on_collection_load is not dummy_event_source
