# file lib/ansible/cli/doc.py:800-811
# lines [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811]
# branches ['802->803', '802->804', '808->809', '808->811']

import os
import pytest
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_os_path(monkeypatch):
    class MockPath:
        @staticmethod
        def splitext(path):
            return path, '.yml'

    monkeypatch.setattr(os.path, "splitext", MockPath.splitext)

def test_namespace_from_plugin_filepath(mock_os_path, tmp_path):
    basedir = str(tmp_path)
    plugin_name = "test_plugin"
    filepath = os.path.join(basedir, "namespace", "sub_namespace", "_{}_example.yml".format(plugin_name))
    expected_namespace = "namespace.sub_namespace"

    # Create the directory structure and file to simulate the plugin filepath
    os.makedirs(os.path.dirname(filepath))
    with open(filepath, 'w') as f:
        f.write("# test plugin file")

    # Test the namespace_from_plugin_filepath method
    namespace = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert namespace == expected_namespace

    # Cleanup the created file and directories
    os.remove(filepath)
    os.removedirs(os.path.dirname(filepath))
