# file: lib/ansible/modules/apt_repository.py:366-369
# asked: {"lines": [366, 367, 368, 369], "branches": [[367, 368], [367, 369]]}
# gained: {"lines": [366, 367, 368, 369], "branches": [[367, 368], [367, 369]]}

import pytest
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list(monkeypatch):
    def mock_apt_cfg_file(filespec):
        return '/dev/null'
    
    def mock_apt_cfg_dir(dirspec):
        return '/dev/null'
    
    monkeypatch.setattr(SourcesList, '_apt_cfg_file', staticmethod(mock_apt_cfg_file))
    monkeypatch.setattr(SourcesList, '_apt_cfg_dir', staticmethod(mock_apt_cfg_dir))
    
    return SourcesList(module=None)

def test_choice_new_is_none(sources_list):
    result = sources_list._choice(None, 'old_value')
    assert result == 'old_value', "Expected 'old_value' when new is None"

def test_choice_new_is_not_none(sources_list):
    result = sources_list._choice('new_value', 'old_value')
    assert result == 'new_value', "Expected 'new_value' when new is not None"
