# file lib/ansible/vars/clean.py:98-115
# lines [102, 103, 104, 105, 108, 109, 110, 113, 114, 115]
# branches ['102->103', '102->108', '103->102', '103->104', '108->109', '108->113', '109->108', '109->110', '113->exit', '113->114', '114->113', '114->115']

import pytest
from ansible.vars.clean import remove_internal_keys
from ansible.utils.display import Display
from ansible import constants as C

# Mock the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.vars.clean.display', autospec=True)
    mock.warning = mocker.MagicMock()
    return mock

# Test function to cover lines 102-115
def test_remove_internal_keys(mock_display):
    # Setup test data with keys that should trigger the removal logic
    test_data = {
        '_ansible_verbose_always': True,
        '_ansible_no_log': False,
        'warnings': [],
        'deprecations': [],
        'ansible_facts': {
            'discovered_interpreter_python': '/usr/bin/python',
            'ansible_discovered_interpreter_python': '/usr/bin/python',
            'other_fact': 'value'
        }
    }

    # Expected data after cleaning
    expected_data = {
        'ansible_facts': {
            'other_fact': 'value'
        }
    }

    # Call the function to be tested
    remove_internal_keys(test_data)

    # Assertions to verify postconditions
    assert test_data == expected_data
    assert mock_display.warning.call_count == 2
    mock_display.warning.assert_any_call("Removed unexpected internal key in module return: _ansible_verbose_always = True")
    mock_display.warning.assert_any_call("Removed unexpected internal key in module return: _ansible_no_log = False")

# Run the test
def test_run_remove_internal_keys(mock_display):
    test_remove_internal_keys(mock_display)
