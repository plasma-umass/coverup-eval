# file: lib/ansible/modules/apt_repository.py:348-364
# asked: {"lines": [348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364], "branches": [[350, 351], [350, 364], [351, 350], [351, 352], [353, 354], [353, 363], [355, 356], [355, 357], [358, 359], [358, 361]]}
# gained: {"lines": [348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364], "branches": [[350, 351], [350, 364], [351, 350], [351, 352], [353, 354], [353, 363], [355, 356], [355, 357], [358, 359], [358, 361]]}

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def sources_list():
    from ansible.modules.apt_repository import SourcesList
    module = MagicMock()
    with patch('ansible.modules.apt_repository.apt_pkg') as mock_apt_pkg:
        mock_apt_pkg.config.find_file.return_value = '/dev/null'
        sl = SourcesList(module)
        sl.files = {
            'file1.list': [
                (1, True, True, 'deb http://example.com stable main', ''),
                (2, True, False, 'deb http://example.com testing main', 'disabled'),
            ],
            'file2.list': [
                (1, True, True, 'deb http://example.org stable main', 'example'),
            ],
            'empty.list': []
        }
        return sl

def test_dump(sources_list):
    expected_output = {
        'file1.list': 'deb http://example.com stable main\n# deb http://example.com testing main # disabled\n',
        'file2.list': 'deb http://example.org stable main # example\n'
    }
    assert sources_list.dump() == expected_output
