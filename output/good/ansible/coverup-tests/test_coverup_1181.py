# file lib/ansible/cli/doc.py:772-798
# lines [775, 776, 777, 778, 779, 780, 782, 783, 784, 785, 786, 787, 789, 791, 793, 794, 795, 796, 797]
# branches ['777->778', '777->779', '789->791', '789->793']

import pytest
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display
from ansible.utils.plugin_docs import get_docstring
from unittest.mock import MagicMock

# Mock the necessary components to isolate the test environment
@pytest.fixture
def mock_loader(mocker):
    mock_loader = mocker.MagicMock()
    mocker.patch('ansible.cli.doc.plugin_loader', mock_loader)
    return mock_loader

@pytest.fixture
def mock_get_docstring(mocker):
    return mocker.patch('ansible.cli.doc.get_docstring', return_value=(None, None, None, None))

@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch('ansible.cli.doc.display', display)
    return display

@pytest.fixture
def mock_context_CLIARGS(mocker):
    cliargs = {'verbosity': 0}
    mocker.patch('ansible.cli.doc.context.CLIARGS', cliargs)
    return cliargs

def test_get_plugin_metadata_exception(mock_loader, mock_get_docstring, mock_display, mock_context_CLIARGS):
    plugin_type = 'module'
    plugin_name = 'test_module'
    mock_loader.module_loader.find_plugin_with_context.return_value = MagicMock(
        resolved=True,
        plugin_resolved_path='/path/to/plugin.py',
        plugin_resolved_collection='test_collection'
    )

    # Simulate an exception when getting the docstring
    mock_get_docstring.side_effect = Exception("Some error")

    with pytest.raises(AnsibleError) as excinfo:
        DocCLI.get_plugin_metadata(plugin_type, plugin_name)

    assert str(excinfo.value) == f"{plugin_type} {plugin_name} at /path/to/plugin.py has a documentation formatting error or is missing documentation."

def test_get_plugin_metadata_no_doc(mock_loader, mock_get_docstring, mock_display, mock_context_CLIARGS):
    plugin_type = 'module'
    plugin_name = 'test_module'
    mock_loader.module_loader.find_plugin_with_context.return_value = MagicMock(
        resolved=True,
        plugin_resolved_path='/path/to/plugin.py',
        plugin_resolved_collection='test_collection'
    )

    # Simulate a None docstring (plugin removed or no documentation)
    mock_get_docstring.return_value = (None, None, None, None)

    result = DocCLI.get_plugin_metadata(plugin_type, plugin_name)
    assert result is None

def test_get_plugin_metadata_success(mock_loader, mock_get_docstring, mock_display, mock_context_CLIARGS):
    plugin_type = 'module'
    plugin_name = 'test_module'
    package_path = '/path/to/'
    mock_loader.module_loader.find_plugin_with_context.return_value = MagicMock(
        resolved=True,
        plugin_resolved_path='/path/to/plugin.py',
        plugin_resolved_collection='test_collection'
    )
    mock_loader.module_loader.package_path = package_path

    # Simulate a successful docstring retrieval
    doc = {
        'short_description': 'Test module',
        'version_added': '1.0.0'
    }
    mock_get_docstring.return_value = (doc, None, None, None)

    result = DocCLI.get_plugin_metadata(plugin_type, plugin_name)
    assert result == {
        'name': plugin_name,
        'namespace': DocCLI.namespace_from_plugin_filepath('/path/to/plugin.py', plugin_name, package_path),
        'description': 'Test module',
        'version_added': '1.0.0'
    }
