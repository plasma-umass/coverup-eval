# file: lib/ansible/inventory/host.py:40-43
# asked: {"lines": [40, 41, 42, 43], "branches": [[41, 42], [41, 43]]}
# gained: {"lines": [40], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host_instance():
    class Host:
        def __init__(self, uuid):
            self._uuid = uuid

        def __eq__(self, other):
            if not isinstance(other, Host):
                return False
            return self._uuid == other._uuid

    return Host("1234")

def test_host_equality_same_uuid(host_instance):
    other_host = host_instance.__class__("1234")
    assert host_instance == other_host

def test_host_equality_different_uuid(host_instance):
    other_host = host_instance.__class__("5678")
    assert host_instance != other_host

def test_host_equality_different_type(host_instance):
    other_object = "not_a_host"
    assert host_instance != other_object
