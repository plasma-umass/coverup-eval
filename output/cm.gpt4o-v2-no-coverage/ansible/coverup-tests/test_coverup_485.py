# file: lib/ansible/module_utils/facts/system/distribution.py:568-576
# asked: {"lines": [568, 569, 570, 571, 572, 573, 574, 575, 576], "branches": [[573, 574], [573, 576]]}
# gained: {"lines": [568, 569, 570, 571, 572, 573, 574, 575, 576], "branches": [[573, 574]]}

import pytest
from unittest.mock import Mock

class TestDistribution:
    
    @pytest.fixture
    def distribution(self):
        from ansible.module_utils.facts.system.distribution import Distribution
        module = Mock()
        return Distribution(module)
    
    def test_get_distribution_Darwin(self, distribution):
        # Mock the run_command method
        distribution.module.run_command = Mock(return_value=(0, "10.15.7", ""))
        
        # Call the method
        result = distribution.get_distribution_Darwin()
        
        # Assertions
        assert result['distribution'] == 'MacOSX'
        assert result['distribution_major_version'] == '10'
        assert result['distribution_version'] == '10.15.7'
        
        # Clean up / ensure no state pollution
        distribution.module.run_command.assert_called_once_with("/usr/bin/sw_vers -productVersion")
