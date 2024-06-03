# file lib/ansible/executor/powershell/module_manifest.py:254-261
# lines [255, 256, 257, 258, 259, 260, 261]
# branches ['255->256', '255->258']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp

def test_slurp_file_not_exists(mocker):
    # Mock os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)
    
    with pytest.raises(AnsibleError, match="imported module support code does not exist at"):
        _slurp('non_existent_file')

def test_slurp_file_exists(mocker):
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock the open function to simulate file reading
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=b'test data'))
    
    result = _slurp('existent_file')
    
    # Assert that the file was read correctly
    assert result == b'test data'
    
    # Ensure the file was opened in 'rb' mode
    mock_open.assert_called_once_with('existent_file', 'rb')
    
    # Ensure the file was closed
    mock_open().close.assert_called_once()
