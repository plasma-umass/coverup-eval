# file lib/ansible/modules/apt_repository.py:366-369
# lines [366, 367, 368, 369]
# branches ['367->368', '367->369']

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.apt_repository import SourcesList

# Test function to cover the _choice method in SourcesList class
@patch('ansible.modules.apt_repository.apt_pkg', create=True)
def test_sources_list_choice(mock_apt_pkg):
    # Mocking the apt_pkg.config.find_file method to avoid AttributeError
    mock_apt_pkg.config.find_file.return_value = '/etc/apt/sources.list'
    mock_apt_pkg.Config.FindFile.return_value = '/etc/apt/sources.list'

    mock_module = MagicMock()
    sources_list = SourcesList(mock_module)

    # Test when new is None, should return old
    old_value = "old_value"
    assert sources_list._choice(None, old_value) == old_value

    # Test when new is not None, should return new
    new_value = "new_value"
    assert sources_list._choice(new_value, old_value) == new_value

    # Clean up is not necessary as no external state is modified
