# file lib/ansible/parsing/dataloader.py:231-284
# lines [240, 241, 244, 245, 248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 264, 266, 269, 272, 275, 278, 280, 281, 282, 284]
# branches ['244->245', '244->248', '252->253', '252->255', '255->256', '255->258', '264->266', '264->269', '280->281', '280->284', '281->280', '281->282']

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_dwim_relative(dataloader, mocker):
    mocker.patch('ansible.parsing.dataloader.to_text', side_effect=lambda x, errors='surrogate_or_strict': x)
    mocker.patch('ansible.parsing.dataloader.unfrackpath', side_effect=lambda x, follow=False: x)
    mocker.patch('ansible.parsing.dataloader.to_bytes', side_effect=lambda x, errors='surrogate_or_strict': x)
    mocker.patch('os.path.exists', return_value=True)
    
    mocker.patch.object(dataloader, '_is_role', return_value=True)
    mocker.patch.object(dataloader, 'set_basedir')
    mocker.patch.object(dataloader, 'path_dwim', side_effect=lambda x: x)
    
    path = '/some/path'
    dirname = 'templates'
    source = 'file.yml'
    
    result = dataloader.path_dwim_relative(path, dirname, source, is_role=False)
    
    assert result == os.path.join(path, dirname, source)
    dataloader.set_basedir.assert_called()
    dataloader.path_dwim.assert_called()
