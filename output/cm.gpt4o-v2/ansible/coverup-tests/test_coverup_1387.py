# file: lib/ansible/module_utils/facts/system/distribution.py:167-208
# asked: {"lines": [185, 186, 187, 188], "branches": [[175, 208], [184, 185], [197, 175]]}
# gained: {"lines": [185, 186, 187, 188], "branches": [[184, 185]]}

import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def distribution_files():
    from ansible.module_utils.facts.system.distribution import DistributionFiles
    module = MagicMock()
    return DistributionFiles(module)

def test_process_dist_files_all_branches(distribution_files):
    mock_osdist_list = [
        {'path': '/etc/arch-release', 'name': 'Archlinux', 'allowempty': True},
        {'path': '/etc/redhat-release', 'name': 'RedHat'}
    ]

    with patch.object(distribution_files, 'OSDIST_LIST', mock_osdist_list):
        with patch.object(distribution_files, '_guess_distribution', return_value={'distribution': 'TestDistro'}):
            with patch.object(distribution_files, '_get_dist_file_content', side_effect=[(True, ''), (True, 'RedHat')]):
                with patch.object(distribution_files, '_parse_dist_file', return_value=(True, {'distribution': 'RedHat'})):
                    result = distribution_files.process_dist_files()
                    assert result['distribution'] == 'Archlinux'
                    assert result['distribution_file_path'] == '/etc/arch-release'
                    assert result['distribution_file_variety'] == 'Archlinux'

    # Test the second branch separately
    mock_osdist_list = [
        {'path': '/etc/redhat-release', 'name': 'RedHat'}
    ]

    with patch.object(distribution_files, 'OSDIST_LIST', mock_osdist_list):
        with patch.object(distribution_files, '_guess_distribution', return_value={'distribution': 'TestDistro'}):
            with patch.object(distribution_files, '_get_dist_file_content', return_value=(True, 'RedHat')):
                with patch.object(distribution_files, '_parse_dist_file', return_value=(True, {'distribution': 'RedHat'})):
                    result = distribution_files.process_dist_files()
                    assert result['distribution'] == 'RedHat'
                    assert result['distribution_file_path'] == '/etc/redhat-release'
                    assert result['distribution_file_variety'] == 'RedHat'
                    assert result['distribution_file_parsed'] == True
