# file: lib/ansible/plugins/lookup/first_found.py:206-236
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleLookupError, AnsibleUndefinedVariable
from jinja2.exceptions import UndefinedError
from ansible.plugins.lookup.first_found import LookupModule
from ansible.template import Templar
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def lookup_module():
    loader = DataLoader()
    templar = Templar(loader=loader)
    return LookupModule(loader=loader, templar=templar)

def test_run_handles_undefined_variable(lookup_module, monkeypatch):
    terms = ['{{ undefined_variable }}']
    variables = {}
    kwargs = {}

    mock_template = MagicMock(side_effect=AnsibleUndefinedVariable)
    monkeypatch.setattr(lookup_module._templar, 'template', mock_template)

    with patch.object(lookup_module, '_process_terms', return_value=(terms, False)):
        with patch.object(lookup_module, 'find_file_in_search_path', return_value=None):
            with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
                lookup_module.run(terms, variables, **kwargs)

def test_run_handles_undefined_error(lookup_module, monkeypatch):
    terms = ['{{ undefined_variable }}']
    variables = {}
    kwargs = {}

    mock_template = MagicMock(side_effect=UndefinedError)
    monkeypatch.setattr(lookup_module._templar, 'template', mock_template)

    with patch.object(lookup_module, '_process_terms', return_value=(terms, False)):
        with patch.object(lookup_module, 'find_file_in_search_path', return_value=None):
            with pytest.raises(AnsibleLookupError, match="No file was found when using first_found."):
                lookup_module.run(terms, variables, **kwargs)
