# file lib/ansible/module_utils/facts/system/distribution.py:47-95
# lines [47, 48, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 90, 91, 94]
# branches []

import pytest
from unittest.mock import mock_open, patch

# Assuming the DistributionFiles class is imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_filesystem():
    files = {
        '/etc/altlinux-release': 'ALT Linux',
        '/etc/oracle-release': 'Oracle Linux Server release 7.9',
        '/etc/slackware-version': 'Slackware 14.2',
        '/etc/centos-release': 'CentOS Linux release 7.9.2009 (Core)',
        '/etc/redhat-release': 'Red Hat Enterprise Linux Server release 7.9 (Maipo)',
        '/etc/vmware-release': '',
        '/etc/openwrt_release': 'DISTRIB_ID="OpenWrt"',
        '/etc/os-release': 'NAME="Amazon Linux"',
        '/etc/system-release': 'Amazon Linux release 2 (Karoo)',
        '/etc/alpine-release': '3.12.1',
        '/etc/arch-release': '',
        '/etc/SuSE-release': 'SUSE Linux Enterprise Server 12 SP5',
        '/etc/gentoo-release': 'Gentoo Base System release 2.7',
        '/etc/lsb-release': 'DISTRIB_ID=Ubuntu\nDISTRIB_RELEASE=20.04\nDISTRIB_CODENAME=focal\nDISTRIB_DESCRIPTION="Ubuntu 20.04.1 LTS"',
        '/etc/sourcemage-release': 'Source Mage GNU/Linux',
        '/usr/lib/os-release': 'NAME="Clear Linux OS"',
        '/etc/coreos/update.conf': 'GROUP=stable',
        '/etc/flatcar/update.conf': 'GROUP=stable',
    }
    return files

@pytest.fixture
def mock_open_files(mock_filesystem):
    def _mock_open(file, *args, **kwargs):
        if file in mock_filesystem:
            return mock_open(read_data=mock_filesystem[file])()
        raise FileNotFoundError(f"No such file or directory: '{file}'")
    return _mock_open

@pytest.mark.parametrize("file_path, expected_name", [
    ('/etc/altlinux-release', 'Altlinux'),
    ('/etc/oracle-release', 'OracleLinux'),
    ('/etc/slackware-version', 'Slackware'),
    ('/etc/centos-release', 'CentOS'),
    ('/etc/redhat-release', 'RedHat'),
    ('/etc/vmware-release', 'VMwareESX'),
    ('/etc/openwrt_release', 'OpenWrt'),
    ('/etc/os-release', 'Amazon'),
    ('/etc/system-release', 'Amazon'),
    ('/etc/alpine-release', 'Alpine'),
    ('/etc/arch-release', 'Archlinux'),
    ('/etc/SuSE-release', 'SUSE'),
    ('/etc/gentoo-release', 'Gentoo'),
    ('/etc/lsb-release', 'Debian'),
    ('/etc/sourcemage-release', 'SMGL'),
    ('/usr/lib/os-release', 'ClearLinux'),
    ('/etc/coreos/update.conf', 'Coreos'),
    ('/etc/flatcar/update.conf', 'Flatcar'),
])
def test_distribution_files(mock_open_files, file_path, expected_name):
    with patch('builtins.open', mock_open_files):
        dist_files = DistributionFiles(module=None)  # Pass a dummy value for the required 'module' argument
        for dist in dist_files.OSDIST_LIST:
            if dist['path'] == file_path:
                assert dist['name'] == expected_name
                break
        else:
            pytest.fail(f"File path {file_path} not found in OSDIST_LIST")
