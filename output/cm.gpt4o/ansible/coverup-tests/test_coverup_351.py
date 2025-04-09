# file lib/ansible/cli/doc.py:867-888
# lines [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.doc.display')

@pytest.fixture
def mock_traceback(mocker):
    return mocker.patch('traceback.format_exc')

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.cli.doc.to_native')

@pytest.fixture
def mock_get_man_text(mocker):
    return mocker.patch('ansible.cli.doc.DocCLI.get_man_text')

def test_format_plugin_doc_success(mock_get_man_text):
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {'collection': 'test_collection'}
    plainexamples = 'example'
    returndocs = 'return docs'
    metadata = 'metadata'

    mock_get_man_text.return_value = 'formatted text'

    result = DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert result == 'formatted text'
    assert doc['plainexamples'] == plainexamples
    assert doc['returndocs'] == returndocs
    assert doc['metadata'] == metadata

def test_format_plugin_doc_exception(mock_display, mock_traceback, mock_to_native, mock_get_man_text):
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {'collection': 'test_collection'}
    plainexamples = 'example'
    returndocs = 'return docs'
    metadata = 'metadata'

    mock_get_man_text.side_effect = Exception('test exception')
    mock_traceback.return_value = 'traceback info'
    mock_to_native.return_value = 'native exception'

    with pytest.raises(AnsibleError) as excinfo:
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert 'Unable to retrieve documentation from' in str(excinfo.value)
    assert 'test_plugin' in str(excinfo.value)
    assert 'native exception' in str(excinfo.value)
    mock_display.vvv.assert_called_once_with('traceback info')
