# file: lib/ansible/vars/hostvars.py:131-154
# asked: {"lines": [131, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 149, 150, 152, 153, 154], "branches": [[146, 0], [146, 147]]}
# gained: {"lines": [131, 133, 134, 135, 137, 138, 139, 140, 142, 143, 145, 146, 147, 149, 150, 152, 153, 154], "branches": [[146, 0], [146, 147]]}

import pytest
from ansible.vars.hostvars import HostVarsVars
from ansible.template import Templar

class MockTemplar:
    def __init__(self, variables, loader):
        self.variables = variables
        self.loader = loader

    def template(self, var, fail_on_undefined=False, static_vars=None):
        return var

@pytest.fixture
def mock_templar(monkeypatch):
    monkeypatch.setattr('ansible.vars.hostvars.Templar', MockTemplar)

@pytest.fixture
def hostvars():
    variables = {
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3'
    }
    loader = object()  # Mock loader object
    return HostVarsVars(variables, loader)

def test_getitem(mock_templar, hostvars):
    assert hostvars['var1'] == 'value1'
    assert hostvars['var2'] == 'value2'
    assert hostvars['var3'] == 'value3'

def test_contains(mock_templar, hostvars):
    assert 'var1' in hostvars
    assert 'var2' in hostvars
    assert 'var3' in hostvars
    assert 'var4' not in hostvars

def test_iter(mock_templar, hostvars):
    vars_list = list(iter(hostvars))
    assert vars_list == ['var1', 'var2', 'var3']

def test_len(mock_templar, hostvars):
    assert len(hostvars) == 3

def test_repr(mock_templar, hostvars):
    expected_repr = repr({
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3'
    })
    assert repr(hostvars) == expected_repr
