# file: lib/ansible/module_utils/common/sys_info.py:82-109
# asked: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}
# gained: {"lines": [82, 89, 90, 94, 95, 97, 98, 100, 101, 102, 104, 105, 106, 107, 109], "branches": [[90, 94], [90, 109], [97, 98], [97, 100], [100, 101], [100, 104], [104, 105], [104, 109], [106, 107], [106, 109]]}

import pytest
import platform
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.sys_info import get_distribution_codename

@pytest.mark.parametrize("system, os_release_info, lsb_release_info, distro_id, distro_codename, expected", [
    ('Linux', {'version_codename': 'focal'}, {}, 'ubuntu', '', 'focal'),
    ('Linux', {'version_codename': None, 'ubuntu_codename': 'bionic'}, {}, 'ubuntu', '', 'bionic'),
    ('Linux', {'version_codename': None, 'ubuntu_codename': None}, {'codename': 'xenial'}, 'ubuntu', '', 'xenial'),
    ('Linux', {'version_codename': None, 'ubuntu_codename': None}, {}, 'ubuntu', 'trusty', 'trusty'),
    ('Linux', {'version_codename': None, 'ubuntu_codename': None}, {}, 'fedora', '', None),
    ('Windows', {}, {}, '', '', None),
])
def test_get_distribution_codename(system, os_release_info, lsb_release_info, distro_id, distro_codename, expected):
    with patch('platform.system', return_value=system):
        with patch('ansible.module_utils.distro.os_release_info', return_value=os_release_info):
            with patch('ansible.module_utils.distro.lsb_release_info', return_value=lsb_release_info):
                with patch('ansible.module_utils.distro.id', return_value=distro_id):
                    with patch('ansible.module_utils.distro.codename', return_value=distro_codename):
                        assert get_distribution_codename() == expected
