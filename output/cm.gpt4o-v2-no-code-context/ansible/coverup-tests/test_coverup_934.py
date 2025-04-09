# file: lib/ansible/plugins/lookup/file.py:60-87
# asked: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}
# gained: {"lines": [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87], "branches": [[67, 68], [67, 87], [74, 75], [74, 83], [77, 78], [77, 79], [79, 80], [79, 81]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup.file import LookupModule
from ansible.utils.display import Display

@pytest.fixture
def lookup_module():
    return LookupModule()

@pytest.fixture
def mock_loader(lookup_module):
    with patch.object(lookup_module, '_loader', autospec=True) as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_display():
    with patch('ansible.plugins.lookup.file.display', autospec=True) as mock_display:
        yield mock_display

def test_run_success(lookup_module, mock_loader, mock_display):
    terms = ['testfile']
    variables = {}
    kwargs = {}

    mock_loader._get_file_contents.return_value = (b'file contents', None)
    lookup_module.set_options = MagicMock()
    lookup_module.find_file_in_search_path = MagicMock(return_value='path/to/testfile')
    lookup_module.get_option = MagicMock(side_effect=lambda option: False)

    result = lookup_module.run(terms, variables, **kwargs)

    assert result == ['file contents']
    mock_display.debug.assert_called_with("File lookup term: testfile")
    mock_display.vvvv.assert_called_with(u"File lookup using path/to/testfile as file")

def test_run_file_not_found(lookup_module, mock_loader, mock_display):
    terms = ['nonexistentfile']
    variables = {}
    kwargs = {}

    lookup_module.set_options = MagicMock()
    lookup_module.find_file_in_search_path = MagicMock(return_value=None)

    with pytest.raises(AnsibleError, match="could not locate file in lookup: nonexistentfile"):
        lookup_module.run(terms, variables, **kwargs)

    mock_display.debug.assert_called_with("File lookup term: nonexistentfile")

def test_run_with_lstrip_rstrip(lookup_module, mock_loader, mock_display):
    terms = ['testfile']
    variables = {}
    kwargs = {}

    mock_loader._get_file_contents.return_value = (b'  file contents  ', None)
    lookup_module.set_options = MagicMock()
    lookup_module.find_file_in_search_path = MagicMock(return_value='path/to/testfile')
    lookup_module.get_option = MagicMock(side_effect=lambda option: option in ['lstrip', 'rstrip'])

    result = lookup_module.run(terms, variables, **kwargs)

    assert result == ['file contents']
    mock_display.debug.assert_called_with("File lookup term: testfile")
    mock_display.vvvv.assert_called_with(u"File lookup using path/to/testfile as file")
