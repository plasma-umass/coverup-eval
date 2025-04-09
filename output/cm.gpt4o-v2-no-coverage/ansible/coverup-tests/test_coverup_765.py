# file: lib/ansible/playbook/playbook_include.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.playbook_include import PlaybookInclude

class MockLoader:
    pass

@pytest.fixture
def mock_loader():
    return MockLoader()

def test_playbook_include_load(monkeypatch, mock_loader):
    data = {'key': 'value'}
    basedir = '/mock/basedir'
    variable_manager = {'var': 'manager'}

    def mock_load_data(self, ds, basedir, variable_manager=None, loader=None):
        assert ds == data
        assert basedir == basedir
        assert variable_manager == variable_manager
        assert loader == mock_loader
        return 'mocked'

    monkeypatch.setattr(PlaybookInclude, 'load_data', mock_load_data)

    result = PlaybookInclude.load(data, basedir, variable_manager, mock_loader)
    assert result == 'mocked'
