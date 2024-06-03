# file lib/ansible/utils/vars.py:46-55
# lines [46, 48, 49, 50, 51, 52, 53, 54]
# branches []

import pytest
from unittest import mock

# Assuming the function get_unique_id is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in ansible.utils.vars

# Mocking the global variables
@pytest.fixture
def mock_globals(mocker):
    mocker.patch('ansible.utils.vars.cur_id', 0)
    mocker.patch('ansible.utils.vars.node_mac', '001122334455')
    mocker.patch('ansible.utils.vars.random_int', 'a1b2c3d4')

def test_get_unique_id(mock_globals):
    from ansible.utils.vars import get_unique_id

    # Call the function to ensure it executes
    unique_id = get_unique_id()

    # Assert the unique_id is in the expected format
    assert unique_id == "00112233-4455-a1b2-c3d4-000000000001"

    # Call the function again to check increment
    unique_id = get_unique_id()
    assert unique_id == "00112233-4455-a1b2-c3d4-000000000002"
