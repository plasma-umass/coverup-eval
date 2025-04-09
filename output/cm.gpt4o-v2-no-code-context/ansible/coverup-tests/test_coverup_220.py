# file: lib/ansible/cli/doc.py:800-811
# asked: {"lines": [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811], "branches": [[802, 803], [802, 804], [808, 809], [808, 811]]}
# gained: {"lines": [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811], "branches": [[802, 803], [802, 804], [808, 809], [808, 811]]}

import os
import pytest
from ansible.cli.doc import DocCLI

def test_namespace_from_plugin_filepath_with_slash(monkeypatch):
    filepath = "/some/base/dir/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/some/base/dir/"

    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result is None

def test_namespace_from_plugin_filepath_without_slash(monkeypatch):
    filepath = "/some/base/dir/subdir/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/some/base/dir"

    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == "subdir"

def test_namespace_from_plugin_filepath_nested(monkeypatch):
    filepath = "/some/base/dir/subdir/nested/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/some/base/dir/"

    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == "subdir.nested"

def test_namespace_from_plugin_filepath_no_namespace(monkeypatch):
    filepath = "/some/base/dir/plugin_name.py"
    plugin_name = "plugin_name"
    basedir = "/some/base/dir"

    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result is None
