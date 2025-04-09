# file: lib/ansible/module_utils/common/sys_info.py:17-38
# asked: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}
# gained: {"lines": [17, 28, 30, 31, 32, 33, 34, 35, 36, 38], "branches": [[30, 31], [30, 38], [31, 32], [31, 33], [33, 34], [33, 35], [35, 36], [35, 38]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.common.sys_info import get_distribution

@pytest.mark.parametrize("distro_id, platform_system, expected", [
    ("amzn", "Linux", "Amazon"),
    ("rhel", "Linux", "Redhat"),
    ("", "Linux", "OtherLinux"),
    ("ubuntu", "Linux", "Ubuntu"),
    ("windows", "Windows", "Windows"),
])
def test_get_distribution(monkeypatch, distro_id, platform_system, expected):
    def mock_distro_id():
        return distro_id

    def mock_platform_system():
        return platform_system

    monkeypatch.setattr("distro.id", mock_distro_id)
    monkeypatch.setattr("platform.system", mock_platform_system)

    assert get_distribution() == expected
