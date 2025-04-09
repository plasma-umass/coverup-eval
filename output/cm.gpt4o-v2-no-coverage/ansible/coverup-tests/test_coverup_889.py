# file: lib/ansible/inventory/host.py:34-35
# asked: {"lines": [34, 35], "branches": []}
# gained: {"lines": [34, 35], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

def test_serialize(host, mocker):
    mock_group = MagicMock()
    mock_group.serialize.return_value = {"name": "group1"}
    host.groups = [mock_group]
    host.vars = {"var1": "value1"}
    host._uuid = "1234-5678"
    host.implicit = True

    expected_output = {
        "name": "test_host",
        "vars": {"var1": "value1"},
        "address": "test_host",
        "uuid": "1234-5678",
        "groups": [{"name": "group1"}],
        "implicit": True
    }

    assert host.serialize() == expected_output

def test_getstate(host, mocker):
    mock_serialize = mocker.patch.object(host, 'serialize', return_value={"name": "test_host"})
    assert host.__getstate__() == {"name": "test_host"}
    mock_serialize.assert_called_once()
