# file: lib/ansible/module_utils/facts/system/distribution.py:547-557
# asked: {"lines": [547, 548, 549, 550, 551, 552, 553, 554, 556, 557], "branches": [[552, 553], [552, 556]]}
# gained: {"lines": [547, 548, 549, 550, 551, 552, 553, 554, 556, 557], "branches": [[552, 553], [552, 556]]}

import pytest
from unittest.mock import Mock

class TestDistribution:
    
    @pytest.fixture
    def distribution(self):
        from ansible.module_utils.facts.system.distribution import Distribution
        module = Mock()
        return Distribution(module)
    
    def test_get_distribution_AIX_major_version_only(self, distribution):
        distribution.module.run_command = Mock(return_value=(0, "7", ""))
        result = distribution.get_distribution_AIX()
        assert result == {
            'distribution_major_version': '7',
            'distribution_version': '7'
        }
    
    def test_get_distribution_AIX_major_and_minor_version(self, distribution):
        distribution.module.run_command = Mock(return_value=(0, "7.2", ""))
        result = distribution.get_distribution_AIX()
        assert result == {
            'distribution_major_version': '7',
            'distribution_version': '7.2',
            'distribution_release': '2'
        }
    
    def test_get_distribution_AIX_error(self, distribution):
        distribution.module.run_command = Mock(return_value=(1, "", "error"))
        result = distribution.get_distribution_AIX()
        assert result == {
            'distribution_major_version': '',
            'distribution_version': ''
        }
