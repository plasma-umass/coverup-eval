# file lib/ansible/cli/doc.py:800-811
# lines [809]
# branches ['802->804', '808->809']

import os
import pytest
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_filepath(tmp_path):
    basedir = tmp_path / "test_plugins"
    basedir.mkdir()
    plugin_file = basedir / "my_plugin.py"
    plugin_file.touch()
    return str(plugin_file), basedir

def test_namespace_from_plugin_filepath_no_namespace(mock_filepath):
    filepath, basedir = mock_filepath
    plugin_name = "my_plugin"
    namespace = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, str(basedir))
    assert namespace is None

def test_namespace_from_plugin_filepath_with_namespace(mock_filepath):
    filepath, basedir = mock_filepath
    plugin_name = "my_plugin"
    subdir = basedir / "subdir"
    subdir.mkdir()
    namespaced_plugin = subdir / "my_plugin.py"
    namespaced_plugin.touch()
    namespace = DocCLI.namespace_from_plugin_filepath(str(namespaced_plugin), plugin_name, str(basedir))
    assert namespace == 'subdir'
