# file lib/ansible/cli/doc.py:800-811
# lines [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 811]
# branches ['802->803', '802->804', '808->809', '808->811']

import os
import pytest
from ansible.cli.doc import DocCLI

def test_namespace_from_plugin_filepath(mocker):
    # Mocking the inputs
    filepath = '/some/base/dir/plugins/module_name.py'
    plugin_name = 'module_name'
    basedir = '/some/base/dir/'

    # Call the method
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)

    # Assert the expected result
    assert result == 'plugins'

    # Test with basedir not ending with '/'
    basedir = '/some/base/dir'
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result == 'plugins'

    # Test with no namespace
    filepath = '/some/base/dir/module_name.py'
    result = DocCLI.namespace_from_plugin_filepath(filepath, plugin_name, basedir)
    assert result is None
