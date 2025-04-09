# file: lib/ansible/module_utils/common/sys_info.py:17-38
# asked: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}
# gained: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution

@pytest.mark.parametrize("platform_system, distro_id, expected", [
    ('Linux', 'amzn', 'Amazon'),
    ('Linux', 'rhel', 'Redhat'),
    ('Linux', '', 'OtherLinux'),
    ('Linux', 'ubuntu', 'Ubuntu'),
    ('Windows', 'amzn', 'Amzn'),
    ('Darwin', 'rhel', 'Rhel'),
])
def test_get_distribution(platform_system, distro_id, expected):
    with patch('platform.system', return_value=platform_system):
        with patch('distro.id', return_value=distro_id):
            assert get_distribution() == expected
