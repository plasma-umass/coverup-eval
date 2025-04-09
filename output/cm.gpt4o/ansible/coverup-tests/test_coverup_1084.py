# file lib/ansible/cli/doc.py:772-798
# lines [775, 776, 777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 789, 791, 793, 794, 795, 796, 797]
# branches ['777->778', '777->779', '789->791', '789->793']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError

@pytest.fixture
def mock_plugin_loader(mocker):
    return mocker.patch('ansible.cli.doc.plugin_loader')

@pytest.fixture
def mock_get_docstring(mocker):
    return mocker.patch('ansible.cli.doc.get_docstring')

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.doc.display')

@pytest.fixture
def mock_context(mocker):
    return mocker.patch('ansible.cli.doc.context')

def test_get_plugin_metadata_success(mock_plugin_loader, mock_get_docstring, mock_context):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_package_path'
    mock_plugin_loader.some_loader = mock_loader

    mock_context.CLIARGS = {'verbosity': 0}
    mock_get_docstring.return_value = ({'short_description': 'desc', 'version_added': '1.0'}, None, None, None)

    result = DocCLI.get_plugin_metadata('some', 'plugin')

    assert result == {
        'name': 'plugin',
        'namespace': DocCLI.namespace_from_plugin_filepath('some_path', 'plugin', 'some_package_path'),
        'description': 'desc',
        'version_added': '1.0'
    }

def test_get_plugin_metadata_not_resolved(mock_plugin_loader):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = False
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_plugin_loader.some_loader = mock_loader

    with pytest.raises(AnsibleError, match="unable to load some plugin named plugin"):
        DocCLI.get_plugin_metadata('some', 'plugin')

def test_get_plugin_metadata_docstring_error(mock_plugin_loader, mock_get_docstring, mock_display, mock_context):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_package_path'
    mock_plugin_loader.some_loader = mock_loader

    mock_context.CLIARGS = {'verbosity': 0}
    mock_get_docstring.side_effect = Exception('docstring error')

    with pytest.raises(AnsibleError, match="some plugin at some_path has a documentation formatting error or is missing documentation."):
        DocCLI.get_plugin_metadata('some', 'plugin')

def test_get_plugin_metadata_no_doc(mock_plugin_loader, mock_get_docstring, mock_context):
    mock_loader = MagicMock()
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = 'some_path'
    mock_result.plugin_resolved_collection = 'some_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    mock_loader.package_path = 'some_package_path'
    mock_plugin_loader.some_loader = mock_loader

    mock_context.CLIARGS = {'verbosity': 0}
    mock_get_docstring.return_value = (None, None, None, None)

    result = DocCLI.get_plugin_metadata('some', 'plugin')

    assert result is None
