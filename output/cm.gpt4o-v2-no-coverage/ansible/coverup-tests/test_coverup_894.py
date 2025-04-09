# file: lib/ansible/inventory/host.py:45-46
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest
from ansible.inventory.host import Host

@pytest.fixture
def host_a():
    return Host(name="host_a")

@pytest.fixture
def host_b():
    return Host(name="host_b")

def test_host_ne_with_equal_hosts(host_a, host_b, mocker):
    mocker.patch.object(host_a, '_uuid', '1234')
    mocker.patch.object(host_b, '_uuid', '1234')
    assert not host_a != host_b  # They are equal, so __ne__ should return False

def test_host_ne_with_different_hosts(host_a, host_b, mocker):
    mocker.patch.object(host_a, '_uuid', '1234')
    mocker.patch.object(host_b, '_uuid', '5678')
    assert host_a != host_b  # They are not equal, so __ne__ should return True

def test_host_ne_with_non_host_object(host_a):
    assert host_a != "not_a_host"  # Comparing with a non-Host object should return True
