# file lib/ansible/module_utils/facts/system/distribution.py:265-317
# lines [266, 267, 268, 269, 270, 271, 272, 273, 275, 276, 277, 278, 279, 280, 281, 282, 283, 285, 286, 287, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 314, 315, 317]
# branches ['267->268', '267->269', '269->270', '269->291', '270->271', '270->314', '272->273', '272->275', '276->277', '276->279', '279->280', '279->283', '281->270', '281->282', '283->270', '283->285', '286->287', '286->289', '291->292', '291->314', '292->293', '292->300', '296->297', '296->314', '298->296', '298->299', '300->301', '300->314', '303->304', '303->305', '305->306', '305->307', '307->308', '307->314', '309->307', '309->310', '314->315', '314->317']

import os
import pytest
from unittest.mock import MagicMock

# Assuming the DistributionFiles class is imported from the appropriate module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def mock_os_path_islink(mocker):
    return mocker.patch('os.path.islink', return_value=False)

@pytest.fixture
def mock_os_path_realpath(mocker):
    return mocker.patch('os.path.realpath', return_value='')

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.distribution.get_file_content', return_value='openSUSE 13.2 (Harlequin) (x86_64)')

# Mock module parameter required for DistributionFiles class instantiation
@pytest.fixture
def mock_module():
    module_mock = MagicMock()
    return module_mock

def test_parse_distribution_file_SUSE_open_os_release(mock_os_path_islink, mock_os_path_realpath, mock_get_file_content, mock_module):
    distribution_files = DistributionFiles(mock_module)
    name = 'openSUSE'
    data = 'NAME="openSUSE Leap"\nVERSION_ID="15.2"\nPRETTY_NAME="openSUSE Leap 15.2"'
    path = '/etc/os-release'
    collected_facts = {}

    result, suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, path, collected_facts)

    assert result is True
    assert suse_facts['distribution'] == 'openSUSE Leap'
    assert suse_facts['distribution_version'] == '15.2'
    assert suse_facts['distribution_major_version'] == '15'
    assert suse_facts['distribution_release'] == '2'

def test_parse_distribution_file_SUSE_enterprise_os_release(mock_os_path_islink, mock_os_path_realpath, mock_get_file_content, mock_module):
    distribution_files = DistributionFiles(mock_module)
    name = 'SLES'
    data = 'NAME="SLES"\nVERSION_ID="12.3"\nPRETTY_NAME="SUSE Linux Enterprise Server 12 SP3"'
    path = '/etc/os-release'
    collected_facts = {}

    result, suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, path, collected_facts)

    assert result is True
    assert suse_facts['distribution'] == 'SLES'
    assert suse_facts['distribution_version'] == '12.3'
    assert suse_facts['distribution_major_version'] == '12'
    assert suse_facts['distribution_release'] == '3'

def test_parse_distribution_file_SUSE_open_SuSE_release(mock_os_path_islink, mock_os_path_realpath, mock_get_file_content, mock_module):
    distribution_files = DistributionFiles(mock_module)
    name = 'openSUSE'
    data = 'openSUSE 13.2 (Harlequin) (x86_64)\nCODENAME = Harlequin'
    path = '/etc/SuSE-release'
    collected_facts = {'distribution_version': '13.2'}

    result, suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, path, collected_facts)

    assert result is True
    assert suse_facts['distribution'] == 'openSUSE'
    assert suse_facts['distribution_release'] == 'Harlequin'

def test_parse_distribution_file_SUSE_enterprise_SuSE_release(mock_os_path_islink, mock_os_path_realpath, mock_get_file_content, mock_module):
    distribution_files = DistributionFiles(mock_module)
    name = 'SLES'
    data = 'SUSE Linux Enterprise Server 12\nPATCHLEVEL = 3'
    path = '/etc/SuSE-release'
    collected_facts = {'distribution_version': '12'}

    result, suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, path, collected_facts)

    assert result is True
    assert suse_facts['distribution'] == 'SLES'
    assert suse_facts['distribution_release'] == '3'
    assert suse_facts['distribution_version'] == '12.3'

def test_parse_distribution_file_SUSE_SLES_SAP(mock_os_path_islink, mock_os_path_realpath, mock_get_file_content, mock_module):
    mock_os_path_islink.return_value = True
    mock_os_path_realpath.return_value = '/etc/products.d/SLES_SAP.prod'
    distribution_files = DistributionFiles(mock_module)
    name = 'SLES_SAP'
    data = 'NAME="SLES_SAP"\nVERSION_ID="12.3"\nPRETTY_NAME="SUSE Linux Enterprise Server for SAP Applications 12 SP3"'
    path = '/etc/os-release'
    collected_facts = {}

    result, suse_facts = distribution_files.parse_distribution_file_SUSE(name, data, path, collected_facts)

    assert result is True
    assert suse_facts['distribution'] == 'SLES_SAP'
