# file thefuck/conf.py:75-80
# lines [77, 78, 79, 80]
# branches ['78->79', '78->80']

import pytest
from unittest import mock

class TestSettings:
    def test_rules_from_env(self, mocker):
        from thefuck.conf import Settings
        from thefuck import const

        settings = Settings()

        # Mocking const.DEFAULT_RULES to ensure it has a known value
        mock_default_rules = ['rule1', 'rule2']
        mocker.patch.object(const, 'DEFAULT_RULES', mock_default_rules)

        # Test case where 'DEFAULT_RULES' is in the input
        env_val = 'DEFAULT_RULES:rule3:rule4'
        expected_result = mock_default_rules + ['rule3', 'rule4']
        result = settings._rules_from_env(env_val)
        assert result == expected_result

        # Test case where 'DEFAULT_RULES' is not in the input
        env_val = 'rule5:rule6'
        expected_result = ['rule5', 'rule6']
        result = settings._rules_from_env(env_val)
        assert result == expected_result
