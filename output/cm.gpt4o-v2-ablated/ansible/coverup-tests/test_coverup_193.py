# file: lib/ansible/utils/vars.py:46-55
# asked: {"lines": [46, 48, 49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [46, 48, 49, 50, 51, 52, 53, 54], "branches": []}

import pytest

# Assuming the global variables are defined somewhere in the module
# For the purpose of this test, we will define them here
cur_id = 0
node_mac = "001122334455"
random_int = "a1b2c3d4e5f6"

from ansible.utils.vars import get_unique_id

@pytest.fixture(autouse=True)
def setup_globals(monkeypatch):
    global cur_id, node_mac, random_int
    cur_id = 0
    node_mac = "001122334455"
    random_int = "a1b2c3d4e5f6"
    monkeypatch.setattr('ansible.utils.vars.cur_id', cur_id)
    monkeypatch.setattr('ansible.utils.vars.node_mac', node_mac)
    monkeypatch.setattr('ansible.utils.vars.random_int', random_int)
    yield
    # Cleanup if necessary
    cur_id = 0

def test_get_unique_id(monkeypatch):
    global cur_id
    cur_id = 0
    monkeypatch.setattr('ansible.utils.vars.cur_id', cur_id)
    
    unique_id = get_unique_id()
    assert unique_id == "00112233-4455-a1b2-c3d4-000000000001"
    
    unique_id = get_unique_id()
    assert unique_id == "00112233-4455-a1b2-c3d4-000000000002"
    
    # Test with different node_mac and random_int
    monkeypatch.setattr('ansible.utils.vars.node_mac', "aabbccddeeff")
    monkeypatch.setattr('ansible.utils.vars.random_int', "1234567890ab")
    
    unique_id = get_unique_id()
    assert unique_id == "aabbccdd-eeff-1234-5678-000000000003"
    
    unique_id = get_unique_id()
    assert unique_id == "aabbccdd-eeff-1234-5678-000000000004"
