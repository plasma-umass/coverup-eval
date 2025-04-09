# file: lib/ansible/module_utils/facts/other/facter.py:46-50
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from unittest.mock import Mock

class TestFacterFactCollector:
    
    @pytest.fixture
    def facter_collector(self):
        return FacterFactCollector()

    def test_run_facter_success(self, facter_collector):
        module = Mock()
        module.run_command = Mock(return_value=(0, '{"fact": "value"}', ''))
        facter_path = "/usr/bin/facter"
        
        rc, out, err = facter_collector.run_facter(module, facter_path)
        
        module.run_command.assert_called_once_with(facter_path + " --puppet --json")
        assert rc == 0
        assert out == '{"fact": "value"}'
        assert err == ''

    def test_run_facter_failure(self, facter_collector):
        module = Mock()
        module.run_command = Mock(return_value=(1, '', 'error'))
        facter_path = "/usr/bin/facter"
        
        rc, out, err = facter_collector.run_facter(module, facter_path)
        
        module.run_command.assert_called_once_with(facter_path + " --puppet --json")
        assert rc == 1
        assert out == ''
        assert err == 'error'
