# file lib/ansible/cli/doc.py:847-865
# lines [856, 858, 859, 861, 862, 864, 865]
# branches ['850->856', '858->859', '858->861', '861->862', '861->864']

import pytest
from ansible.cli.doc import DocCLI

def _do_lookup_snippet(doc):
    return ['lookup_snippet']

def _do_yaml_snippet(doc):
    return ['yaml_snippet']

@pytest.fixture
def mock_do_lookup_snippet(mocker):
    return mocker.patch('ansible.cli.doc._do_lookup_snippet', side_effect=_do_lookup_snippet)

@pytest.fixture
def mock_do_yaml_snippet(mocker):
    return mocker.patch('ansible.cli.doc._do_yaml_snippet', side_effect=_do_yaml_snippet)

def test_format_snippet_for_lookup_plugin(mock_do_lookup_snippet):
    plugin = 'my_lookup_plugin'
    plugin_type = 'lookup'
    doc = {}
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    assert result == 'lookup_snippet\n'
    mock_do_lookup_snippet.assert_called_once_with(doc)

def test_format_snippet_for_yaml_options(mock_do_yaml_snippet):
    plugin = 'my_yaml_plugin'
    plugin_type = 'module'
    doc = {'options': {}}
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    assert result == 'yaml_snippet\n'
    mock_do_yaml_snippet.assert_called_once_with(doc)
