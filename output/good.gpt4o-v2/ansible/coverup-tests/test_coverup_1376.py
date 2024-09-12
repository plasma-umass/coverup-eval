# file: lib/ansible/module_utils/facts/system/distribution.py:600-609
# asked: {"lines": [601, 602, 604, 605, 606, 607, 608, 609], "branches": [[606, 607], [606, 609]]}
# gained: {"lines": [601, 602, 604, 605, 606, 607, 608, 609], "branches": [[606, 607]]}

import pytest
import re
from unittest.mock import Mock, patch

class TestDistribution:
    @pytest.fixture
    def distribution(self):
        from ansible.module_utils.facts.system.distribution import Distribution
        module = Mock()
        return Distribution(module)

    @patch('platform.release', return_value="5.8-RELEASE")
    def test_get_distribution_DragonFly(self, mock_release, distribution):
        # Mock run_command
        distribution.module.run_command = Mock(return_value=(0, "DragonFly v5.8.2-RELEASE #0: Tue Jan  1 00:00:00 UTC 2020", ""))

        # Run the method
        result = distribution.get_distribution_DragonFly()

        # Assertions
        assert result['distribution_release'] == "5.8-RELEASE"
        assert result['distribution_major_version'] == '5'
        assert result['distribution_version'] == '5.8.2'
