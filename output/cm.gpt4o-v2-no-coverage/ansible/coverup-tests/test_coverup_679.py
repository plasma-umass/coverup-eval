# file: lib/ansible/modules/apt_repository.py:366-369
# asked: {"lines": [366, 367, 368, 369], "branches": [[367, 368], [367, 369]]}
# gained: {"lines": [366, 367, 368, 369], "branches": [[367, 368], [367, 369]]}

import pytest
from ansible.modules.apt_repository import SourcesList

class MockModule:
    pass

@pytest.fixture
def sources_list(monkeypatch):
    def mock_apt_cfg_file(filespec):
        return '/mock/path/sources.list'
    
    def mock_apt_cfg_dir(dirspec):
        return '/mock/path/sources.list.d'
    
    monkeypatch.setattr(SourcesList, '_apt_cfg_file', staticmethod(mock_apt_cfg_file))
    monkeypatch.setattr(SourcesList, '_apt_cfg_dir', staticmethod(mock_apt_cfg_dir))
    module = MockModule()
    return SourcesList(module)

def test_choice_new_is_none(sources_list):
    assert sources_list._choice(None, 'old_value') == 'old_value'

def test_choice_new_is_not_none(sources_list):
    assert sources_list._choice('new_value', 'old_value') == 'new_value'
