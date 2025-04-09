# file: lib/ansible/cli/doc.py:800-811
# asked: {"lines": [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811], "branches": [[802, 803], [802, 804], [808, 809], [808, 811]]}
# gained: {"lines": [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811], "branches": [[802, 803], [802, 804], [808, 809], [808, 811]]}

import pytest
from ansible.cli.doc import DocCLI

def test_namespace_from_plugin_filepath_with_slash():
    filepath = "/path/to/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/path/to/"
    expected = None
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == expected

def test_namespace_from_plugin_filepath_without_slash():
    filepath = "/path/to/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/path/to"
    expected = None
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == expected

def test_namespace_from_plugin_filepath_with_namespace():
    filepath = "/path/to/ns/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/path/to/"
    expected = "ns"
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == expected

def test_namespace_from_plugin_filepath_with_nested_namespace():
    filepath = "/path/to/ns/subns/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/path/to/"
    expected = "ns.subns"
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == expected
