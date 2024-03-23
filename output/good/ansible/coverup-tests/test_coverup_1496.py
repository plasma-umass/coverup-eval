# file lib/ansible/playbook/included_file.py:60-61
# lines [61]
# branches []

import pytest
from ansible.playbook.included_file import IncludedFile

# Mock class to represent the IncludedFile with the necessary attributes
class MockIncludedFile(IncludedFile):
    def __init__(self, filename, args, vars, hosts):
        self._filename = filename
        self._args = args
        self._vars = vars
        self._hosts = hosts

# Test function to cover the __repr__ method
def test_included_file_repr():
    # Setup the mock object with test data
    test_filename = "test_file.yml"
    test_args = {'test_arg': 'value'}
    test_vars = {'test_var': 'value'}
    test_hosts = ['host1', 'host2']
    included_file = MockIncludedFile(test_filename, test_args, test_vars, test_hosts)

    # Expected representation format
    expected_repr = "test_file.yml (args={'test_arg': 'value'} vars={'test_var': 'value'}): ['host1', 'host2']"

    # Assert that the __repr__ method returns the expected string
    assert repr(included_file) == expected_repr

    # No cleanup required as no external state is modified
