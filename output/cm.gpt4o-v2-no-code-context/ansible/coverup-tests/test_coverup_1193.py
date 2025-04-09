# file: lib/ansible/modules/apt_repository.py:413-415
# asked: {"lines": [414, 415], "branches": []}
# gained: {"lines": [414, 415], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list():
    module_mock = MagicMock()
    with patch('ansible.modules.apt_repository.apt_pkg') as apt_pkg_mock:
        apt_pkg_mock.config.find_file.return_value = '/dev/null'
        return SourcesList(module=module_mock)

def test_remove_source_executes_all_lines(sources_list):
    line = "deb http://example.com/ stable main"
    
    with patch.object(sources_list, '_parse', return_value=(None, None, 'parsed_source')) as mock_parse, \
         patch.object(sources_list, '_remove_valid_source') as mock_remove_valid_source:
        
        sources_list.remove_source(line)
        
        mock_parse.assert_called_once_with(line, raise_if_invalid_or_disabled=True)
        mock_remove_valid_source.assert_called_once_with('parsed_source')
