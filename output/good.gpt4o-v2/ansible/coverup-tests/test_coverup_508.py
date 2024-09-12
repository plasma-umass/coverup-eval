# file: lib/ansible/utils/vars.py:46-55
# asked: {"lines": [46, 48, 49, 50, 51, 52, 53, 54], "branches": []}
# gained: {"lines": [46, 48, 49, 50, 51, 52, 53, 54], "branches": []}

import pytest
from ansible.utils.vars import get_unique_id

def test_get_unique_id(monkeypatch):
    # Setup the initial state
    monkeypatch.setattr('ansible.utils.vars.cur_id', 0)
    monkeypatch.setattr('ansible.utils.vars.node_mac', '123456789abc')
    monkeypatch.setattr('ansible.utils.vars.random_int', 'deadbeef')

    # Call the function and check the result
    unique_id = get_unique_id()
    assert unique_id == '12345678-9abc-dead-beef-000000000001'

    # Call the function again to ensure cur_id increments
    unique_id = get_unique_id()
    assert unique_id == '12345678-9abc-dead-beef-000000000002'
