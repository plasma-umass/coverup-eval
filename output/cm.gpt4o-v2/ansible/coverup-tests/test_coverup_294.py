# file: lib/ansible/inventory/host.py:57-69
# asked: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}
# gained: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68], "branches": [[59, 60], [59, 62]]}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.host import Host

@pytest.fixture
def host():
    return Host(name="test_host")

def test_serialize_no_groups(host):
    host.vars = {"var1": "value1"}
    host._uuid = "1234-5678"
    host.implicit = True

    expected_output = {
        "name": "test_host",
        "vars": {"var1": "value1"},
        "address": "test_host",
        "uuid": "1234-5678",
        "groups": [],
        "implicit": True,
    }

    assert host.serialize() == expected_output

def test_serialize_with_groups(host):
    group_mock = MagicMock()
    group_mock.serialize.return_value = {"group_var": "group_value"}
    host.groups = [group_mock]
    host.vars = {"var1": "value1"}
    host._uuid = "1234-5678"
    host.implicit = True

    expected_output = {
        "name": "test_host",
        "vars": {"var1": "value1"},
        "address": "test_host",
        "uuid": "1234-5678",
        "groups": [{"group_var": "group_value"}],
        "implicit": True,
    }

    assert host.serialize() == expected_output
