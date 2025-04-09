# file: lib/ansible/module_utils/facts/system/distribution.py:167-208
# asked: {"lines": [167, 170, 172, 173, 175, 176, 177, 178, 180, 184, 185, 186, 187, 188, 190, 192, 194, 197, 198, 199, 203, 204, 205, 206, 208], "branches": [[175, 176], [175, 208], [184, 185], [184, 190], [190, 192], [190, 194], [197, 175], [197, 198]]}
# gained: {"lines": [167, 170, 172, 173, 175, 176, 177, 178, 180, 184, 185, 186, 187, 188, 190, 192, 194, 197, 198, 199, 203, 204, 205, 206, 208], "branches": [[175, 176], [175, 208], [184, 185], [184, 190], [190, 192], [190, 194], [197, 198]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DistributionFiles class and its methods are imported from the module
from ansible.module_utils.facts.system.distribution import DistributionFiles

@pytest.fixture
def dist_files():
    module = MagicMock()
    return DistributionFiles(module)

def test_process_dist_files_guess_distribution(dist_files):
    with patch.object(DistributionFiles, '_guess_distribution', return_value={'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}):
        with patch.object(DistributionFiles, '_get_dist_file_content', return_value=(False, None)):
            dist_files.OSDIST_LIST = [{'name': 'TestOS', 'path': '/etc/testos-release', 'allowempty': False}]
            result = dist_files.process_dist_files()
            assert result == {'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}

def test_process_dist_files_with_dist_file(dist_files):
    with patch.object(DistributionFiles, '_guess_distribution', return_value={'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}):
        with patch.object(DistributionFiles, '_get_dist_file_content', return_value=(True, 'TestOS Content')):
            with patch.object(DistributionFiles, '_parse_dist_file', return_value=(True, {'distribution': 'TestOS'})):
                dist_files.OSDIST_LIST = [{'name': 'TestOS', 'path': '/etc/testos-release', 'allowempty': False}]
                result = dist_files.process_dist_files()
                assert result == {
                    'distribution': 'TestOS',
                    'distribution_version': '1.0',
                    'distribution_release': 'TestRelease',
                    'distribution_major_version': '1',
                    'distribution_file_path': '/etc/testos-release',
                    'distribution_file_variety': 'TestOS',
                    'distribution_file_parsed': True
                }

def test_process_dist_files_with_empty_allowed(dist_files):
    with patch.object(DistributionFiles, '_guess_distribution', return_value={'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}):
        with patch.object(DistributionFiles, '_get_dist_file_content', return_value=(True, '')):
            dist_files.OSDIST_LIST = [{'name': 'TestOS', 'path': '/etc/testos-release', 'allowempty': True}]
            result = dist_files.process_dist_files()
            assert result == {
                'distribution': 'TestOS',
                'distribution_version': '1.0',
                'distribution_release': 'TestRelease',
                'distribution_major_version': '1',
                'distribution_file_path': '/etc/testos-release',
                'distribution_file_variety': 'TestOS'
            }

def test_process_dist_files_no_dist_file(dist_files):
    with patch.object(DistributionFiles, '_guess_distribution', return_value={'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}):
        with patch.object(DistributionFiles, '_get_dist_file_content', return_value=(False, None)):
            dist_files.OSDIST_LIST = [{'name': 'TestOS', 'path': '/etc/testos-release', 'allowempty': False}]
            result = dist_files.process_dist_files()
            assert result == {'distribution': 'TestOS', 'distribution_version': '1.0', 'distribution_release': 'TestRelease', 'distribution_major_version': '1'}
