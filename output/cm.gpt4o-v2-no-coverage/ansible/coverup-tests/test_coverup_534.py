# file: lib/ansible/module_utils/facts/system/distribution.py:559-566
# asked: {"lines": [559, 560, 561, 562, 563, 564, 565, 566], "branches": [[563, 564], [563, 566]]}
# gained: {"lines": [559, 560, 561, 562, 563, 564, 565, 566], "branches": [[563, 564], [563, 566]]}

import pytest
from unittest.mock import Mock

class TestDistribution:
    @pytest.fixture
    def distribution(self, mocker):
        from ansible.module_utils.facts.system.distribution import Distribution
        module_mock = mocker.Mock()
        return Distribution(module=module_mock)

    def test_get_distribution_HPUX_no_match(self, distribution, mocker):
        distribution.module.run_command = Mock(return_value=(0, "No match here", ""))
        
        result = distribution.get_distribution_HPUX()
        
        assert result == {}

    def test_get_distribution_HPUX_with_match(self, distribution, mocker):
        distribution.module.run_command = Mock(return_value=(0, "HPUX OE A.11.31.1805 something", ""))
        
        result = distribution.get_distribution_HPUX()
        
        assert result == {
            'distribution_version': 'A.11.31',
            'distribution_release': '1805'
        }
