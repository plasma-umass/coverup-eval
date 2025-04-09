# file: lib/ansible/plugins/lookup/first_found.py:206-236
# asked: {"lines": [206, 208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}
# gained: {"lines": [206, 208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236], "branches": [[218, 220], [218, 233], [229, 218], [229, 230], [233, 235], [233, 236]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
from jinja2.exceptions import UndefinedError
from ansible.plugins.lookup.first_found import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_found_file(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_process_terms', return_value=(['file1', 'file2'], False))
    mocker.patch.object(lookup_module, '_templar', create=True)
    lookup_module._templar.template = MagicMock(side_effect=lambda x: x)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', side_effect=[None, 'path/to/file2'])

    result = lookup_module.run(['file1', 'file2'], {})
    assert result == ['path/to/file2']

def test_run_no_file_found_with_skip(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_process_terms', return_value=(['file1', 'file2'], True))
    mocker.patch.object(lookup_module, '_templar', create=True)
    lookup_module._templar.template = MagicMock(side_effect=lambda x: x)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    result = lookup_module.run(['file1', 'file2'], {})
    assert result == []

def test_run_no_file_found_without_skip(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_process_terms', return_value=(['file1', 'file2'], False))
    mocker.patch.object(lookup_module, '_templar', create=True)
    lookup_module._templar.template = MagicMock(side_effect=lambda x: x)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(['file1', 'file2'], {})

def test_run_template_error(lookup_module, mocker):
    mocker.patch.object(lookup_module, '_process_terms', return_value=(['file1', 'file2'], False))
    mocker.patch.object(lookup_module, '_templar', create=True)
    lookup_module._templar.template = MagicMock(side_effect=AnsibleUndefinedVariable)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(['file1', 'file2'], {})
