# file lib/ansible/utils/vars.py:213-232
# lines [213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 232]
# branches ['215->216', '215->217', '227->228', '227->232', '229->227', '229->230']

import pytest
from unittest.mock import MagicMock

# Assuming the context module and CLIARGS are accessible from ansible.utils.context
# Since the import failed, we'll mock the context and CLIARGS directly

# Mock the context.CLIARGS to simulate the command line arguments
@pytest.fixture
def mock_cliargs(mocker):
    cliargs = {
        'check': True,
        'diff': False,
        'forks': 5,
        'inventory': '/path/to/inventory',
        'skip_tags': ['test_tag'],
        'subset': 'all',
        'tags': ['build'],
        'verbosity': 3
    }
    mocker.patch('ansible.utils.vars.context.CLIARGS', cliargs)

# Test function to improve coverage
def test_load_options_vars_with_all_attrs(mock_cliargs):
    from ansible.utils.vars import load_options_vars

    # Call the function with a specific version
    options_vars = load_options_vars('2.9.0')

    # Assertions to check if the function behaves as expected
    assert options_vars['ansible_version'] == '2.9.0'
    assert options_vars['ansible_check_mode'] is True
    assert options_vars['ansible_diff_mode'] is False
    assert options_vars['ansible_forks'] == 5
    assert options_vars['ansible_inventory_sources'] == '/path/to/inventory'
    assert options_vars['ansible_skip_tags'] == ['test_tag']
    assert options_vars['ansible_limit'] == 'all'
    assert options_vars['ansible_run_tags'] == ['build']
    assert options_vars['ansible_verbosity'] == 3

# Test function to improve coverage when version is None
def test_load_options_vars_with_none_version(mock_cliargs):
    from ansible.utils.vars import load_options_vars

    # Call the function without specifying a version
    options_vars = load_options_vars(None)

    # Assertions to check if the function behaves as expected
    assert options_vars['ansible_version'] == 'Unknown'
    assert options_vars['ansible_check_mode'] is True
    assert options_vars['ansible_diff_mode'] is False
    assert options_vars['ansible_forks'] == 5
    assert options_vars['ansible_inventory_sources'] == '/path/to/inventory'
    assert options_vars['ansible_skip_tags'] == ['test_tag']
    assert options_vars['ansible_limit'] == 'all'
    assert options_vars['ansible_run_tags'] == ['build']
    assert options_vars['ansible_verbosity'] == 3
