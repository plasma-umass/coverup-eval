# file: lib/ansible/utils/collection_loader/_collection_config.py:51-54
# asked: {"lines": [51, 52, 53, 54], "branches": []}
# gained: {"lines": [51, 52, 53, 54], "branches": []}

import pytest
from ansible.utils.collection_loader._collection_config import _AnsibleCollectionConfig, _EventSource

def test_ansible_collection_config_init(monkeypatch):
    class MockEventSource:
        pass

    monkeypatch.setattr('ansible.utils.collection_loader._collection_config._EventSource', MockEventSource)

    class TestClass(metaclass=_AnsibleCollectionConfig):
        pass

    assert TestClass._collection_finder is None
    assert TestClass._default_collection is None
    assert isinstance(TestClass._on_collection_load, MockEventSource)
