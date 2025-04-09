# file: lib/ansible/playbook/play.py:133-138
# asked: {"lines": [133, 134, 135, 136, 137, 138], "branches": [[136, 137], [136, 138]]}
# gained: {"lines": [133, 134, 135, 136, 137, 138], "branches": [[136, 137], [136, 138]]}

import pytest
from ansible.playbook.play import Play

def test_play_load_with_vars(monkeypatch):
    data = {'some': 'data'}
    variable_manager = 'variable_manager'
    loader = 'loader'
    vars = {'key': 'value'}

    def mock_load_data(self, data, variable_manager=None, loader=None):
        assert self.vars == vars
        assert data == {'some': 'data'}
        assert variable_manager == 'variable_manager'
        assert loader == 'loader'
        return 'mocked'

    monkeypatch.setattr(Play, 'load_data', mock_load_data)

    result = Play.load(data, variable_manager=variable_manager, loader=loader, vars=vars)
    assert result == 'mocked'

def test_play_load_without_vars(monkeypatch):
    data = {'some': 'data'}
    variable_manager = 'variable_manager'
    loader = 'loader'

    def mock_load_data(self, data, variable_manager=None, loader=None):
        assert self.vars == {}
        assert data == {'some': 'data'}
        assert variable_manager == 'variable_manager'
        assert loader == 'loader'
        return 'mocked'

    monkeypatch.setattr(Play, 'load_data', mock_load_data)

    result = Play.load(data, variable_manager=variable_manager, loader=loader)
    assert result == 'mocked'
