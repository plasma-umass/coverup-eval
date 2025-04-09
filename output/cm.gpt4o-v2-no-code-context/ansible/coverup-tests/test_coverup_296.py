# file: lib/ansible/cli/doc.py:867-888
# asked: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}
# gained: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}

import pytest
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError
from ansible.utils.display import Display
import traceback

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.utils.display.Display.vvv')

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

def test_format_plugin_doc_exception(mock_get_man_text, mock_display):
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {'collection': 'test_collection'}
    plainexamples = 'example'
    returndocs = 'return docs'
    metadata = 'metadata'

    mock_get_man_text.side_effect = Exception('test exception')

    with pytest.raises(AnsibleError) as excinfo:
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert "Unable to retrieve documentation from 'test_plugin' due to: test exception" in str(excinfo.value)
    assert mock_display.called
