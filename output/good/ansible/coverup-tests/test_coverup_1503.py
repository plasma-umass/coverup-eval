# file lib/ansible/cli/doc.py:867-888
# lines [888]
# branches []

import pytest
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError
from ansible.utils.display import Display

# Mock the display object to capture verbose output
@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.cli.doc.display', new_callable=Display)
    mock_display.vvv = mocker.MagicMock()
    return mock_display

# Test function to cover line 888
def test_format_plugin_doc_returns_text(mock_display, mocker):
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {'collection': 'test_collection', 'doc': 'test_doc'}
    plainexamples = "test_plainexamples"
    returndocs = "test_returndocs"
    metadata = "test_metadata"

    # Mock the get_man_text static method to return a known string
    mocker.patch.object(DocCLI, 'get_man_text', return_value='test_text')

    # Call the method under test
    result = DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    # Assert that the result is the expected text
    assert result == 'test_text'

    # Assert that the verbose output was not triggered
    mock_display.vvv.assert_not_called()

    # Assert that the doc dictionary was updated correctly
    assert doc['plainexamples'] == plainexamples
    assert doc['returndocs'] == returndocs
    assert doc['metadata'] == metadata

# Test function to cover the exception branch
def test_format_plugin_doc_exception(mock_display, mocker):
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {'collection': 'test_collection', 'doc': 'test_doc'}
    plainexamples = "test_plainexamples"
    returndocs = "test_returndocs"
    metadata = "test_metadata"

    # Mock the get_man_text static method to raise an exception
    mocker.patch.object(DocCLI, 'get_man_text', side_effect=Exception('test exception'))

    # Call the method under test and assert that it raises an AnsibleError
    with pytest.raises(AnsibleError) as exc_info:
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    # Assert that the exception message is as expected
    assert "Unable to retrieve documentation from 'test_plugin' due to: test exception" in str(exc_info.value)

    # Assert that the verbose output was triggered
    mock_display.vvv.assert_called_once()
