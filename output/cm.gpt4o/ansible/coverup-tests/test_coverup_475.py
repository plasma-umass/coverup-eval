# file lib/ansible/parsing/dataloader.py:181-195
# lines [181, 186, 187, 189, 190, 192, 193, 195]
# branches ['189->190', '189->192']

import os
import pytest
from unittest.mock import patch
from urllib.parse import unquote

# Assuming the necessary imports for to_text and unfrackpath
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text
from ansible.utils.path import unfrackpath

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._basedir = '/mock/basedir'
    return loader

def test_path_dwim_absolute_path(dataloader):
    given = '/absolute/path'
    expected = '/absolute/path'
    
    with patch('ansible.parsing.dataloader.unquote', side_effect=unquote), \
         patch('ansible.module_utils._text.to_text', side_effect=to_text), \
         patch('ansible.utils.path.unfrackpath', side_effect=unfrackpath):
        result = dataloader.path_dwim(given)
        assert result == expected

def test_path_dwim_home_path(dataloader):
    given = '~/home/path'
    expected = os.path.expanduser('~/home/path')
    
    with patch('ansible.parsing.dataloader.unquote', side_effect=unquote), \
         patch('ansible.module_utils._text.to_text', side_effect=to_text), \
         patch('ansible.utils.path.unfrackpath', side_effect=unfrackpath):
        result = dataloader.path_dwim(given)
        assert result == expected

def test_path_dwim_relative_path(dataloader):
    given = 'relative/path'
    expected = '/mock/basedir/relative/path'
    
    with patch('ansible.parsing.dataloader.unquote', side_effect=unquote), \
         patch('ansible.module_utils._text.to_text', side_effect=to_text), \
         patch('ansible.utils.path.unfrackpath', side_effect=unfrackpath):
        result = dataloader.path_dwim(given)
        assert result == expected
