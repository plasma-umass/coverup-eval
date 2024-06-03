# file lib/ansible/plugins/lookup/first_found.py:206-236
# lines [206, 208, 215, 217, 218, 220, 221, 222, 223, 226, 229, 230, 233, 235, 236]
# branches ['218->220', '218->233', '229->218', '229->230', '233->235', '233->236']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.lookup.first_found import LookupModule
from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
from jinja2 import UndefinedError

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_no_file_found(lookup_module, mocker):
    terms = ['nonexistent_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, '_process_terms', return_value=(terms, False))
    mocker.patch.object(lookup_module, '_templar', create=True)
    mocker.patch.object(lookup_module._templar, 'template', side_effect=AnsibleUndefinedVariable)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)

def test_run_skip_no_file_found(lookup_module, mocker):
    terms = ['nonexistent_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, '_process_terms', return_value=(terms, True))
    mocker.patch.object(lookup_module, '_templar', create=True)
    mocker.patch.object(lookup_module._templar, 'template', side_effect=AnsibleUndefinedVariable)
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []

def test_run_file_found(lookup_module, mocker):
    terms = ['existent_file']
    variables = {}
    kwargs = {}

    mocker.patch.object(lookup_module, '_process_terms', return_value=(terms, False))
    mocker.patch.object(lookup_module, '_templar', create=True)
    mocker.patch.object(lookup_module._templar, 'template', return_value='existent_file')
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value='/path/to/existent_file')

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == ['/path/to/existent_file']
