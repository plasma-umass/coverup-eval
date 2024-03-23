# file lib/ansible/plugins/loader.py:307-314
# lines [307, 308, 309, 310, 311, 312, 313, 314]
# branches ['310->311', '310->314', '311->310', '311->312', '312->310', '312->313']

import os
import pytest
from ansible.plugins.loader import PluginLoader

# Test function to cover the missing lines/branches in PluginLoader._all_directories
def test_plugin_loader_all_directories(tmp_path):
    # Create a temporary directory structure
    base_dir = tmp_path / "base"
    base_dir.mkdir()
    sub_dir = base_dir / "sub"
    sub_dir.mkdir()
    init_file = base_dir / "__init__.py"
    init_file.touch()

    # Instantiate PluginLoader with dummy arguments
    loader = PluginLoader(class_name='dummy_class', package='dummy_package', config={}, subdir='')

    # Call _all_directories with the base directory
    directories = loader._all_directories(str(base_dir))

    # Assertions to verify the postconditions
    assert str(base_dir) in directories
    assert str(sub_dir) in directories
    assert len(directories) == 2

    # Cleanup is handled by pytest's tmp_path fixture automatically
