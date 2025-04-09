# file lib/ansible/modules/apt_repository.py:211-216
# lines [211, 213, 214, 215, 216]
# branches ['213->exit', '213->214', '214->213', '214->215', '215->214', '215->216']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the SourcesList class is imported from ansible.modules.apt_repository
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list():
    module_mock = MagicMock()
    with patch('ansible.modules.apt_repository.apt_pkg') as apt_pkg_mock:
        apt_pkg_mock.config.find_file.return_value = '/dev/null'
        sl = SourcesList(module=module_mock)
        sl.files = {
            'file1': [
                (1, True, True, 'deb http://example.com stable main', '# comment'),
                (2, False, True, 'deb http://example.com stable main', '# comment'),
                (3, True, False, 'deb http://example.com stable main', '# comment'),
            ],
            'file2': [
                (1, True, True, 'deb http://example.com stable main', '# comment'),
                (2, True, True, 'deb http://example.com stable main', '# comment'),
            ]
        }
        return sl

def test_sources_list_iterator(sources_list):
    expected = [
        ('file1', 1, True, 'deb http://example.com stable main', '# comment'),
        ('file1', 3, False, 'deb http://example.com stable main', '# comment'),
        ('file2', 1, True, 'deb http://example.com stable main', '# comment'),
        ('file2', 2, True, 'deb http://example.com stable main', '# comment'),
    ]
    result = list(sources_list)
    assert result == expected

# Clean up fixture
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
