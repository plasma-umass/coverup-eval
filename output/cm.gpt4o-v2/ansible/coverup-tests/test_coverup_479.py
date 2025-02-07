# file: lib/ansible/template/vars.py:108-122
# asked: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}
# gained: {"lines": [108, 113, 114, 119, 120, 122], "branches": [[113, 114], [113, 119]]}

import pytest
from ansible.template.vars import AnsibleJ2Vars

class MockTemplar:
    pass

@pytest.fixture
def templar():
    return MockTemplar()

@pytest.fixture
def globals():
    return {'global_var': 'value'}

@pytest.fixture
def locals():
    return {'local_var': 'value'}

def test_add_locals_with_none(templar, globals):
    j2vars = AnsibleJ2Vars(templar, globals)
    result = j2vars.add_locals(None)
    assert result is j2vars

def test_add_locals_with_values(templar, globals, locals):
    j2vars = AnsibleJ2Vars(templar, globals)
    result = j2vars.add_locals(locals)
    assert result is not j2vars
    assert isinstance(result, AnsibleJ2Vars)
    assert result._locals['local_var'] == 'value'
    assert 'global_var' in result._globals
