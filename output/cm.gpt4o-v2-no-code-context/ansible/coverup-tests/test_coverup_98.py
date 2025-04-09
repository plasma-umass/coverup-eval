# file: lib/ansible/cli/doc.py:772-798
# asked: {"lines": [772, 773, 775, 776, 777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 789, 791, 793, 794, 795, 796, 797], "branches": [[777, 778], [777, 779], [789, 791], [789, 793]]}
# gained: {"lines": [772, 773, 775, 776, 777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 789, 791, 793, 794, 795, 796, 797], "branches": [[777, 778], [777, 779], [789, 791], [789, 793]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_plugin_loader():
    with patch('ansible.cli.doc.plugin_loader') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_fragment_loader():
    with patch('ansible.cli.doc.fragment_loader') as mock_loader:
        yield mock_loader

@pytest.fixture
def mock_context():
    with patch('ansible.cli.doc.context') as mock_context:
        mock_context.CLIARGS = {'verbosity': 0}
        yield mock_context

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display') as mock_display:
        yield mock_display

@pytest.fixture
def mock_traceback():
    with patch('ansible.cli.doc.traceback') as mock_traceback:
        yield mock_traceback

@pytest.fixture
def mock_get_docstring():
    with patch('ansible.cli.doc.get_docstring') as mock_get_docstring:
        yield mock_get_docstring

def test_get_plugin_metadata_success(mock_plugin_loader, mock_fragment_loader, mock_context, mock_get_docstring):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_base_path/'
    mock_plugin_loader.module_loader = mock_loader

    mock_get_docstring.return_value = ({'short_description': 'desc', 'version_added': '2.0'}, None, None, None)

    result = DocCLI.get_plugin_metadata('module', 'test_plugin')

    assert result == {
        'name': 'test_plugin',
        'namespace': DocCLI.namespace_from_plugin_filepath('some_path', 'test_plugin', 'some_base_path/'),
        'description': 'desc',
        'version_added': '2.0'
    }

def test_get_plugin_metadata_not_resolved(mock_plugin_loader):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = False
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_plugin_loader.module_loader = mock_loader

    with pytest.raises(AnsibleError, match="unable to load module plugin named test_plugin"):
        DocCLI.get_plugin_metadata('module', 'test_plugin')

def test_get_plugin_metadata_docstring_exception(mock_plugin_loader, mock_fragment_loader, mock_context, mock_display, mock_traceback, mock_get_docstring):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_base_path/'
    mock_plugin_loader.module_loader = mock_loader

    mock_get_docstring.side_effect = Exception("docstring error")

    with pytest.raises(AnsibleError, match="module test_plugin at some_path has a documentation formatting error or is missing documentation."):
        DocCLI.get_plugin_metadata('module', 'test_plugin')

    mock_display.vvv.assert_called_once()
    mock_traceback.format_exc.assert_called_once()

def test_get_plugin_metadata_no_doc(mock_plugin_loader, mock_fragment_loader, mock_context, mock_get_docstring):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_base_path/'
    mock_plugin_loader.module_loader = mock_loader

    mock_get_docstring.return_value = (None, None, None, None)

    result = DocCLI.get_plugin_metadata('module', 'test_plugin')

    assert result is None
