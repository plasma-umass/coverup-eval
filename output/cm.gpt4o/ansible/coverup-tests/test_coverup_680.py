# file lib/ansible/module_utils/facts/system/lsb.py:27-31
# lines [27, 28, 29, 30]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.lsb import LSBFactCollector, BaseFactCollector

@pytest.fixture
def mock_base_fact_collector(mocker):
    mocker.patch('ansible.module_utils.facts.system.lsb.BaseFactCollector', autospec=True)

def test_lsb_fact_collector_initialization(mock_base_fact_collector):
    collector = LSBFactCollector()
    assert collector.name == 'lsb'
    assert collector._fact_ids == set()
    assert collector.STRIP_QUOTES == r'\'\"\\'

def test_lsb_fact_collector_inheritance(mock_base_fact_collector):
    collector = LSBFactCollector()
    assert isinstance(collector, BaseFactCollector)
