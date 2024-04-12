# file lib/ansible/vars/hostvars.py:131-154
# lines [134, 135, 138, 139, 140, 143, 146, 147, 150, 153, 154]
# branches ['146->exit', '146->147']

import pytest
from unittest.mock import MagicMock

# Assuming the Templar class and STATIC_VARS are defined elsewhere in the ansible codebase
# and that they are imported correctly in the test environment
from ansible.template import Templar
from ansible.vars.hostvars import HostVarsVars

# Define a test case to cover the missing lines
@pytest.fixture
def host_vars_vars():
    variables = {'a': 1, 'b': 2, 'c': 3}
    loader = MagicMock()
    return HostVarsVars(variables, loader)

def test_host_vars_vars_getitem(host_vars_vars):
    # Access an item to trigger __getitem__
    assert host_vars_vars['a'] == 1

def test_host_vars_vars_contains(host_vars_vars):
    # Check for containment to trigger __contains__
    assert 'a' in host_vars_vars
    assert 'z' not in host_vars_vars

def test_host_vars_vars_iter(host_vars_vars):
    # Iterate to trigger __iter__
    assert set(iter(host_vars_vars)) == {'a', 'b', 'c'}

def test_host_vars_vars_len(host_vars_vars):
    # Get length to trigger __len__
    assert len(host_vars_vars) == 3

def test_host_vars_vars_repr(host_vars_vars):
    # Get repr to trigger __repr__
    assert isinstance(repr(host_vars_vars), str)
