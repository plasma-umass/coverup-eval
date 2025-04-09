# file lib/ansible/cli/doc.py:834-845
# lines [834, 835, 837, 839, 840, 842, 845]
# branches ['837->839', '837->845', '839->840', '839->842']

import pytest
from ansible.cli.doc import DocCLI
from ansible.plugins.loader import action_loader

# Mock the action_loader to control the presence of a plugin
@pytest.fixture
def mock_action_loader(mocker):
    mock_loader = mocker.MagicMock()
    mocker.patch('ansible.cli.doc.action_loader', mock_loader)
    return mock_loader

# Test function to cover both branches of the if condition
def test_combine_plugin_doc(mock_action_loader):
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {'description': 'Test plugin description'}
    plainexamples = 'Examples for test plugin'
    returndocs = 'Return data for test plugin'
    metadata = {'version': '1.0.0'}

    # Case when the plugin is present in the action_loader
    mock_action_loader.__contains__.return_value = True
    combined_doc = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    assert combined_doc['doc']['has_action'] is True

    # Case when the plugin is not present in the action_loader
    mock_action_loader.__contains__.return_value = False
    combined_doc = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    assert combined_doc['doc']['has_action'] is False

    # Assert that the rest of the dictionary is correctly formed
    assert combined_doc['doc'] == doc
    assert combined_doc['examples'] == plainexamples
    assert combined_doc['return'] == returndocs
    assert combined_doc['metadata'] == metadata
