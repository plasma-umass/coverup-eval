# file lib/ansible/modules/apt_repository.py:371-377
# lines [376, 377]
# branches []

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
            'test_file': [
                (0, True, True, 'deb http://example.com stable main', '# comment'),
                (1, True, False, 'deb-src http://example.com stable main', '# another comment')
            ]
        }
        sl._choice = MagicMock(side_effect=lambda new, old: new if new is not None else old)
        return sl

def test_modify(sources_list):
    # Modify the second entry in 'test_file'
    sources_list.modify('test_file', 1, enabled=True, source='deb http://newexample.com stable main', comment='# new comment')

    # Assertions to verify the changes
    assert sources_list.files['test_file'][1] == (1, True, True, 'deb http://newexample.com stable main', '# new comment')

    # Clean up
    sources_list.files['test_file'][1] = (1, True, False, 'deb-src http://example.com stable main', '# another comment')
