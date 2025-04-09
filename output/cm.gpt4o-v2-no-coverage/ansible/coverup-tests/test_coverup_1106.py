# file: lib/ansible/plugins/lookup/file.py:60-87
# asked: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}
# gained: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup.file import LookupModule

@pytest.fixture
def lookup_module():
    loader = MagicMock()
    templar = MagicMock()
    lookup = LookupModule(loader=loader, templar=templar)
    lookup._load_name = 'file'
    return lookup

def test_run_success(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/mock/path']}
    kwargs = {}

    mock_file_contents = (b"file content", None)
    mock_find_file = '/mock/path/testfile'
    
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda *args, **kwargs: mock_find_file)
    monkeypatch.setattr(lookup_module._loader, '_get_file_contents', lambda *args, **kwargs: mock_file_contents)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: False)
    
    result = lookup_module.run(terms, variables, **kwargs)
    
    assert result == ["file content"]

def test_run_file_not_found(lookup_module, monkeypatch):
    terms = ['nonexistentfile']
    variables = {'ansible_search_path': ['/mock/path']}
    kwargs = {}

    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda *args, **kwargs: None)
    
    with pytest.raises(AnsibleError, match="could not locate file in lookup: nonexistentfile"):
        lookup_module.run(terms, variables, **kwargs)

def test_run_with_lstrip(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/mock/path']}
    kwargs = {}

    mock_file_contents = (b"   file content", None)
    mock_find_file = '/mock/path/testfile'
    
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda *args, **kwargs: mock_find_file)
    monkeypatch.setattr(lookup_module._loader, '_get_file_contents', lambda *args, **kwargs: mock_file_contents)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: option == 'lstrip')
    
    result = lookup_module.run(terms, variables, **kwargs)
    
    assert result == ["file content"]

def test_run_with_rstrip(lookup_module, monkeypatch):
    terms = ['testfile']
    variables = {'ansible_search_path': ['/mock/path']}
    kwargs = {}

    mock_file_contents = (b"file content   ", None)
    mock_find_file = '/mock/path/testfile'
    
    monkeypatch.setattr(lookup_module, 'find_file_in_search_path', lambda *args, **kwargs: mock_find_file)
    monkeypatch.setattr(lookup_module._loader, '_get_file_contents', lambda *args, **kwargs: mock_file_contents)
    monkeypatch.setattr(lookup_module, 'get_option', lambda option: option == 'rstrip')
    
    result = lookup_module.run(terms, variables, **kwargs)
    
    assert result == ["file content"]
