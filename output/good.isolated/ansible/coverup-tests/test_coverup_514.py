# file lib/ansible/utils/vars.py:46-55
# lines [46, 48, 49, 50, 51, 52, 53, 54]
# branches []

import pytest
from unittest.mock import patch
from ansible.utils.vars import get_unique_id

# Assuming the module ansible.utils.vars has the following global variables
# node_mac and random_int which are used in the get_unique_id function.
# We will mock these variables for our test.

@pytest.fixture
def unique_id_env_setup(mocker):
    # Setup the environment for the test
    mocker.patch('ansible.utils.vars.node_mac', '001122334455')
    mocker.patch('ansible.utils.vars.random_int', 'aabbccddeeff')
    mocker.patch('ansible.utils.vars.cur_id', -1)  # Start with -1 so first id will be 0

def test_get_unique_id(unique_id_env_setup):
    # Test the get_unique_id function to ensure it generates the correct format
    first_id = get_unique_id()
    second_id = get_unique_id()

    # Verify that the IDs are unique
    assert first_id != second_id

    # Verify the structure of the ID
    assert len(first_id.split('-')) == 5
    assert first_id.split('-')[0] == '00112233'
    assert first_id.split('-')[1] == '4455'
    assert first_id.split('-')[2] == 'aabb'
    assert first_id.split('-')[3] == 'ccdd'
    assert len(first_id.split('-')[4]) == 12  # Ensure the last part is 12 characters long

    # Verify that the cur_id has been incremented correctly
    assert int(first_id.split('-')[4], 16) == 0
    assert int(second_id.split('-')[4], 16) == 1

# Note: The actual implementation of the get_unique_id function may differ from the provided snippet.
# The above test assumes that the function uses global variables node_mac, random_int, and cur_id.
# If the actual implementation differs, the test may need to be adjusted accordingly.
