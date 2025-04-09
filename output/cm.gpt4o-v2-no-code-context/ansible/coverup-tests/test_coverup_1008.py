# file: lib/ansible/module_utils/facts/system/fips.py:26-37
# asked: {"lines": [32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37], "branches": [[35, 36], [35, 37]]}

import pytest
from ansible.module_utils.facts.system.fips import FipsFactCollector
from unittest.mock import patch

@pytest.fixture
def fips_collector():
    return FipsFactCollector()

def test_collect_fips_disabled(fips_collector, mocker):
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='0')
    result = fips_collector.collect()
    assert result == {'fips': False}

def test_collect_fips_enabled(fips_collector, mocker):
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value='1')
    result = fips_collector.collect()
    assert result == {'fips': True}

def test_collect_fips_no_data(fips_collector, mocker):
    mocker.patch('ansible.module_utils.facts.system.fips.get_file_content', return_value=None)
    result = fips_collector.collect()
    assert result == {'fips': False}
