# file: lib/ansible/playbook/play.py:133-138
# asked: {"lines": [137], "branches": [[136, 137]]}
# gained: {"lines": [137], "branches": [[136, 137]]}

import pytest
from ansible.playbook.play import Play

class MockPlay(Play):
    def load_data(self, data, variable_manager=None, loader=None):
        return self

def test_play_load_with_vars(monkeypatch):
    data = {}  # Assuming some data structure is required
    variable_manager = None
    loader = None
    vars = {'key': 'value'}

    monkeypatch.setattr(Play, 'load_data', MockPlay.load_data)
    play_instance = Play.load(data, variable_manager=variable_manager, loader=loader, vars=vars)
    
    assert hasattr(play_instance, 'vars')
    assert play_instance.vars == vars

def test_play_load_without_vars(monkeypatch):
    data = {}  # Assuming some data structure is required
    variable_manager = None
    loader = None
    vars = None

    monkeypatch.setattr(Play, 'load_data', MockPlay.load_data)
    play_instance = Play.load(data, variable_manager=variable_manager, loader=loader, vars=vars)
    
    assert play_instance.vars == {}
