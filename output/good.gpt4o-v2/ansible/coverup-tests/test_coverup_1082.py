# file: lib/ansible/parsing/dataloader.py:286-343
# asked: {"lines": [298, 299, 301, 302, 303, 304, 305, 307, 308, 309, 311, 312, 313, 314, 315, 318, 319, 320, 323, 324, 325, 329, 330, 331, 333, 334, 335, 336, 337, 338, 340, 341, 343], "branches": [[303, 304], [303, 305], [305, 307], [305, 311], [308, 309], [308, 340], [312, 313], [312, 329], [318, 319], [318, 323], [323, 324], [323, 325], [329, 330], [329, 331], [334, 335], [334, 340], [336, 334], [336, 337], [340, 341], [340, 343]]}
# gained: {"lines": [298, 299, 301, 302, 303, 304, 305, 307, 308, 309, 311, 312, 313, 314, 315, 318, 323, 324, 325, 329, 330, 331, 333, 334, 335, 336, 337, 338, 340, 341, 343], "branches": [[303, 304], [303, 305], [305, 307], [305, 311], [308, 309], [308, 340], [312, 313], [312, 329], [318, 323], [323, 324], [329, 330], [334, 335], [334, 340], [336, 334], [336, 337], [340, 341], [340, 343]]}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound
from ansible.module_utils._text import to_bytes
from unittest.mock import patch, MagicMock

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_dwim_relative_stack_null_source(dataloader, mocker):
    mocker.patch('ansible.parsing.dataloader.display.warning')
    with pytest.raises(AnsibleFileNotFound):
        dataloader.path_dwim_relative_stack([], 'dirname', None)

def test_path_dwim_relative_stack_absolute_path_exists(dataloader, mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('ansible.parsing.dataloader.unfrackpath', return_value='/absolute/path')
    result = dataloader.path_dwim_relative_stack([], 'dirname', '/absolute/path')
    assert result == '/absolute/path'

def test_path_dwim_relative_stack_absolute_path_not_exists(dataloader, mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('ansible.parsing.dataloader.unfrackpath', return_value='/absolute/path')
    with pytest.raises(AnsibleFileNotFound):
        dataloader.path_dwim_relative_stack([], 'dirname', '/absolute/path')

def test_path_dwim_relative_stack_relative_path(dataloader, mocker):
    mocker.patch('os.path.exists', side_effect=[False, True])
    mocker.patch('ansible.parsing.dataloader.unfrackpath', side_effect=lambda x, follow: x)
    mocker.patch('ansible.parsing.dataloader.DataLoader.get_basedir', return_value='/base/dir')
    mocker.patch('ansible.parsing.dataloader.DataLoader._is_role', return_value=False)
    result = dataloader.path_dwim_relative_stack(['/some/path'], 'dirname', 'source')
    assert result == '/some/path/source'

def test_path_dwim_relative_stack_not_found(dataloader, mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('ansible.parsing.dataloader.unfrackpath', side_effect=lambda x, follow: x)
    mocker.patch('ansible.parsing.dataloader.DataLoader.get_basedir', return_value='/base/dir')
    mocker.patch('ansible.parsing.dataloader.DataLoader._is_role', return_value=False)
    with pytest.raises(AnsibleFileNotFound):
        dataloader.path_dwim_relative_stack(['/some/path'], 'dirname', 'source')
