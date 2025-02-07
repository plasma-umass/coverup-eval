# file: lib/ansible/plugins/lookup/file.py:60-87
# asked: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}
# gained: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup.file import LookupModule
from ansible.module_utils._text import to_text
from unittest.mock import patch, MagicMock

@pytest.fixture
def lookup_module():
    loader = MagicMock()
    return LookupModule(loader=loader)

def test_run_with_valid_file(lookup_module, mocker):
    terms = ['valid_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value='path/to/valid_file')
    mocker.patch.object(lookup_module._loader, '_get_file_contents', return_value=(b'file contents', None))
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda option: False)
    mocker.patch('ansible.plugins.lookup.file.display')

    result = lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'files', 'valid_file')
    lookup_module._loader._get_file_contents.assert_called_once_with('path/to/valid_file')
    lookup_module.get_option.assert_any_call('lstrip')
    lookup_module.get_option.assert_any_call('rstrip')
    assert result == ['file contents']

def test_run_with_missing_file(lookup_module, mocker):
    terms = ['missing_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)
    mocker.patch('ansible.plugins.lookup.file.display')

    with pytest.raises(AnsibleError, match='could not locate file in lookup: missing_file'):
        lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'files', 'missing_file')

def test_run_with_lstrip_rstrip(lookup_module, mocker):
    terms = ['valid_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, 'set_options')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value='path/to/valid_file')
    mocker.patch.object(lookup_module._loader, '_get_file_contents', return_value=(b'  file contents  ', None))
    mocker.patch.object(lookup_module, 'get_option', side_effect=lambda option: option in ['lstrip', 'rstrip'])
    mocker.patch('ansible.plugins.lookup.file.display')

    result = lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'files', 'valid_file')
    lookup_module._loader._get_file_contents.assert_called_once_with('path/to/valid_file')
    lookup_module.get_option.assert_any_call('lstrip')
    lookup_module.get_option.assert_any_call('rstrip')
    assert result == ['file contents']
