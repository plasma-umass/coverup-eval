# file: lib/ansible/module_utils/common/sys_info.py:41-79
# asked: {"lines": [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79], "branches": [[60, 61], [60, 77], [61, 62], [61, 79], [67, 68], [67, 73], [73, 74], [73, 79]]}
# gained: {"lines": [41, 50, 52, 57, 58, 60, 61, 62, 67, 68, 73, 74, 77, 79], "branches": [[60, 61], [60, 77], [61, 62], [61, 79], [67, 68], [67, 73], [73, 74], [73, 79]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution_version

@pytest.mark.parametrize("distro_id, version, version_best, expected", [
    ("centos", "7.9", "7.9.2009", "7.9"),
    ("debian", "10", "10.7", "10.7"),
    ("ubuntu", "20.04", None, "20.04"),
    ("centos", None, None, ""),
])
def test_get_distribution_version(distro_id, version, version_best, expected):
    with patch("ansible.module_utils.distro.id", return_value=distro_id), \
         patch("ansible.module_utils.distro.version", side_effect=[version, version_best]):
        assert get_distribution_version() == expected
