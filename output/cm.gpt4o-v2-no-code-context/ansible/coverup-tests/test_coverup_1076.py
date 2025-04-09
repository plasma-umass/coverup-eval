# file: lib/ansible/cli/doc.py:847-865
# asked: {"lines": [], "branches": [[861, 864]]}
# gained: {"lines": [], "branches": [[861, 864]]}

import pytest
from ansible.cli.doc import DocCLI

def _do_yaml_snippet(doc):
    return ["# YAML snippet for {}".format(doc.get('name', 'unknown'))]

def _do_lookup_snippet(doc):
    return ["# Lookup snippet for {}".format(doc.get('name', 'unknown'))]

@pytest.fixture
def mock_do_yaml_snippet(monkeypatch):
    monkeypatch.setattr('ansible.cli.doc._do_yaml_snippet', _do_yaml_snippet)

@pytest.fixture
def mock_do_lookup_snippet(monkeypatch):
    monkeypatch.setattr('ansible.cli.doc._do_lookup_snippet', _do_lookup_snippet)

def test_format_snippet_inventory_plugin():
    with pytest.raises(ValueError) as excinfo:
        DocCLI.format_snippet('test_plugin', 'inventory', {'options': {'plugin': True}})
    assert 'The test_plugin inventory plugin does not take YAML type config source' in str(excinfo.value)

def test_format_snippet_lookup_plugin(mock_do_lookup_snippet):
    result = DocCLI.format_snippet('test_plugin', 'lookup', {'name': 'test_lookup'})
    assert result == "# Lookup snippet for test_lookup\n"

def test_format_snippet_with_options(mock_do_yaml_snippet):
    result = DocCLI.format_snippet('test_plugin', 'other', {'options': {'some_option': 'value'}, 'name': 'test_yaml'})
    assert result == "# YAML snippet for test_yaml\n"

def test_format_snippet_no_options():
    result = DocCLI.format_snippet('test_plugin', 'other', {'name': 'test_no_options'})
    assert result == ""
