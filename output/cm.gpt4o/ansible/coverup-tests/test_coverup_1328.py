# file lib/ansible/plugins/lookup/first_found.py:206-236
# lines []
# branches ['229->218']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.lookup.first_found import LookupModule
from ansible.errors import AnsibleLookupError

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_first_found_no_file_found(lookup_module, mocker):
    terms = ['nonexistent_file']
    variables = {}
    kwargs = {}

    # Mock the _process_terms method to return a controlled output
    mocker.patch.object(lookup_module, '_process_terms', return_value=(terms, False))
    
    # Mock the _templar attribute to have a template method
    lookup_module._templar = MagicMock()
    lookup_module._templar.template = MagicMock(side_effect=lambda x: x)
    
    # Mock the find_file_in_search_path method to always return None
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
        lookup_module.run(terms, variables, **kwargs)

def test_first_found_skip(lookup_module, mocker):
    terms = ['nonexistent_file']
    variables = {}
    kwargs = {}

    # Mock the _process_terms method to return a controlled output with skip=True
    mocker.patch.object(lookup_module, '_process_terms', return_value=(terms, True))
    
    # Mock the _templar attribute to have a template method
    lookup_module._templar = MagicMock()
    lookup_module._templar.template = MagicMock(side_effect=lambda x: x)
    
    # Mock the find_file_in_search_path method to always return None
    mocker.patch.object(lookup_module, 'find_file_in_search_path', return_value=None)

    result = lookup_module.run(terms, variables, **kwargs)
    assert result == []

